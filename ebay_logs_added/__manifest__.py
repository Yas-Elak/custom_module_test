# -*- coding: utf-8 -*-
{
    'name': "ebay_logs_added",

    'summary': """
       Add logs for ebay""",

    'description': """
        Add logs for ebay
    """,

    'author': "Odoo YLA",
    'website': "",
    'license': 'LGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'stock', 'delivery', 'attachment_indexation', 'sale_ebay'],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [],
}
