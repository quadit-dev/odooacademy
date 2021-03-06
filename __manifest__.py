# Copyright 2018, ChartCXM
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'OdooAcademy',
    'summary': 'This module for test purposes',
    'version': '11.0.1.0.0',
    'category': 'Hidden',
    'website': 'http://www.chartcxm.com',
    'author': 'ChartCXM',
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'depends': ['base', 'account'],
    'data': [
        'views/courses_view.xml',
        'views/sessions_view.xml',
        'views/partner_view.xml',
    ],
}
