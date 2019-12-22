# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging


_logger = logging.getLogger(__name__)


class ks_tx_res_currency(models.Model):
    _inherit = 'res.currency'

    def _get_rates(self, company, date):
        currency_rates = super(ks_tx_res_currency, self)._get_rates(company, date)

        if self.env.context.get('value_ks_tx_exchange_rate') and \
           self.env.context.get('currency_id'):

            key = self.env.context.get('currency_id')
            currency_rates[key] = 1.0 / self.env.context.get('value_ks_tx_exchange_rate')

        return currency_rates