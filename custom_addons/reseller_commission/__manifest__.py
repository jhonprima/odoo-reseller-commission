{
    'name': 'Reseller Commission Tracking',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Mencatat komisi agen sesuai PSAK 72', # [cite: 13, 35]
    'depends': ['sale_management', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/commission_report_views.xml'
    ],
    'installable': True,    
    'license': 'LGPL-3',
    
}