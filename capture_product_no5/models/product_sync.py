import requests
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    synced_with_z = fields.Boolean(string='Synced with Z*', default=False)

    def _send_to_z(self, data):
        url = "https://api.z.com/sync_product"  # URL API Aplikasi Z*
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(url, json=data, headers=headers, timeout=10)
            response.raise_for_status()  # Memastikan respons sukses
            _logger.info(f"Product {data['name']} synced successfully.")
        except requests.exceptions.RequestException as e:
            _logger.error(f"Failed to sync product: {e}")

    @api.model
    def create(self, vals):
        records = super(ProductTemplate, self).create(vals)
        for record in records:
            record._send_to_z(record._prepare_sync_data())
        return records

    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        for record in self:
            if not record.synced_with_z:
                record._send_to_z(record._prepare_sync_data())
                record.synced_with_z = True
        return res

    def _prepare_sync_data(self):
        return {
            'id': self.id,
            'name': self.name,
            'default_code': self.default_code,
            'list_price': self.list_price,
            'type': self.type,
            'active': self.active,
        }
