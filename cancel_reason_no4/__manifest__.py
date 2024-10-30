# -*- coding: utf-8 -*-
{
    'name': "Cancel Reason (No 4)",

    'summary': """
        Module ini merupakan jawab untuk test No 4""",

    'description': """
        Module ini merupakan jawab untuk test No 4
    """,

    'author': "Mochamad Ari Pratama",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/tbl_cancel_reason_wizard_views.xml',
        'views/sale_views.xml',
        'views/setting_views.xml',
    ],
}
