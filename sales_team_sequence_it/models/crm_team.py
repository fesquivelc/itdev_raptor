# coding=utf-8
from odoo import models, api, fields


class CRMTeam(models.Model):
    _inherit = 'crm.team'

    sequence_prefix = fields.Char(u'Prefijo')
