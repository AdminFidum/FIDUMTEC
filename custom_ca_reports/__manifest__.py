# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Accounting Reports - Custom turnover',
    'version': '1.1',
    'category': 'Accounting & Finance',
    'description': """
        A custom report to get turnover by country/partner
    """,
    'depends': [
        'account_reports', 'account_accountant'
    ],
    'data': [
        'views/turnover_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'OEEL-1',
}
