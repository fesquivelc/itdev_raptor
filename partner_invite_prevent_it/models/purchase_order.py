# coding=utf-8
from odoo import api, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        # res = super(PurchaseOrder, self.with_context(mail_create_nosubscribe=True)).create(vals)
        res = super(PurchaseOrder, self).create(vals)
        return res

    @api.multi
    def button_confirm(self):
        # res = super(PurchaseOrder, self.with_context(mail_create_nosubscribe=True)).button_confirm()
        res = super(PurchaseOrder, self).button_confirm()
        for order in self:
            partner_follower_id = order.message_follower_ids.filtered(lambda f: f.partner_id == order.partner_id)
            partner_follower_id.unlink()
        return res
