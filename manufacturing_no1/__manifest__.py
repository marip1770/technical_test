# -*- coding: utf-8 -*-
{
    'name': "Kustomisasi Modul Manufaktur (No 1)",

    'summary': """
        Module ini merupakan jawab untuk test No 1""",

    'description': """
        Module ini merupakan jawab untuk test No 1
    """,

    'author': "Mochamad Ari Pratama",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp'],

    # always loaded
    'data': [
        'views/mrp_production_views.xml',
    ],
}
