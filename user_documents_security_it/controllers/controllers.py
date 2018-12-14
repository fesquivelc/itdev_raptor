# -*- coding: utf-8 -*-
from odoo import http

# class UserDocumentsSecurityIt(http.Controller):
#     @http.route('/user_documents_security_it/user_documents_security_it/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/user_documents_security_it/user_documents_security_it/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('user_documents_security_it.listing', {
#             'root': '/user_documents_security_it/user_documents_security_it',
#             'objects': http.request.env['user_documents_security_it.user_documents_security_it'].search([]),
#         })

#     @http.route('/user_documents_security_it/user_documents_security_it/objects/<model("user_documents_security_it.user_documents_security_it"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('user_documents_security_it.object', {
#             'object': obj
#         })