rom odoo import models,api,fields
from odoo.exceptions import UserError, AccessError, ValidationError
import logging
_logger = logging.getLogger(__name__)


class Toto(models.Model):
	_name = 'totp'
	

	vignette = fields.Char('Vignette du Véhicule')