# -*- coding: utf-8 -*-
{
    'name': "ks_accounting_reports",

    'summary': """
        Optimización de los Reportes Contables""",

    'author': "Keep It Simple",
    'website': "http://kisforce.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/account_general_ledger.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
