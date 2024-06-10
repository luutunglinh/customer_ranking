
# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _

class CustomerLoyaltyReward(models.Model):
    _inherit = 'loyalty.reward'

    is_rank = fields.Boolean(related='program_id.is_rank', store= False)
    ranking_reward = fields.Many2one('rank.program')
    required_point = fields.Float(compute='_compute_required_points', store= True)

    @api.depends('ranking_reward')
    def _compute_required_points(self):
        for record in self:
            if record.is_rank and record.program_type == 'loyalty':
                if record.ranking_reward:
                    record.required_point = record.ranking_reward.revenue_require
            else:
                record.required_point = 0


