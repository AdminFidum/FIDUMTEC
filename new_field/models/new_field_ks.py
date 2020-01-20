from openerp import models, fields, api
class NewField(models.Model):
    _inherit = 'crm.lead'
    team_id_users = fields.Many2one('crm.team/field_id', 'KS Team')

    