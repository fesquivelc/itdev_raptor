# -*- coding: utf-8 -*-
{
    'name': u"Parámetros de configuración",

    'summary': u"""
        Permite definir múltiples ubicaciones de destino por línea de compra""",

    'description': """
        Long description of module's purpose
    """,

    'author': "IT Grupo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_parameters.xml',
        'views/partner_parameters.xml',
        'data/sale_parameters.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}