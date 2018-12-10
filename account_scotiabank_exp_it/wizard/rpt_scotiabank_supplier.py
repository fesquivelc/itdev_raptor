# coding=utf-8
import logging
import math

from odoo import models, fields, api, _
from odoo.exceptions import Warning

_logger = logging.getLogger(__name__)

PAYMENT_METHOD = [
    (' ', 'Interbancario'),
    ('0', 'Cheque de gerencia'),
    ('00', 'Cuenta corriente'),
    ('000', 'Cuenta de ahorro'),
]

CURRENCY_CODES = {
    'PEN': '0',
    'USD': '1'
}


class RptScotiabankSupplier(models.TransientModel):
    _name = 'rpt.scotiabank.supplier'

    def _get_lines(self):
        active_ids = self._context.get('active_ids', False)
        if active_ids:
            payment_ids = self.env['account.payment'].browse(active_ids)

            lines = [
                (0, False, {
                    'payment_id': p.id,
                    'partner_mail': p.partner_id.email,
                    'partner_id': p.partner_id.id,
                    'payment_amount': p.amount,
                    'payment_communication': p.communication,
                    'currency_id': p.currency_id.id,
                }) for p in payment_ids
            ]

            return lines
        return [(6, False, [])]

    supplier_line_ids = fields.Many2many('rpt.scotiabank.supplier.line', 'wizard_id',
                                         default=_get_lines)

    @api.multi
    def generate(self):
        self.ensure_one()
        for wizard in self:
            return {
                'type': 'ir.actions.act_url',
                'url': '/report/scotiabank/supplier-payment?report_id={}'.format(wizard.id),
                'target': 'new',
            }


class RptScotiabankSupplierLine(models.TransientModel):
    _name = 'rpt.scotiabank.supplier.line'

    wizard_id = fields.Many2one('rpt.scotiabank.supplier')
    payment_id = fields.Many2one('account.payment', u'Pago', required=True)
    payment_method = fields.Selection(PAYMENT_METHOD, u'Método de pago', default='000', required=True)
    partner_mail = fields.Char(u'E-mail', required=True)
    partner_bank_id = fields.Many2one('res.partner.bank', u'Cuenta bancaria', required=True)
    partner_id = fields.Many2one('res.partner', u'Proveedor', related='payment_id.partner_id', readonly=True)
    payment_amount = fields.Monetary(u'Monto', related='payment_id.amount', readonly=True)
    payment_communication = fields.Char(u'Referencia de pago', readonly=True, related='payment_id.communication')
    currency_id = fields.Many2one('res.currency', related='payment_id.currency_id', readonly=True)

    @api.multi
    def get_file_rows(self):
        lines = []
        template = '{}{:<60}{:<60}{:<18}{}{:0>13}{:0>2}{}{:>14}{:>20}'

        for line in self:
            r, d = self.float_splitter(line.payment_amount)
            acc_ext = ''
            acc_int = ''
            acc_number = line.partner_bank_id.sanitized_acc_number
            currency_code = CURRENCY_CODES[line.currency_id.name]
            if line.payment_method == '00':
                if currency_code == '0':
                    acc_currency = '01'
                else:
                    acc_currency = '07'
                acc_int = '{}{:0>12}'.format(acc_currency, acc_number)
            elif line.payment_method == '000':
                if currency_code == '0':
                    acc_currency = '14'
                else:
                    acc_currency = '13'
                acc_int = '{}{:0>12}'.format(acc_currency, acc_number)
            elif line.payment_method == ' ':
                acc_ext = '{:0>20}'.format(line.partner_bank_id.sanitized_acc_number)

            lines.append(
                template.format(
                    line.partner_id.nro_documento,
                    line.partner_id.name.upper(),
                    line.partner_mail.upper(),
                    line.payment_communication.upper(),
                    currency_code,
                    r,
                    d,
                    line.payment_method,
                    acc_int,
                    acc_ext
                )
            )
        return '\n'.join(lines)

    def float_splitter(self, number):
        d, r = math.modf(number)
        return int(r), int(round(d, 2) * 100)
