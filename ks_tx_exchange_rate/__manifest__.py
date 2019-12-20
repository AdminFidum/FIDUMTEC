# -*- coding: utf-8 -*-
{
    'name': "ks_tx_exchange_rate",

    'summary': """
        Tipo de Cambio en el CRM """,

    'description': """
        Se habilita la multimoneda en las oportunidades, presupuesto y ordenes de venta. Adicional se visualiza la tasa de cambio de en la invoice y la entrada de diario asociada
    """,

    'author': "Keep It Simple",
    'website': "http://kisforce.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm','sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/crm_lead.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
