from odoo import models, fields, api


class GradeGrade(models.Model):
    _name = 'grade.grade'
    name = fields.Char(string='Khối lớp')
