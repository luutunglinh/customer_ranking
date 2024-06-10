# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
import re


class RankProgram(models.Model):
    _name = "rank.program"
    _description = "Rank Program"

    name = fields.Char(string="Rank Name")
    revenue_require = fields.Float(string="Revenue Required", default=0)
    customer_loyalty_rule = fields.Many2one('loyalty.rule')
    customer_loyalty_reward_id = fields.One2many('loyalty.reward','ranking_reward')



