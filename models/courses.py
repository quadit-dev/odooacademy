from odoo import models, fields


class OdooacademyCourse(models.Model):

    _name = 'odooacademy.course'
    _description = 'Odoo Academy Course'

    name = fields.Char(string='Title')
    responsible = fields.Many2one(
        comodel_name='res.users',
        string='Responsible')
