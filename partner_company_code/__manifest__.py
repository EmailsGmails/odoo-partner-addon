# -*- coding: utf-8 -*-
{
    'name': "partner_company_code",

    'summary': """
        Adds a new Char field "company_code" for the "res.partner" data model.""",

    'description': """
        Adds the field 'Company Code' for contacts which allows the same company code to be used
        for up to 3 different partners.
    """,

    'author': "Emil",
    'website': "https://github.com/EmailsGmails",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_views.xml'
    ],

    'demo': [
        'demo/demo.xml',
    ],
}