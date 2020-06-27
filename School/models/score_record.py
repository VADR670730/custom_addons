from odoo import models, fields, api


class ScoreScore(models.Model):
    _name = 'score.score'
    student_id = fields.Many2one('student.student', string='Học sinh',required= True)
    subject_id = fields.Many2one('subject.subject', string='Môn học',required= True)
    score_process = fields.Char(string='Điểm quá trình',required= True)
    score_midterm = fields.Char(string='Điểm giữa kỳ',required= True)
    score_final = fields.Char(string='Điểm cuối kỳ',required= True)
    score_average = fields.Char(string='Điểm trung bình',required= True)
    school_term = fields.Char(string='Học kỳ',required= True)
    # Năm học
    date_from = fields.Char(string='Bắt đầu',required= True)
    date_to = fields.Char(string='Kết thúc',required= True)
