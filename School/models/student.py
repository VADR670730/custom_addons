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
    #Quản lý thông tin cá nhân
    name = fields.Char(string='Họ và tên', required=True)
    student_dob = fields.Date(string='Ngày sinh',required=True)
    gender = fields.Selection([('male', 'Nam'), ('female', 'Nữ')],
                              string='Giới tính',required=True)
    avatar = fields.Binary(string="Ảnh đại diện")
    place_of_birth = fields.Char(string='Nơi sinh',required=True )
    # Vùng quản lý địa chỉ
    address = fields.Char(string='Địa chỉ', store=True,required=True)
    # Vùng qUản lý lớp học
    grade_id= fields.Many2one('grade.grade', string="Khối")
    class_id = fields.Many2one('class.class',string='Lớp')
    # Vùng quản lý thông tin cha
    name_father = fields.Char(string='Họ và tên cha')
    phone_father = fields.Char(string='Số điện thoại cha')
    work_place_father = fields.Char(string='Nơi làm việc của cha')
    # Vùng quản lý thông tin của mẹ
    name_mother = fields.Char(string='Họ và tên mẹ')
    phone_mother = fields.Char(string='Số điện thoại mẹ')
    work_place_mother = fields.Char(string='Nơi làm việc của mẹ')
    # #link giữa lựa chọn khối lớp với các lớp được hiển thị
    @api.onchange('grade_id')
    def set_values_to_state(self):
        if self.grade_id:
            ids = self.env['class.class'].search([('grade_id', '=', self.grade_id.id)])
            return {
                'domain': {'class_id': [('id', 'in', ids.ids)], }
            }