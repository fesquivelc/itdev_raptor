# coding=utf-8
from odoo import models, api, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def action_invoice_open(self):
        ret = super(AccountInvoice, self).action_invoice_open()
        for inv in self:
            partner_follower_id = inv.message_follower_ids.filtered(lambda f: f.partner_id == inv.partner_id)
            partner_follower_id.unlink()
        return ret
