# coding=utf-8
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class StockConfiguration(models.Model):
    _name = 'stock.parameters.it'

    name = fields.Char('Nombre', size=50, default=u'Parámetros de venta')
    default_product_followers = fields.Many2many('res.users', 'rel_def_followers_users',
                                                 string=u'Seguidores de producto')
