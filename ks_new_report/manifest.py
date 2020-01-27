# -*- coding: utf-8 -*-
{
    'name': "ks_new_qweb_report",

    'summary': """
        Creación de un reporte qweb""",

    'description': """
        Creación de un reporte qweb
    """,

    'author': "Keep It Simple",
    'website': "http://www.kisforce.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'reporting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'account_accountant'
    ],
    "demo":[],
    "installable":True
}
