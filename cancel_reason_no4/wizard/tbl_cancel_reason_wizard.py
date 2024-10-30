from odoo import models, fields, api

class SaleOrderCancelWizard(models.TransientModel):
    _name = 'tbl_cancel_reason_wizard'
    _description = 'Wizard for Sale Order Cancel Reason'

    order_id = fields.Many2one('sale.order', string='Sale Order', required=True)
    cancel_reason_id = fields.Many2one('tbl_cancel_reason', string='Cancel Reason', required=True)

    def confirm_cancel(self):
        self.order_id.cancel_reason_id = self.cancel_reason_id
        self.order_id.action_cancel()
