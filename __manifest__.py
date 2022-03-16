# -*- coding: utf-8 -*-
{
    'name': "Toko Zhafron",

    'summary': """
        Toko Zhafron""",

    'description': """
        Toko Zhafron
    """,

    'author': "Zhafron",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/panggung_views.xml',
        'views/pelaminan_views.xml',
        'views/kursi_pengantin_views.xml',
        'views/kursi_tamu_views.xml',
        'views/order_views.xml',
        'views/pegawai_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
