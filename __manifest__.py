{
    'name': "Generic Resource",

    'summary': """
        Provides the ability to create and categorize
        various resources that can be used in other Odoo modules.
    """,

    'author': "Center of Research and Development",
    'website': "https://crnd.pro",

    'category': 'Generic Resource',
    'version': '11.0.1.1.2',

    # any module necessary for this one to work correctly
    'depends': [
        'mail',
        'generic_m2o',
        'generic_mixin',
    ],

    # always loaded
    'data': [
        'data/ir_module_category.xml',

        'security/security.xml',
        'security/ir.model.access.csv',

        'data/generic_resource_type_data.xml',
        'data/ir_sequence_data.xml',

        'views/generic_resource_views.xml',
        'views/generic_resource_type_views.xml',
        'views/generic_resource_simple.xml',
        'views/generic_resource_simple_category.xml',
    ],
    'demo': [
        'demo/demo_resource.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'license': 'OPL-1',
}
