# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging


_logger = logging.getLogger(__name__)


class ResCurrency(models.Model):
    _inherit = 'res.currency'

    def _get_rates(self, company, date):
        currency_rates = super(ResCurrency, self)._get_rates(company, date)

        _logger.info('WATARU currency rate %s currency_id %s',self.env.context.get('value_ks_tx_exchange_rate'),self.env.context.get('currency_id'))

        if self.env.context.get('value_ks_tx_exchange_rate') and \
           self.env.context.get('currency_id'):

            key = self.env.context.get('currency_id')
            currency_rates[key] = 1.0 / self.env.context.get('value_ks_tx_exchange_rate')

        return currency_rates