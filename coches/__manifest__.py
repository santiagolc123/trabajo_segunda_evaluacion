# -*- coding: utf-8 -*-
{
    'name': "Concesionario",
    'summary': "Venta de coches",
    'description': """Este módulo se centra en la comercialización de automóviles""",
    'author': "Santiago Lorenzo",
    'website': "http://www.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/ventas.xml',
        'views/stock.xml',
        'views/clientes.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}