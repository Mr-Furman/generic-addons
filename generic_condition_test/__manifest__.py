{
    "name": "Generic Condition - Test",
    "version": "16.0.1.12.0",
    "author": "Center of Research and Development",
    "website": "https://crnd.pro",
    "license": "LGPL-3",
    "summary": "Generic Conditions - Tests (do not install manualy)",
    'category': 'Hidden',
    'depends': [
        'generic_condition',
        'calendar',
        'survey',
        'crm',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/test_model_demo.xml',
        'demo/res_partner.xml',
        'demo/calendar_event.xml',
        'demo/crm_lead.xml',
        'demo/survey_user_input.xml',
        'demo/generic_condition.xml',
        'demo/generic_condition_find_1.xml',
        'demo/generic_condition_find_2.xml',
        'demo/generic_condition_find_3.xml',
        'demo/generic_condition_find_4.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
