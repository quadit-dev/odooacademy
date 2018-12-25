from odoo import api, fields, models


class Partner(models.Model):

    _inherit = 'res.partner'

    instructor = fields.Boolean(
        default=False,
        string='Instructor')
    session_ids = fields.Many2many(
        comodel_name='odooacademy.session',
        readonly=False,
        string='Attended Sessions'
        )

    # @api.model
    # def create(self, values):
    #     pass

    # @api.multi
    # def write(self, values):
    #     pass
