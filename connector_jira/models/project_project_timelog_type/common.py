from odoo import fields, models


class JiraProjectTimelogType(models.Model):
    _name = 'jira.project.project.timelog.type'
    _inherit = 'jira.binding'
    _inherits = {'project.project.timelog.type': 'odoo_id'}
    _description = 'Jira Task SME Type'

    odoo_id = fields.Many2one(comodel_name='project.project.timelog.type',
            string='Task SME Type',
            required=True,
            index=True,
            ondelete='restrict')
