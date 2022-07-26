# -*- coding: utf-8 -*-
# from odoo import http


# class EbayLogsAdded(http.Controller):
#     @http.route('/ebay_logs_added/ebay_logs_added', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ebay_logs_added/ebay_logs_added/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ebay_logs_added.listing', {
#             'root': '/ebay_logs_added/ebay_logs_added',
#             'objects': http.request.env['ebay_logs_added.ebay_logs_added'].search([]),
#         })

#     @http.route('/ebay_logs_added/ebay_logs_added/objects/<model("ebay_logs_added.ebay_logs_added"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ebay_logs_added.object', {
#             'object': obj
#         })

