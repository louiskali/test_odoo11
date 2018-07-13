# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class TestOdoo(http.Controller):

    @http.route('/testodoo', auth='public')
    def hello_world(self, **kwargs):
        # return ("<h1 class='text-primary text-center'>hello man this is a test page </h1>")
        return request.render('test_odoo11.test_view')
