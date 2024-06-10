from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    total_revenue = fields.Float(string="Total Revenue", compute="_compute_total_revenue")

    total_discount = fields.Float(string="Total Discount")

    current_rank = fields.Char("Current Rank", compute='_compute_current_rank')

    custom_ids = fields.One2many('loyalty.card', 'partner_id', string="Custom Records")

    @api.depends('sale_order_ids.state', 'sale_order_ids.amount_total')
    def _compute_total_revenue(self):
        for record in self:
            total = sum(order.amount_total for order in record.sale_order_ids if order.state in ['sale'])
            print(total)
            record.total_revenue = total

    @api.depends('custom_ids.points')
    def _compute_current_rank(self):
        for record in self:
            record.current_rank = ""
            for item in record.custom_ids:
                if item.program_type == 'loyalty' and item.is_rank:
                    ranking = item
                    if ranking:
                        for r in ranking:
                            record.current_rank = r.current_rank
                    else:
                        record.current_rank = "None"


