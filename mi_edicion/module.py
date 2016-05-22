# -*- coding: utf-8 -*-
from openerp.osv import fields, orm

class edicion(orm.Model):

	#	_name = "res.edicion"
	_inherit = "product.template"
	_description = "Ediciones de cursos"
	_columns = {
		'is_course':fields.boolean("¿Es una edicion de curso?"),
		#'curso' : fields.many2one('res.curso', 'Curso') #para saber de qué curso es, no?
		'profesor' : fields.many2one('hr.employee', "Profesor"),
		#'fecha_inicio' : fields.date('Fecha inicio'), #cuando vaya el resto probamos esto
		#'fecha_fin' : fields.date('Fecha fin')
	}

edicion()
