# -*- coding: utf-8 -*-
from openerp.osv import fields, orm

class edicion(orm.Model):

  #  _name = "res.edicion"
  _inherit = "product.template"
  _description = "Ediciones de cursos"
  _columns = {
    "is_course": fields.boolean("Es edicion"),
    'profesor' : fields.many2one('hr.employee', "Profesor"),
    "cursos" : many2one("res.curso", "Curso"),
    'fecha_in' : fields.date('Fecha inicio'),
	'fecha_fin' : fields.date('Fecha fin'),
  }

edicion()
