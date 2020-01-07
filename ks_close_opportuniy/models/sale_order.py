# -*- coding: utf-8 -*-

from odoo import fields, models, api

import json
import logging
import re
_logger = logging.getLogger(__name__)

##
# Clase que hereda crm lead.
##

class ks_co_create_saleorder(models.Model):
	_inherit = "sale.order"

    @api.model
    def create(self, vals):
        record =  super(ks_co_create_saleorder, self).create(vals)
        _logger.info("kstest1 ks_co")
        return record
# 	ks_so_exchange_rate_field = fields.Float(string='KS Exchange Rate',digits=(12,2))
# 	ks_so_amount_total = fields.Float(string="KS Dolar Amount",digits=(12,2))
# 	ks_default_currency_id = fields.Many2one('res.currency',string="KS Moneda por defecto")

# 	@api.model
# 	def default_get(self,vals):
# 		record = super(ks_tx_so_exchange_rate, self).default_get(vals)
# 		record['ks_default_currency_id'] = 2 #set 2 for USD
# 		return record

# 	@api.onchange('currency_id','date_order') # if these fields are changed, call method
# 	def ks_tx_exchange_rate(self):
# 		ks_company = self.env['res.company']._company_default_get('sale.order')
# 		ks_company_currency = ks_company.currency_id
# 		ks_from_currency = self.currency_id
# 		ks_to_currency = self.ks_default_currency_id
# 		ks_er_date = self.date_order or fields.Date.today()
# 		ks_currency_rates = (ks_from_currency + ks_to_currency)._get_rates(ks_company, ks_er_date)
# 		ks_to_currency_rate = ks_currency_rates.get(ks_to_currency.id) or 1
# 		ks_from_currency_rate = ks_currency_rates.get(ks_from_currency.id) or 1
# 		ks_er = 1
# 		if ks_to_currency_rate != ks_from_currency_rate and ks_company_currency!=ks_from_currency:
# 			ks_er = ks_from_currency_rate/ks_to_currency_rate
# 		else:
# 			if ks_company_currency==ks_from_currency:
# 				ks_er = 1/ks_to_currency_rate

#   	_logger.info('WATARU ks_er %s ',ks_er)
# 		self['ks_so_exchange_rate_field'] = ks_er

# 	@api.onchange('amount_total','ks_so_exchange_rate_field') # if these fields are changed, call method
# 	def ks_tx_set_planned_revenue(self):
# 		ks_pr_val = self.amount_total or 0
# 		ks_exchange_rate_field = self.ks_so_exchange_rate_field or 1
# 		_logger.info('WATARU ks_pr_val*ks_exchange_rate_field %s ',ks_pr_val*ks_exchange_rate_field)
# 		self['ks_so_amount_total'] = ks_pr_val/ks_exchange_rate_field
