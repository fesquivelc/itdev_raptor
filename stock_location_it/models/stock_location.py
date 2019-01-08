# coding=utf-8

from odoo import models, api, fields


class StockLocationIt(models.Model):
    _name = 'stock.location.it'

    name = fields.Char(u'Ubicación')
    product_ids = fields.One2many('product.product', 'location_it_id', u'Productos')
