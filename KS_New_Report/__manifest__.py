# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'ks_new_report',
    'version': '1.1',
    'category': 'reporting',
    'description': """
        A custom report to get turnover by country/partner
    """,
    'depends': [
        'account_reports'
    ],
    'data': [
        'views/KS_Report_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'OEEL-1',
}
