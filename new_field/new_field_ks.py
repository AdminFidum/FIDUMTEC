from openerp import models, fields, api
class NewField(models.Model):
    _inherit = 're.users'
    user_id = fields.Many2one('res.users', 'Responsible')