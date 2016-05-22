# -*- coding: utf-8 -*-
from openerp.osv import fields, orm

class edicion(orm.Model):

	#	_name = "res.edicion"
	_inherit = "product.template"
	_description = "Ediciones de cursos"
	_columns = {
		'is_course':fields.boolean("¿Es una edicion de curso?"),
		#'curso' : fields.one2one('res.curso', 'Curso')
		'profesores' : fields.many2one('hr.employee', "Profesor"),
		'fecha' : fields.date('Fecha')
	}

edicion()

#'edicion'  : fields.many2one('product.product', "Edicion", domain="[{'sale_ok','=','1'}]"),
