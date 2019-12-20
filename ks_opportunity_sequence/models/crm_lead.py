# -*- coding: utf-8 -*-

from odoo import fields, models, api

import json
import logging
import re
_logger = logging.getLogger(__name__)

##
# Clase que hereda crm lead.
##

class ks_opportunity_secuence(models.Model):
	_inherit = 'crm.lead'
  
	@api.model
	def default_get(self,vals):
		record = super(ks_opportunity_secuence, self).default_get(vals)
		record['name'] = "Pending"
		return record

	@api.model_create_multi
	def create(self, vals):
		record = super(ks_opportunity_secuence, self).create(vals)
		try:
			if record.name == 'Pending':
				oportunitynumber = self.env['ir.sequence'].next_by_code('crm.lead')
				_logger.debug('WATARU oportunitynumber %s ',oportunitynumber)
				fieldsToNumber = re.findall('{[a-zA-Z0-9_.]{0,}}',oportunitynumber)
				if fieldsToNumber:
					_logger.debug('WATARU fieldsToNumber %s ',fieldsToNumber)
					for fieldToNumber in fieldsToNumber:
						pyField = 'record.'+fieldToNumber.replace('{','').replace('}','')
						_logger.debug('WATARU fieldsToNumber %s ',pyField)
						oportunitynumber = oportunitynumber.replace(fieldToNumber,eval(pyField))
				record.name = oportunitynumber
		except:
			_logger.debug('WATARU no company crm.lead secuence')
		return record
