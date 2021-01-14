from odoo import models, fields

class Courses(models.Model):
    # _name = 'academy.courses'
    # _inherit = 'mail.thread'

    # to extend a model in-place, it's inherited without giving a new _name
    # product.template already uses discussion system
    # creating courses as published by default so they can be seen without having to log in
    _inherit = 'product.template'

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")