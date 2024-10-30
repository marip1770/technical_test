from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

class Inventory(models.Model):
    _inherit = 'stock.inventory'

    state = fields.Selection(string='Status', selection=[
        ('draft', 'Draft'),
        ('cancel', 'Cancelled'),
        ('waiting', 'Waiting for Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('confirm', 'In Progress'),
        ('done', 'Validated')],
        copy=False, index=True, readonly=True, tracking=True,
        default='draft')

    def _action_start(self):
        """ Confirms the Inventory Adjustment and generates its inventory lines
        if its state is draft and don't have already inventory lines (can happen
        with demo data or tests).
        """
        for inventory in self:
            if inventory.state != 'approved':
                continue
            vals = {
                'state': 'confirm',
                'date': fields.Datetime.now()
            }
            if not inventory.line_ids and not inventory.start_empty:
                self.env['stock.inventory.line'].create(inventory._get_inventory_lines_values())
            inventory.write(vals)


    def action_request_approval(self):
        if self.state != 'draft':
            raise UserError(_("Only drafts can be submitted for approval."))
        self.write({'state': 'waiting'})
    
    def action_approve(self):
        if not self.env.user.has_group('stock.group_stock_manager'):
            raise UserError(_("Only Warehouse Managers can approve adjustments."))
        self.write({'state': 'approved'})

    def action_reject(self):
        if not self.env.user.has_group('stock.group_stock_manager'):
            raise UserError(_("Only Warehouse Managers can reject adjustments."))
        self.write({'state': 'rejected'})

    def action_cancel_to_draft(self):
        if self.state != 'rejected':
            raise UserError(_("Only rejected adjustments can be Cancel."))
        self.write({'state': 'draft'})
