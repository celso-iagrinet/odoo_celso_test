# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'summary': """ Academy app to manage Training """,
    
    'description': """
    Academy Module to Manage Training:
    - Courses
    - Sessions
    - Attendees
    """,
    'author': 'Celso',
    'website': 'https://www.odoo.com',
    'licence': 'LGPL-3',
    
    'category': 'Training',
    'version': '0.1',
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
}