# -*- coding: utf-8 -*-
{
    'name': "Odoo 13 Rest Api (Json)",

    'summary': """
        This module to akses odoo via rest api with dynamic concept""",

    'description': """
        Module to integration odoo with other system, to using this module you bust be setting in odoo.conf
        
        1) Open odoo.conf
        2) Add 'dbfilter = dbname'.
        3) Restart odoo service.
        4) Test api with tools (ex: postman).

    Any questions?
    Want to test this module?
    Email me: nra.junior26@gmail.com 
    """,

    'author': "NRA",
    'website': "-",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'price': 100,
    'currency': 'EUR',
    'version': '13.0',
    'support': 'nra.junior26@gmail.com ',
    'images': ['images/login1.PNG'],

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/ir.model.access.csv',
        "data/ir_config_param.xml", 
        'views/res_users.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
