# -*- coding: utf-8 -*-
from odoo import api, models

class ParticularReport(models.AbstractModel):
    _name = 'Qweb_report.new_report'

    @api.model
    def get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('module.report_name')
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self,
        }
        return docargs