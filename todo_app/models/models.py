# -*- coding: utf-8 -*-
# desde aqui se crea una tabla
# models tiene una capa de abstraccion para poder conectarme con la base de datos
from odoo import models, fields


class ToDo(models.Model):
    _name = "todo.app"
    _description = "Lista de Tareas"
    # Es como reescribir , toma el nombre representativo al lado del titulo
    _rec_name = "description"
    # name es el nombre del atributo
    name = fields.Char(string="Nombre")
    state = fields.Char(string="Estado")
    description = fields.Char(string="Descripcion")
    # title = fields.Char(string="Titulo")
    # price = fields.Float(string="Precio")
