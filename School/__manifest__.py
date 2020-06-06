# -*- coding: utf-8 -*-
{
    'name': "School",

    'summary': """
        Check""",

    'description': """
        Phục vụ cho mục đích chạy thử 1 số thay đổi, sau đó deploy trên Odoo
        
    """,

    'author': "PepeShop",
    'website': "https://edu-pnhhieu-uit.odoo.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images':[],
    'license':'AGPL-3',
    'installable':True,
    'Application':False,
    'auto_installation':False,
}
