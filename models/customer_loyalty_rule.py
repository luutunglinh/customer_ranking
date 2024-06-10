
# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _

class CustomerLoyalty(models.Model):
    _inherit = 'loyalty.rule'

    ranking_rule = fields.One2many('rank.program', 'customer_loyalty_rule')
    is_rank = fields.Boolean(related='program_id.is_rank')
