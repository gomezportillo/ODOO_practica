# -*- coding: utf-8 -*-
from openerp.osv import fields, orm

class alumno(orm.Model):

  _inherit = "res.partner"
  _description = "Módulo para la gestión de alumnos"
  _columns = {
    "is_alumno": fields.boolean("Es alumno"),
	"ediciones": fields.many2many('product.template', 'cursoedicion','nombre', 'name', 'Cursos del alumno', domain=[('is_course','=',True)])
  }

alumno()
