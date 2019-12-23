from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class ks_tx_account_invoice(models.Model):
    _inherit = 'account.invoice.line'

    ks_tx_local_currency_price = fields.Float(label='Local Price')
    ks_tx_exchange_rate = fields.Float(related='invoice_id.ks_tx_exchange_rate')
    currency_id = fields.Many2one('res.currency', related='invoice_id.currency_id')

    @api.onchange('ks_tx_exchange_rate', 'price_unit', 'quantity')
    def account_invoice_line(self):
        if self.invoice_id.ks_tx_exchange_rate:
            _logger.info('WATARU line ks_tx_exchange_rate %s currency_id %s',self.ks_tx_exchange_rate,self.currency_id)
            self.currency_id = self.invoice_id.currency_id
            self.ks_tx_exchange_rate = self.invoice_id.ks_tx_exchange_rate
            self.ks_tx_local_currency_price = self.quantity * self.price_unit * self.invoice_id.ks_tx_exchange_rate
