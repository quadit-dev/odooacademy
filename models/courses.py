from odoo import models, fields


class OdooacademyCourse(models.Model):

    _name = 'odooacademy.course'
    _description = 'Odoo Academy Course'

    name = fields.Char(string='Title')
    responsible = fields.Char('Responsible')
