# -*- coding: utf-8 -*-
from openerp.osv import fields, orm
from types import *

""" CLASE CURSO """

class curso(orm.Model):

	_name = "res.curso"
	_description = "Lista de cursos"
	_columns = {
		'nombre' : fields.char('Nombre', size=64, required=True),
		'edicion': fields.many2many('product.template', 'cursoedicion','nombre', 'name', 'Ediciones', domain=[('is_course','=',True)])
	}

	_sql_constraints = [('nombre_unique', 'UNIQUE(nombre)', "No puede haber dos cursos con el mismo nombre")]

curso()
