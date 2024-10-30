from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import timedelta

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    estimated_production_time = fields.Float(
        string='Estimated Production Time (hours)',compute='_compute_estimated_time', store=True
    )

    @api.depends('product_id', 'bom_id')
    def _compute_estimated_time(self):
        for rec in self:
            if rec.bom_id:
                total_time = sum(operation.time_cycle for operation in rec.bom_id.operation_ids)
                if total_time > 0:
                    total_time = total_time/60
                rec.estimated_production_time = total_time or 1.0

    def action_plan_production(self):
        if not self.date_planned_start:
            raise UserError(_("Please specify the planned start date."))

        start_date = self.date_planned_start
        end_date = start_date + timedelta(hours=self.estimated_production_time)

        self.write({
            'date_planned_finished': end_date,
        })
        start = self.date_planned_start
        if self.bom_id.operation_ids and self.workorder_ids:
            for line in self.workorder_ids:
                for bom_line in self.bom_id.operation_ids:
                    if line.name == bom_line.name and line.workcenter_id.id == bom_line.workcenter_id.id:
                        end = start + timedelta(minutes=bom_line.time_cycle)
                        line.date_planned_start = start
                        line.date_planned_finished = end
                        start = end
        return {
            'effect': {
                'fadeout': 'slow',
                'message': _("Production has been successfully scheduled."),
                'type': 'rainbow_man',
            }
        }