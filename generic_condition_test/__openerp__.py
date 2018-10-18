{
    "name": "Generic Condition - Test",
    "version": "11.0.1.0.4",
    "author": "Center of Research & Development",
    "website": "https://crnd.pro",
    "license": "LGPL-3",
    "summary": "Generic Conditions - Tests (do not install manualy)",
    'category': 'Technical Settings',
    'depends': [
        'generic_condition',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/test_model_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
