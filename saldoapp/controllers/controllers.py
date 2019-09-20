# -*- coding: utf-8 -*-
from odoo import http

# class Calorias(http.Controller):
#     @http.route('/calorias/calorias/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/calorias/calorias/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('calorias.listing', {
#             'root': '/calorias/calorias',
#             'objects': http.request.env['calorias.calorias'].search([]),
#         })

#     @http.route('/calorias/calorias/objects/<model("calorias.calorias"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('calorias.object', {
#             'object': obj
#         })