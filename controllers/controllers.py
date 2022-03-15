# -*- coding: utf-8 -*-
# from odoo import http


# class TokoZhafron(http.Controller):
#     @http.route('/toko_zhafron/toko_zhafron/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/toko_zhafron/toko_zhafron/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('toko_zhafron.listing', {
#             'root': '/toko_zhafron/toko_zhafron',
#             'objects': http.request.env['toko_zhafron.toko_zhafron'].search([]),
#         })

#     @http.route('/toko_zhafron/toko_zhafron/objects/<model("toko_zhafron.toko_zhafron"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('toko_zhafron.object', {
#             'object': obj
#         })
