from odoo import models, fields


class OdooacademySession(models.Model):

    _name = 'odooacademy.session'
    _description = 'Sessions'

    name = fields.Char(string='Name')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    seats = fields.Integer('Seats')
    instructor_id = fields.Many2one(
        comodel_name='res.users',
        string='Instructor')
