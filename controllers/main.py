# -*- coding: utf-8 -*-merisevbphp
from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)
import os

class TestOdoo(http.Controller):

	@http.route('/smileodoo', auth='public')
	def hello_world(self, **kwargs):
		
		return request.render('test_odoo11.test_view')
	    
	@http.route('/log', auth='public')
	def demo(self, **kwargs):
		
		logFile = open('/var/log/odoo/odoo-server.log', 'r')
		content = logFile.read()
		_logger.critical(logFile)
		_logger.critical(logFile)
		_logger.critical(content)
		test = "my test page htm"	

		return request.render('test_odoo11.test1_view',{'test' : content})

	