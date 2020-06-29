from odoo import models, fields, api


class ScoreScore(models.Model):
    _name = 'score.score'
    name = fields.Char(compute='get_full_name_record', string='Phiếu điểm', store=True)
    student_id = fields.Many2one('student.student', string='Học sinh', required=True)
    subject_id = fields.Many2one('subject.subject', string='Môn học', required=True)
    score_process = fields.Float(string='Điểm quá trình', required=True)
    score_midterm = fields.Float(string='Điểm giữa kỳ', required=True)
    score_final = fields.Float(string='Điểm cuối kỳ', required=True)
    score_average = fields.Float(compute='get_average_score', string='Điểm trung bình', store=True)
    school_term = fields.Selection([('1', 'Học kỳ 1'), ('2', 'Học kỳ 2')], string='Học kỳ', required=True)
    # Năm học
    date_from = fields.Char(string='Bắt đầu', required=True)
    date_to = fields.Char(string='Kết thúc', required=True)
#Gán tên cho từng phiếu điểm theo cấu trúc [tên học sinh, môn học, học kỳ, năm bắt đầu]
    @api.depends("student_id", "subject_id", "school_term", "date_from")
    def get_full_name_record(self):
        student_id = self.student_id.name or ""
        subject_id = self.subject_id.name or ""
        school_term = self.school_term or ""
        date_from = self.date_from or ""
        name = student_id + ',' + '' + subject_id + ',' + '' + school_term + ',' + '' + date_from
        self.name = name
#Tính giá trị điểm trung bình của từng môn học
    @api.depends("score_process", "score_midterm", "score_final")
    def get_average_score(self):
        score_process = float(self.score_process)
        score_midterm = float(self.score_midterm)
        score_final = float(self.score_final)
        score_average = (float(score_process) + float(score_midterm)*2 + float(score_final)*3)/6
        self.score_average = score_average
        # (score_average) = (float(score_process) + float(score_midterm) * 2 + float(score_final) * 3) / 5
        # return  score_average
