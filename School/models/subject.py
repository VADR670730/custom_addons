from odoo import models, fields, api


class SubjectSubject(models.Model):
    _name = 'subject.subject'
    name = fields.Char(string='Tên môn học', required=True)
