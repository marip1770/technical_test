from odoo import models, api, _
from odoo.exceptions import ValidationError

class Picking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        for record in self:
            list = None
            for move_line in record.move_ids_without_package:
                if move_line.quantity_done > 0:
                    valid_product = self.env['tbl_location_product_rule'].search([
                        ('location_id', '=', record.location_dest_id.id),
                        ('product_id', '=', move_line.product_id.id),
                        ('active', '=', True)
                    ], limit=1)
                    if not valid_product:
                        if list:
                            list += f"\n- {move_line.product_id.display_name}"
                        else:
                            list = f"- {move_line.product_id.display_name}"
            if list:
                raise ValidationError(_(f"Product :\n{list}\nis not allowed in destination location '{record.location_dest_id.display_name}'."))
        
        res = super(Picking, self).button_validate()
        return res
