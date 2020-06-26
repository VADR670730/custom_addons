from odoo import models, fields, api


class TeacherTeacher(models.Model):
    # name sẽ tạo ra 1 bảng trong db có dạng teacher_teacher
    _name = 'teacher.teacher'
    # Với các cột là các fields được đinh nghĩa
    # Vùng quản lý thông tin cơ bản giáo viên
    name = fields.Char(string='Họ và tên', required=False)
    teacher_dob = fields.Date(string='Ngày sinh')
    gender = fields.Selection([('male', 'Nam'), ('female', 'Nữ')],
                              string='Giới tính')
    avatar = fields.Binary(string='Ảnh đại diện')
    teacher_place_of_birth = fields.Char(string='Nơi sinh')
    teacher_nation = fields.Char(string='Dân tộc')
    # Vùng quản lý thông tin liên hệ
    address = fields.Char(string='Địa chỉ')
    teacher_phone = fields.Char(string='Số điện thoại')
    # Vùng quản lý thông tin chuyên môn
    teacher_level = fields.Char(string='Trình độ học vấn')
    teacher_graduate_year = fields.Char(string='Năm tốt nghiệp')
    teacher_certificate_language = fields.Char(string='Chứng chỉ ngoại ngữ')
    teacher_certificate_IT = fields.Char(string='Chứng chỉ tin học')
    teacher_years_of_teaching = fields.Char(string='Số năm tham gia giảng dạy')
    teacher_experience = fields.Char(string='Kinh nghiệm thực tế')
    teacher_title = fields.Char(string='Danh hiệu đạt được')
    teacher_reward = fields.Char(string='Giải thưởng đạt được')
    # Grade = fields.Many2one
    # Class = fields.Many2one
    # # link giữa lựa chọn quốc gia với các tỉnh thành tương ứng
    # @api.onchange('Nationality')
    # def set_values_to_state(self):
    #     if self.Nationality:
    #         ids = self.env['res.country.state'].search([('country_id', '=', self.Nationality.id)])
    #         return {
    #             'domain': {'city': [('id', 'in', ids.ids)], }
    #         }
