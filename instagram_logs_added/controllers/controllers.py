# -*- coding: utf-8 -*-
# from odoo import http


# class InstagramLogsAdded(http.Controller):
#     @http.route('/instagram_logs_added/instagram_logs_added', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/instagram_logs_added/instagram_logs_added/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('instagram_logs_added.listing', {
#             'root': '/instagram_logs_added/instagram_logs_added',
#             'objects': http.request.env['instagram_logs_added.instagram_logs_added'].search([]),
#         })

#     @http.route('/instagram_logs_added/instagram_logs_added/objects/<model("instagram_logs_added.instagram_logs_added"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('instagram_logs_added.object', {
#             'object': obj
#         })

