# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class test_module(models.Model):
#     _name = 'test_module.test_module'
#     _description = 'test_module.test_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value)
from odoo import models, fields


class StudentStudent(models.Model):
    _name = 'student.student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    photo = fields.Binary(string='Image')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                             string='Gender')
    student_dob = fields.Date(string="Date of Birth")
    student_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
        ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group'
    )
    nationality = fields.Many2one('res.country', string='Nationality')
