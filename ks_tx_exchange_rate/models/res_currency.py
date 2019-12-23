# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging


_logger = logging.getLogger(__name__)


class ks_tx_res_currency(models.Model):
    _inherit = 'res.currency'

    def _get_rates(self, company, date):
        currency_rates = super(ks_tx_res_currency, self)._get_rates(company, date)
        ks_echangerate = self.env.context.get('ks_tx_exchange_rate')
        currency_key = self.env.context.get('currency_id')
        _logger.info('WATARU currency ks_echangerate %s currency_key %s context %s',ks_echangerate,currency_key,self.env.context)
        if ks_echangerate and currency_key:
            currency_rates[currency_key] = 1.0 / ks_echangerate

        return currency_rates