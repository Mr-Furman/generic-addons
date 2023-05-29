{
    'name': "Generic Service",

    'summary': """
        Create and manage service catalog
    """,

    'author': "Center of Research and Development",
    'website': "https://crnd.pro",
    'category': 'Generic Service',
    'version': '12.0.1.21.0',

    # any module necessary for this one to work correctly
    'depends': [
        'mail',
        'generic_mixin',
    ],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/generic_service_views.xml',
        'views/generic_service_level_views.xml',
        'views/res_partner_views.xml',
        'views/res_config_settings_view.xml',
        'views/generic_service_group.xml',
        'data/generic_service_default.xml'
    ],
    'demo': [
        'demo/generic_service_demo.xml',
        'demo/generic_service_level_demo.xml',
        'demo/res_partner.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
