# -*- coding: utf-8 -*-

from odoo import fields, models, api

import json
import logging
import re
_logger = logging.getLogger(__name__)

##
# Clase que hereda sales order.
##

class ks_co_create_saleorder(models.Model):
    _inherit = "sale.order"

    @api.model_create_multi
    def create(self, vals):
        record = super(ks_co_create_saleorder, self).create(vals)
        _logger.debug('TESTKSCO01')
        return record
