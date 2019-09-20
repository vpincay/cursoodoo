# -*- coding: utf-8 -*-
{
    'name': "saldoapp",

    'summary': "Aplicación de saldo ",

    'description': " Aplicación de saldo - curso odoo",

    'author': "Victor Pincay V.",
    'website': "http://www.next-pro.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}