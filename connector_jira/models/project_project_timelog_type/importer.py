from odoo.addons.connector.components.mapper import mapping
from odoo.addons.component.core import Component


class ProjectProjectTimelogTypeImporter(Component):
    _name = "jira.project.project.timelog.type.importer"
    _inherit = "jira.importer"
    _apply_on = ["jira.project.project.timelog.type"]


class ProjectProjectTimelogTypeMapper(Component):
    _name = "jira.project.project.timelog.type.mapper"
    _inherit = "jira.import.mapper"
    _apply_on = ["jira.project.project.timelog.type"]

    @mapping
    def name(self, record):
        name = record["value"]
        # try to link with existing one first
        project_project_timelog_type = self.env["jira.project.project.timelog.type"].search(
                [("name", "=", name)], limit=1)
        if project_project_timelog_type:
            return {"odoo_id": project_project_timelog_type.id}
        else:
            return {"name": name}

    @mapping
    def backend_id(self, record):
        return {'backend_id': self.backend_record.id}
