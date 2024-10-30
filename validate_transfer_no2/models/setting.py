from odoo import models, fields, api

class LocationProductRule(models.Model):
    _name = 'tbl_location_product_rule'
    _description = 'Location Product Rules'

    location_id = fields.Many2one('stock.location', string='Location', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('location_product_unique', 'unique(location_id, product_id)',
         'Each product can only be assigned once per location!')
    ]
