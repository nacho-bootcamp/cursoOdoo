# -*- coding: utf-8 -*-
# from odoo import http


# class MiSegundoModulo(http.Controller):
#     @http.route('/mi_segundo_modulo/mi_segundo_modulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mi_segundo_modulo/mi_segundo_modulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mi_segundo_modulo.listing', {
#             'root': '/mi_segundo_modulo/mi_segundo_modulo',
#             'objects': http.request.env['mi_segundo_modulo.mi_segundo_modulo'].search([]),
#         })

#     @http.route('/mi_segundo_modulo/mi_segundo_modulo/objects/<model("mi_segundo_modulo.mi_segundo_modulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mi_segundo_modulo.object', {
#             'object': obj
#         })

