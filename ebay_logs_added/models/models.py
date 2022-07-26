# -*- coding: utf-8 -*-

# from odoo import models, fields, api


from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ebay_logs_added(models.Model):
    _inherit = 'product.template'

    def push_product_ebay(self):
        for product in self:
            if product.ebay_listing_status != 'Active':
                item_dict = product._get_item_dict()
                _logger.warning(item_dict)

        res = super(ebay_logs_added, self).push_product_ebay()
        return res


    @api.model
    def ebay_execute(self, verb, data=None, list_nodes=[], verb_attrs=None, files=None):
        _logger.warning("verb")
        _logger.warning(verb)
        _logger.warning("data")
        _logger.warning(data)
        _logger.warning("list nodes")
        _logger.warning(list_nodes)
        _logger.warning("verb_attrs")
        _logger.warning(verb_attrs)

        res = super(ebay_logs_added, self).ebay_execute()
        return res

