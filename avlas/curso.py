# -*- coding: utf-8 -*-
from openerp.osv import fields, orm

from types import *

class curso(orm.Model):
	_name = 'res.curso'
	_description = 'Cursos ofertados por ACADEMIA FORTE'
	_columns = {
		'nombre': fields.char('Nombre', size=20, required=True),
		'precio': fields.float('Precio del Curso', required=True),
		'ediciones': fields.many2many('product.template', 'tablacursoedicion','nombre','numeroedicion', 'escurso', domain = [('escurso', '=', True)]),
	}
	
