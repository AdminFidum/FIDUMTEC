from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class ks_tx_account_invoice(models.Model):
    _inherit = 'account.invoice.line'

    ks_tx_local_currency_price = fields.Float()
    ks_tx_exchange_rate = fields.Float(related='invoice_id.ks_tx_exchange_rate')
    currency_id = fields.Many2one('res.currency', related='invoice_id.currency_id')

    @api.onchange('ks_tx_exchange_rate', 'price_unit', 'quantity')
    def account_invoice_line(self):
        if self.invoice_id.ks_tx_inv_exchange_rate:
            self.local_currency_price = self.quantity * self.price_unit * self.invoice_id.ks_tx_exchange_rate
