# -*- coding: utf-8 -*-
{
    'name': 'Odoo WooCommerce Connector',
    'version': '13.0.18',
    'license': 'OPL-1',
    'category': 'Sale',
    'summary': 'Odoo Woocommerce Connector helps you automate your vital business processes at Odoo by enabling '
               'bi-directional data exchange between WooCommerce & Odoo.',

    'author': 'Emipro Technologies Pvt. Ltd.',
    'website': 'https://www.emiprotechnologies.com/',
    'maintainer': 'Emipro Technologies Pvt. Ltd.',
    'depends': ['auto_invoice_workflow_ept', 'common_connector_library'],
    'data': ['security/group.xml',
             'security/ir.model.access.csv',
             'data/product_data.xml',
             'data/ir_sequence.xml',
             'data/ir_cron_data.xml',
             'data/import_order_status_ept.xml',
             'wizard/manual_queue_process_ept.xml',
             'wizard/cron_configuration_ept.xml',
             'views/instance_main_menu_view.xml',
             'views/product_image_ept.xml',
             'views/product_template_view.xml',
             'wizard/woo_process_import_export_view.xml',
             'views/web_templates.xml',
             'views/sale_workflow_config.xml',
             'wizard/res_config_view.xml',
             'views/product_data_queue_ept_view.xml',
             'views/product_data_queue_line_ept_view.xml',
             'views/product_variant_view.xml',
             'views/tags_ept.xml',
             'views/product_attribute_view.xml',
             'views/product_attribute_term_view.xml',
             'views/product_category_view.xml',
             'views/customer_data_queue_ept.xml',
             'views/customer_data_queue_line_ept.xml',
             'views/order_data_queue_ept.xml',
             'views/order_data_queue_line_ept.xml',
             'views/webhook_ept.xml',
             'views/common_log_book_ept.xml',
             'views/sale_order.xml',
             'views/stock_picking_view.xml',
             'views/res_partner.xml',
             'views/payment_gateway.xml',
             'views/account_move_view.xml',
             'views/instance_view.xml',
             'wizard/cancel_refund_order_wizard.xml',
             'views/coupons_ept.xml',
             'views/coupon_data_queue_ept.xml',
             'views/coupon_data_queue_line_ept.xml',
             'wizard/prepare_product_for_export.xml'
             ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'active': False,
    'images': ['static/description/woocommerce-odoo-cover.gif'],
    'live_test_url': 'https://www.emiprotechnologies.com/free-trial?app=woo-commerce-ept&version=13&edition=enterprise',
    'price': 379.00,
    'currency': 'EUR',
}
