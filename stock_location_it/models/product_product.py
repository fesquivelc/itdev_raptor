# coding=utf-8

from odoo import fields, models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    location_it_id = fields.Many2one('stock.location.it', u'Ubicación')
