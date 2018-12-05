# -*- coding: utf-8 -*-
{
    'name': u"Plantillas de proyecto",

    'summary': u"""
        Módulo que permite crear estructuras base para generación ágil de proyectos""",

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
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/project_template.xml',
        'views/project_view_simplified.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
