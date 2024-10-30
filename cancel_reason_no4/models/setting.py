from odoo import models, fields

class CancelReason(models.Model):
    _name = 'tbl_cancel_reason'
    _description = 'Sales Order Cancel Reason'

    name = fields.Char(string='Reason Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
