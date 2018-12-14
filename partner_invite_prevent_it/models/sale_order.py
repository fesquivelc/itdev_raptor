# coding=utf-8
from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        res = super(SaleOrder, self.with_context(mail_create_nosubscribe=True)).create(vals)
        return res

    @api.multi
    def action_confirm(self):
        res = super(SaleOrder, self.with_context(mail_create_nosubscribe=True)).action_confirm()
        for sale in self:
            partner_follower_id = sale.message_follower_ids.filtered(lambda f: f.partner_id == sale.partner_id)
            partner_follower_id.unlink()
        return res
