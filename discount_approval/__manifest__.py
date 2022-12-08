{
    'name': 'Discount Approval',
    'version': '15.0.1.0',
    'category': 'approval',
    'summary': 'discount approval',
    'application': True,
    'depends':['sale_management',
               'contacts',
               'base',
               ],
    'data': [
        'views/sale_config_settings.xml',
        'views/sale_state_button.xml',
        'views/sale_state.xml',

    ],
    'sequence': -200
}