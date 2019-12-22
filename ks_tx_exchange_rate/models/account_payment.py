# -*- coding: utf-8 -*-

from odoo import fields, models, api

import json
import logging
import re
_logger = logging.getLogger(__name__)

##
# Clase que hereda crm lead.
##
class ks_tx_payment_exchange_rate(models.Model):
	_inherit = 'account.payment'
	ks_tx_exchange_rate = fields.Float(string='Exchange Rate',digits=(12,2))
	local_currency_price = fields.Monetary(readonly=1)

	@api.onchange('amount','payment_date','currency_id') # if these fields are changed, call method
	def ks_tx_change_date_currency(self):
		ks_company = self.env['res.company']._company_default_get('account.payment')
		ks_company_currency = ks_company.currency_id
		ks_from_currency = ks_company_currency
		ks_to_currency = self.currency_id
		ks_er_date = self.payment_date or fields.Date.today()
		ks_tx = self.env['account.invoice'].ks_tx_inv_exchange_rate.ks_tx_get_rates(self,ks_er_date,ks_company,ks_from_currency,ks_to_currency)
		self['ks_tx_exchange_rate'] = ks_tx['ks_er']
		self.local_currency_price = self.ks_tx_exchange_rate * self.amount