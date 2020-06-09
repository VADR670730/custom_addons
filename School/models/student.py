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
from odoo import models, fields, api


class StudentStudent(models.Model):
    # name sẽ tạo 1 bảng trong db dưới dạng student_student
    _name = 'student.student'
    # Với các cột là các fields được định nghĩa trong class StudentStudent
    name = fields.Char(string='Họ và tên', required=True)
    student_dob = fields.Date(string='Ngày sinh')
    gender = fields.Selection([('male', 'Nam'), ('female', 'Nữ')],
                              string='Giới tính')
    image = fields.Binary(string='Ảnh')
    # Vùng quản lý địa chỉ
    street = fields.Char(string='Tên đường', required=True)
    city = fields.Many2one('res.country.state', string='Thành phố',store=True)
    Nationality = fields.Many2one('res.country', string='Quốc gia')

    # grade = fields.Many2one
    # Class = fields.Many2one
    # link giữa lựa chọn quốc gia với các tỉnh thành tương ứng
    @api.onchange('Nationality')
    def set_values_to_state(self):
        if self.Nationality:
            ids = self.env['res.country.state'].search([('country_id', '=', self.Nationality.id)])
            return {
                'domain' : {'city' : [('id', 'in', ids.ids)], }
            }
