# -*- coding: utf-8 -*-merisevbphp
from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)
import os

class TestOdoo(http.Controller):

	@http.route('/smileodoo', auth='public')
	def hello_world(self, **kwargs):
		# return ("<h1 class='text-primary text-center'>hello man this is a test page </h1>")
		# variable = "Mon Premier conntroller"
		return request.render('test_odoo11.test_view')
	    
	@http.route('/log', auth='public')
	def demo(self, **kwargs):
		# path   = self.get_txt_path
		# logFile = open('/home/innocent/Documents/Innocent/Odoo/addons_odoo/test_odoo11/views/my.xml', 'r')
		logFile = open('/var/log/odoo/odoo-server.log', 'r')
		content = logFile.read()
		_logger.critical(logFile)
		_logger.critical(logFile)
		_logger.critical(content)
		# with open('odoolog.log', 'r') as content_file:
		# 	content = content_file.read()
		# 	print(content)
		# 	_logger.critical(content)
			# return ("<h1 class='text-primary text-center'>this is my first controller </h1>")
		# return request.render('test_odoo11.test1_view')
		test = "my test page htm"				
		return request.render('test_odoo11.test1_view',{'test' : content})

	# def get_txt_path(self):
 #    	directory_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
 #    	return os.path.join(directory_path, 'filename.txt')
