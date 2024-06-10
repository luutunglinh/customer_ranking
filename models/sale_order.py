
from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_revenue_partner = fields.Float(related='partner_id.total_revenue')
    current_rank_partner = fields.Char(related='partner_id.current_rank')

