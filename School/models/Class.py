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

    # Tên lớp đầy đủ

    @api.depends("grade_id", "subname")
    def get_full_name_of_class(self):
        grade_id = self.grade_id or ""
        subname= self.subname or ""
        name = grade_id+subname
        self.name= name
    # number_of_student = Sĩ số học sinh trong 1 lớp, sẽ cập nhật sau,
    # Ý tưởng: Nếu trong view học sinh chọn 1 lớp thì số lượng học sinh trong 1 lớp sẽ dc cập nhật
    teacher_on_duty = fields.Many2one('teacher.teacher',string='Giáo viên chủ nhiệm')
