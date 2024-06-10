# -*- coding: utf-8 -*-
{
    'name': "odoo_ranking_customer",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'product', 'sale', 'account','purchase'],

    'assets': {
        'web.assets_backend': [
            # 'odoo_new/static/src/js/my_library.js',

        ],

        'web.assets_frontend': [

        ]
    },

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/rank_program_view.xml',
        'views/customer_loyalty_program_view.xml',
        'views/customer_loyalty_card_view.xml',
        'views/customer_loyalty_rule_view.xml',
        'views/sale_order.xml',
        'views/website_sales_template.xml',
        'views/customer_loyalty_reward.xml'
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
