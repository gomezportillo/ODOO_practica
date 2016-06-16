# -*- coding: utf-8 -*-
from openerp.osv import fields, orm
from types import *

""" CLASE CURSO """

class curso(orm.Model):

	_name = "res.curso"
	_description = "Lista de cursos"
	_columns = {
		'nombre' : fields.char('Nombre', size=50, required=True),
		'edicion': fields.many2many('product.template', 'curso_edicion','nombre','numero_edicion', 'is_course', domain=[('is_course','=',True)]),
		'precio': fields.char('Precio'),
	}
