# fiel para definir los campos y
# models que es el orm para abstraer la capa de actualizacion,eliminacion
#  con respecto a la base de datos
from odoo import fields, models


class Movimiento(models.Model):
    _name = "sa.movimiento"
    _description = "Movimiento"

    name = fields.Char("Nombre")
    # el primero se almacena en la base de datos y el segundo se muestar en la vistas
    type_move = fields.Selection(selection=[("ingreso", "Ingreso"), ("gasto", "Gasto")])
    date = fields.Datetime("Fecha")
    amount = fields.Float("Monto")
    receipt_image = fields.Binary("Foto del Recibo")
    # primer parametro nombre del modelo que vamos a relacionar
    user_id = fields.Many2one("res.users", string="Usuario")
    category_id = fields.Many2one("sa.category", string="Categoria")
    # primer parametro la tabla con la que se va a relacionar + nombre de como se llamara la nueva tabla
    # + nombre de la columna
    tags_ids = fields.Many2many("sa.tag", "sa_mov_sa_tag_rel", "move_id", "tag_id")


class Category(models.Model):
    _name = "sa.category"
    _description = "Categoria"

    name = fields.Char("Nombre")


class Tag(models.Model):
    _name = "sa.tag"
    _description = "Tag"

    name = fields.Char("Nombre")


class ResUsers(models.Model):
    # para campos que ya existen , a esto se llama extender un camppo
    _inherit = "res.users"

    movimiento_ids = fields.One2many("sa.movimiento", "user_id")
