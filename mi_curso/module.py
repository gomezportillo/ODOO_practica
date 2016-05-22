# -*- coding: utf-8 -*-
from openerp.osv import fields, orm


from types import *

""" CLASE CURSO """

class curso(orm.Model):

	_name = "res.curso"
	_description = "Lista de cursos"
	_columns = {
		'nombre' : fields.char('Nombre', size=50, required=True),
		'edicion'  : fields.many2many('product.product', "Ediciones"), #domain="[{'is_course','=','True'}]"), #, {'curso', '=', str(self.curso)}
		'profesor' : fields.many2many('hr.employee', "Profesor"), #todos los profesores que impartan clase a ediciones de ese curso?
	}

	#_sql_constraints = [
	#	('nombre_unique', 'unique(nombre)', 'El nombre debe ser único'),
	#]

curso()
