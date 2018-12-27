# -*- coding: utf-8 -*-
{
    'name': "Restricción de documentos por usuarios",

    'summary': """
        Restringe documentos para que solo el usuario que los ha creado pueda visualizarlos""",

    'description': """
        Long description of module's purpose
    """,

    'author': "ITGroup",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'purchase', 'purchase_requisition'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/user_document_security.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
