from openerp import models, fields, api
class NewField(models.Model):
    _inherit = 'crm.team'
    team_id_users = fields.Many2one('crm.team', 'Responsible')

    @api.multi
    def search_(self):
        domain = [('team_id.team_type', '=', 'sales'),'|',('members_ids','=',true),('members_ids.team_type','=','sales')]
        records = self.search(domain)
        return records