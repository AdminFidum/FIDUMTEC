# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError

import json
import logging
import re
_logger = logging.getLogger(__name__)

##
# Clase que hereda account invoice.
##
class ks_tx_inv_exchange_rate(models.Model):
	_inherit = 'account.invoice'
	ks_tx_exchange_rate = fields.Float(help='Amount Echange Rate')

	@api.onchange('date_invoice','currency_id') # if these fields are changed, call method
	def ks_tx_change_date_currency(self):
		ks_company = self.env['res.company']._company_default_get('account.invoice')
		ks_company_currency = ks_company.currency_id
		ks_from_currency = ks_company_currency
		ks_to_currency = self.currency_id
		ks_er_date = self.date_invoice or fields.Date.today()
		ks_tx = ks_tx_inv_exchange_rate.ks_tx_get_rates(self,ks_er_date,ks_company,ks_from_currency,ks_to_currency)
		self['ks_tx_exchange_rate'] = ks_tx['ks_er']

		for data in self.invoice_line_ids:
			data.local_currency_price = data.quantity * data.price_unit * self.ks_tx_exchange_rate

	@api.onchange('ks_tx_exchange_rate') # if these fields are changed, call method
	def ks_tx_change_echangerate(self):
		for data in self.invoice_line_ids:
			_logger.info('WATARU set n lines ks_tx_exchange_rate %s ',self.ks_tx_exchange_rate)
			data.local_currency_price = data.quantity * data.price_unit * self.ks_tx_exchange_rate

	@api.model
	def ks_tx_get_rates(self,date,company,from_currency,to_currency):
		result = {'ks_er':1,'ks_er_normal':1}
		ks_currency_rates = (from_currency + to_currency)._get_rates(company, date)
		ks_to_currency_rate = ks_currency_rates.get(to_currency.id) or 1
		if to_currency != from_currency:
			result['ks_er'] = 1/ks_to_currency_rate
			result['ks_er_normal'] = ks_to_currency_rate
		return result