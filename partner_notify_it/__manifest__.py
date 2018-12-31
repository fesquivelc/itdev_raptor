# -*- coding: utf-8 -*-
{
    'name': "Agregar seguidores contacto",

    'summary': """
        Permite que se agreguen seguidores por defecto al crear un contacto nuevo
        cliente/proveedor""",

    'description': """
        Long description of module's purpose
    """,

    'author': "ITGrupo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock_parameters_it'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}