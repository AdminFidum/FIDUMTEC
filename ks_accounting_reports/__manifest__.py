# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'KS Accounting Reports',
    'version': '1.0.0',
    'category': 'reporting',
    'description': """
        A custom report to colombian localization
    """,
    'depends': [
        'account_reports'
    ],
    'data': [
        'views/ks_general_ledger.xml',
    ],
    'installable': True,
    'auto_install': False,
}
