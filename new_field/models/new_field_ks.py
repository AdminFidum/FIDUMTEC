from openerp import models, fields, api
class NewField(models.Model):
    _inherit = 'res.users'
    user_id = fields.Many2one('res.users', 'Responsible')