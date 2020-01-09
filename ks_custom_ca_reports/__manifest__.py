# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{        
    'name': "ks_custom_ca_reports",

    'summary': """
        """,

    'description': """
        Helps you handle your accounting needs, if you are not an accountant, we suggest you to install only the Invoicing.
    """,

    'author': "Keep It Simple",
    'website': "http://www.kisforce.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting &amp; Finance',
    'version': '0.1',

    # always loaded
    'data': [
        'views/turnover_view.xml',
    ],

    # any module necessary for this one to work correctly
    'depends': [
        'account_accountant'
    ],
    "demo":[],
    "installable":True
}
