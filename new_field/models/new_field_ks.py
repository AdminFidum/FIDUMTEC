from openerp import models, fields, api
class NewField(models.Model):
    _inherit = 'crm.lead'
    team_id_users = fields.Many2one('res.users', 'KS Saleperson')



    