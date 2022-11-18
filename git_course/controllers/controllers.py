# -*- coding: utf-8 -*-
# from odoo import http


# class GitCourse(http.Controller):
#     @http.route('/git_course/git_course', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/git_course/git_course/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('git_course.listing', {
#             'root': '/git_course/git_course',
#             'objects': http.request.env['git_course.git_course'].search([]),
#         })

#     @http.route('/git_course/git_course/objects/<model("git_course.git_course"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('git_course.object', {
#             'object': obj
#         })
