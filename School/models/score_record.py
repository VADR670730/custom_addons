from odoo import models, fields, api


class ScoreScore(models.Model):
    _name = 'score.score'
    student_id = fields.Many2one('student.student', string='id học sinh')
    subject_id = fields.Many2one('subject.subject', string='id môn học')
    score_process = fields.char(string='Điểm quá trình')
    score_midterm = fields.char(string='Điểm giữa kỳ')
    score_final = fields.char(string='Điểm cuối kỳ')
    score_average = fields.char (string='Điểm trung bình')
