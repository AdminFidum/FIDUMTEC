# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging


_logger = logging.getLogger(__name__)


class ks_tx_res_currency(models.Model):
    _inherit = 'res.currency'

    def _get_rates(self, company, date):
        currency_rates = super(ks_tx_res_currency, self)._get_rates(company, date)
        ks_echangerate = self.env.context.get('value_ks_tx_exchange_rate')
        key = self.env.context.get('currency_id')
        _logger.info('WATARU ks_echangerate %s key %s',ks_echangerate,key)
        if ks_echangerate and key:

            currency_rates[key] = 1.0 / ks_echangerate

        return currency_rates