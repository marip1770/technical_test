from odoo import models, fields,_

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    cancel_reason_id = fields.Many2one(
        'tbl_cancel_reason', 
        string='Cancel Reason', 
        help='Reason for canceling the Sales Order',
        readonly=True
    )

    def action_cancel_order(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Cancel Reason'),
            'view_mode': 'form',
            'res_model': 'tbl_cancel_reason_wizard',
            'target': 'new',
            'context': {'default_order_id': self.id},
        }
