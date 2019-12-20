# -*- coding: utf-8 -*-
{
    'name': "ks_opportunity_sequence",

    'summary': """
        Add a custom sequence on oppotunity record""",

    'description': """
        Add a custom sequence on oppotunity record get this information from customer record
    """,

    'author': "Keep It Simple",
    'website': "http://www.kisforce.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customer Relationship Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'crm'
    ],
    "demo":[],
    "installable":True
}
