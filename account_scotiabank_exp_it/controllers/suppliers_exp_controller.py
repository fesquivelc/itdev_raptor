# -*- coding: utf-8 -*-
from odoo import http

# class AccountScotiabankExpIt(http.Controller):
#     @http.route('/account_scotiabank_exp_it/account_scotiabank_exp_it/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_scotiabank_exp_it/account_scotiabank_exp_it/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_scotiabank_exp_it.listing', {
#             'root': '/account_scotiabank_exp_it/account_scotiabank_exp_it',
#             'objects': http.request.env['account_scotiabank_exp_it.account_scotiabank_exp_it'].search([]),
#         })

#     @http.route('/account_scotiabank_exp_it/account_scotiabank_exp_it/objects/<model("account_scotiabank_exp_it.account_scotiabank_exp_it"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_scotiabank_exp_it.object', {
#             'object': obj
#         })