# __manifest__.py

{
    'name': 'Nasrat Inventory',
    'version': '17.0.0.0.1',
    'category': 'inventory  Customization',
    'summary': 'this is just for whole inventory',
    'sequence': -3,
    'description': """
      this is belongs to all inventory version 17
    """,
    'author': 'Nasrat Nasrati',
    'website': 'https://www.example.com',
    'depends': ['stock'],
    'data': [
        'data/user_default_data.xml',
        'security/user_category.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'qweb': [
        'static/src/xml/user_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'Nasrat-Inventory/static/src/js/extended_user_menu.js',
        ],
    }
}
