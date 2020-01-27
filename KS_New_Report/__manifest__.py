# -*- coding: utf-8 -*-
{
    'name': "ks_new_report",

    'summary': """
        """,

    'description': """
        
    """,
    'category': 'reporting',

    'author': "Keep It Simple",
    'website': "http://www.kisforce.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'account_reports'
    ],
    'data': [
        'views/KS_Report_view.xml',
    ],
    "demo":[],
    "installable":True
}
