# -*- coding: utf-8 -*-
{
    'name': "School",

    'summary': """
        Quản lý thông tin học sinh, quản lý thông tin giáo viên, quản lý thông tin lớp học
        """,

    'description': """
        Chức năng chính là quản lí thông tin giáo viên, học sinh, lớp học, môn học và bảng điểm. Thể hiện được mô hình quản lí học sinh tiểu học dựa trên đơn vị lớp học. Quản lí các môn học theo từng lớp, và theo từng học kỳ. Cuối mỗi học kỳ sẽ tổng hợp điểm trung bình từ các điểm quá trình, điểm thi giữa kỳ, điểm thi cuối kỳ để đánh giá năng lực học tập của học sinh. 
    Chức năng xếp thời khoá biểu cho học sinh theo từng lớp """,

    'author': "PepeShop",
    'website': "https://edu-pnhhieu-uit.odoo.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/score_record_view.xml',
        'views/class_schedule.xml',
        'views/student_view.xml',
        'views/teacher_views.xml',
        'views/class_view.xml',
        'views/subject_view.xml',
        # 'views/grade_view.xml',
        # 'views/templates.xml',
        #Last Update at 14/07/2020
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'Application': False,
    'auto_installation': False,
}
