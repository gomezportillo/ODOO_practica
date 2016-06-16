# -*- coding: utf-8 -*-
from openerp.osv import fields, orm


from types import *

class edicion(orm.Model):
	_inherit = 'product.template'
	_description = 'Ediciones de cada curso'
	_columns = {
		'escurso': fields.boolean('¿Es un curso?'),
		'profesores': fields.many2one('hr.employee', 'Profesores'),
		'fechainicio': fields.date('Fecha de Inicio: '),
		'fechafin': fields.date('Fecha de Fin: '),
		'tipocurso': fields.selection([('odoo', 'ODOO'),('dynamics','DYNAMICS'),('sap','SAP')], 'Tipo de Curso'),
		'inscripciones': fields.many2many('sale.inscripcion','tablainscripcionedicion','name','edicion','Inscripciones de Ediciones:'),
	}
	# Restricción única al campo NIF
	_sql_constraints = [
		('fechainicio_fechafin_check', 'CHECK(fechafin > fechainicio)', "La fecha de inicio debe ser menor que la fecha de fin"),
		('name_tipocurso_unique', 'UNIQUE(name,tipocurso)', "No pueden existir dos tuplas <Nombre-TipoCurso> iguales"),
	]
edicion()
