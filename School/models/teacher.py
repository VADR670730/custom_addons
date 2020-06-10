from odoo import models, fields, api


class TeacherTeacher(models.Model):
    # name sẽ tạo ra 1 bảng trong db có dạng teacher_teacher
    _name = 'teacher.teacher'
    # Với các cột là các fields được đinh nghĩa
    name = fields.Char(string='Họ và tên', required=False)
    teacher_dob = fields.Date(string='Ngày sinh')
    gender = fields.Selection([('male', 'Nam'), ('female', 'Nữ')],
                              string='Giới tính')
    image = fields.Binary(string="Ảnh đại diện")
    # Vùng quản lý địa chỉ
    street = fields.Char(string='Tên đường', required=False)
    city = fields.Many2one('res.country.state', string='Thành phố', store=True)
    Nationality = fields.Many2one('res.country', string='Quốc gia')

    # Grade = fields.Many2one
    # Class = fields.Many2one
    # link giữa lựa chọn quốc gia với các tỉnh thành tương ứng
    @api.onchange('Nationality')
    def set_values_to_state(self):
        if self.Nationality:
            ids = self.env['res.country.state'].search([('country_id', '=', self.Nationality.id)])
            return {
                'domain': {'city': [('id', 'in', ids.ids)], }
            }
