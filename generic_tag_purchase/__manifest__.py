{
    'name': "Generic Tag (Purchase)",

    'summary': """
        Generic tag integration with purchase addon
    """,

    'author': "Center of Research and Development",
    'website': "https://crnd.pro",

    'category': 'Generic Tags',
    'version': '14.0.1.5.0',

    "depends": [
        "generic_tag",
        "purchase",
    ],

    "data": [
        'data/generic_tag_model.xml',
        'views/purchase_order.xml',
        'views/purchase_order_line.xml',
        'views/generic_tag_purchase.xml'
    ],
    'images': ['static/description/banner.png'],
    "installable": True,
    "auto_install": True,
    'license': 'LGPL-3',
}
