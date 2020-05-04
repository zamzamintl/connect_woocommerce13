from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def _woo_product_count(self):
        woo_product_obj = self.env['woo.product.product.ept']
        for product in self:
            woo_products = woo_product_obj.search([('product_id', '=', product.id)])
            product.woo_product_count = len(woo_products) if woo_products else 0

    woo_product_count = fields.Integer(string='# Sales Count', compute='_woo_product_count')
    image_url = fields.Char(size=600, string='Image URL')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def write(self, vals):
        """
        This method use to archive/unarchive woo product templates base on odoo product templates.
        :parameter: self, vals
        :return: res
        @author: Haresh Mori @Emipro Technologies Pvt. Ltd on date 09/12/2019.
        :Task id: 158502
        """
        if 'active' in vals.keys():
            woo_product_template_obj = self.env['woo.product.template.ept']
            for template in self:
                woo_templates = woo_product_template_obj.search(
                        [('product_tmpl_id', '=', template.id)])
                if vals.get('active'):
                    woo_templates = woo_product_template_obj.search(
                            [('product_tmpl_id', '=', template.id),('active','=',False)])
                woo_templates and woo_templates.write({'active':vals.get('active')})
        res = super(ProductTemplate, self).write(vals)
        return res

    def _woo_template_count(self):
        woo_product_template_obj = self.env['woo.product.template.ept']
        for template in self:
            woo_templates = woo_product_template_obj.search([('product_tmpl_id', '=', template.id)])
            template.woo_template_count = len(woo_templates) if woo_templates else 0

    woo_template_count = fields.Integer(string='# Sales', compute='_woo_template_count')