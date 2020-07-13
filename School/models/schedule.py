from odoo import models, fields, api


class ScheduleSchedule(models.Model):
    _name = 'schedule.schedule'
    name = fields.Char(compute='get_name_schedule', string='Thời khoá biểu', store=True)
    class_id = fields.Many2one('class.class', 'Lớp')
    subject_id = fields.Many2one('subject.subject', 'Môn học')
    subject_date_start = fields.Datetime(string='Bắt đầu', required=True)
    subject_date_stop = fields.Datetime(string='Kết thúc', required=True)


    # Gán tên cho từng thời khoá biểu theo cấu trúc [tên lớp, môn học, thời gian]
    @api.depends("class_id", "subject_id", "subject_date_start")
    def get_name_schedule(self):
        class_id = self.class_id.name or ""
        subject_id = self.subject_id.name or ""
        subject_date_start = self.subject_date_start or ""
        name = subject_id
        self.name = name