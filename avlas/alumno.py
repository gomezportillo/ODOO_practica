# -*- coding: utf-8 -*-
from openerp.osv import fields, orm

from types import *

class alumno(orm.Model):
	_inherit ='res.partner'
	_description = 'Indica si el cliente es un alumno o no'
	_columns = {
		'esalumno': fields.boolean('Alumno'),
		'inscripcionesalumno': fields.many2many('sale.inscripcion','tablainscripcionalumno','name','edicion','Inscripciones Realizadas:'),
	}
