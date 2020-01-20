from openerp import models, fields, api
class NewField(models.Model):
    _inherit = 'crm.team'
    new_user_id = fields.Many2one('crm.team', 'Responsible')