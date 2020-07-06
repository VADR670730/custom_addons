from datetime import datetime
from odoo import models, fields, api


class ClassClass(models.Model):
    _name = 'class.class'
    name = fields.Char(compute='get_full_name_of_class', string='Lớp học', store=True)
    # Các khối lớp
    grade_id = fields.Selection([('1', 'Khối 1'), ('2', 'Khối 2'), ('3', 'Khối 3'), ('4', 'Khối 4'),
                                 ('5', 'Khối 5')], string='Khối lớp')
    # Hậu tố các lớp
    subname = fields.Selection([('A1', 'Lớp A1'), ('A2', 'Lớp A2'), ('A3', 'Lớp A3'), ('A4', 'Lớp A4')
                                   , ('A5', 'Lớp A5')], string='Lớp')
    # Niên khoá
    date_from = fields.Char(string="Bắt đầu")
    date_to = fields.Char(string='Kết thúc ')
    # Giáo viên chủ nhiệm
    teacher_on_duty = fields.Many2one('teacher.teacher', string='Giáo viên chủ nhiệm')
    # Sĩ số
    class_size = fields.Integer(compute='_compute_class_size', string='Sĩ số', strore=True)

    @api.depends("grade_id", "subname")
    def get_full_name_of_class(self):
        grade_id = self.grade_id or ""
        subname = self.subname or ""
        name = grade_id + subname
        self.name = name
    #Tự động cập nhật sĩ số lớp khi có học sinh tham gia vào lớp học
    @api.model
    def _compute_class_size(self):
        for Class in self:
            operator = '='
            Class.class_size = self.env['student.student'].search_count([('class_id', operator, Class.id)])
