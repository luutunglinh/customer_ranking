
# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _

class CustomerLoyaltyProgram(models.Model):
    _inherit = 'loyalty.program'

    is_rank = fields.Boolean('Ranking')

