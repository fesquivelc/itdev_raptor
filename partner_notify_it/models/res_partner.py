# coding=utf-8

from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        ret = super(ResPartner, self).create(vals)
        if ret and ret.id:
            self.add_default_followers(ret)
        return ret

    def add_default_followers(self, partner):
        parameters = self.env.ref('stock_parameters_it.partner_parameters_values')
        partner_ids = parameters.default_partner_followers.mapped('partner_id').ids
        if partner_ids:
            ctx = {'res_model': 'res.partner', 'res_id': partner.id}
            vals = {
                'res_model': 'res.partner',
                'res_id': partner.id,
                'partner_ids': [(6, False, partner_ids)],
                'message': "<p>Se ha creado un nuevo contacto: <strong>{}</strong> y se le ha agregado como seguidor.</p>".format(
                    partner.display_name),
                'send_mail': True

            }
            invite = self.env['mail.wizard.invite'].with_context(ctx).create(vals)
            invite.add_followers()

