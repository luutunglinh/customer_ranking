# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools


class CustomerCardProgram(models.Model):
    _inherit = "loyalty.card"


    is_rank = fields.Boolean(related='program_id.is_rank')
    current_rank = fields.Char(string="Current Rank", compute="_compute_current_rank", store=True)
    ranking_rule = fields.One2many(string="Ranking Rule", related='program_id.rule_ids.ranking_rule')
    partner_id = fields.Many2one('res.partner', string="Partner")


    @api.depends('points')
    def _compute_current_rank(self):
        for record in self:
            record.current_rank = ""
            rank = sorted(record.ranking_rule, key=lambda r: r.revenue_require, reverse=True)
            if rank:
                for item in rank:
                    if record.points > item.revenue_require:
                        record.current_rank = item.name
                        break
                    else:
                        record.current_rank = "None"
            else:
                record.current_rank = "None"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            program_id = self.env['loyalty.program'].sudo().search([('id','=', vals['program_id'])])
            user_id = self.env['res.partner'].sudo().search([('id','=', vals['program_id'])])
            if program_id.is_rank and program_id.program_type == 'loyalty':
                vals['points'] = user_id.total_revenue
        res = super(CustomerCardProgram, self).create(vals_list)
        return res

