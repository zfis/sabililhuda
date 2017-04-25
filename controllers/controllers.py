# -*- coding: utf-8 -*-
from odoo import http

# class Addons/sabililhuda(http.Controller):
#     @http.route('/addons/sabililhuda/addons/sabililhuda/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/sabililhuda/addons/sabililhuda/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/sabililhuda.listing', {
#             'root': '/addons/sabililhuda/addons/sabililhuda',
#             'objects': http.request.env['addons/sabililhuda.addons/sabililhuda'].search([]),
#         })

#     @http.route('/addons/sabililhuda/addons/sabililhuda/objects/<model("addons/sabililhuda.addons/sabililhuda"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/sabililhuda.object', {
#             'object': obj
#         })