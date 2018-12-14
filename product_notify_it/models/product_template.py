# coding=utf-8
from odoo import fields, api, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        ret = super(ProductTemplate, self).create(vals)
        if ret and ret.id:
            self.add_default_followers(ret)

        return ret

    def add_default_followers(self, product):
        parameters = self.env.ref('stock_parameters_it.stock_parameters_values')
        partner_ids = parameters.default_product_followers.mapped('partner_id').ids
        if partner_ids:
            ctx = {'res_model': 'product.template', 'res_id': product.id}
            vals = {
                'res_model': 'product.template',
                'res_id': product.id,
                'partner_ids': [(6, False, partner_ids)],
                'message': "<p>Se ha creado un nuevo producto de nombre: <strong>{}</strong> y se le ha agregado como seguidor.</p>".format(
                    product.name),
                'send_mail': True

            }
            invite = self.env['mail.wizard.invite'].with_context(ctx).create(vals)
            invite.add_followers()
