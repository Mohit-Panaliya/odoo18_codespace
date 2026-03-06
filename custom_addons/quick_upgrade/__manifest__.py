# -*- coding: utf-8 -*-
{
    'name': "Quick Module Upgrade",
    'summary': "Quick upgrade custom modules from a simple page",
    'description': """
        Quick module upgrade via a simple page.
        Shows list of all installed custom modules and allows one-click upgrade.
    """,
    'author': "Custom",
    'website': "",
    'category': 'Tools',
    'version': '1.0',
    'depends': ['base', 'web'],
    'data': [
        'views/quick_upgrade.xml',
        'views/quick_upgrade_menu.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
