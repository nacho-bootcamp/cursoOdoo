# fiel para definir los campos y
# models que es el orm para abstraer la capa de actualizacion,eliminacion
#  con respecto a la base de datos
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Movimiento(models.Model):
    _name = "sa.movimiento"
    _description = "Movimiento"
    _inherit = "mail.thread"
    # hilo de mensaje aparece la notificacion si modificamos

    name = fields.Char("Nombre", required=True)
    # el primero se almacena en la base de datos y el segundo se muestar en la vistas
    type_move = fields.Selection(
        selection=[("ingreso", "Ingreso"), ("gasto", "Gasto")],
        string="Tipo",
        default="ingreso",
        required=True,
        track_visibility="onchange",
    )
    date = fields.Datetime("Fecha", track_visibility="onchange")
    amount = fields.Float("Monto", track_visibility="onchange")
    receipt_image = fields.Binary("Foto del Recibo")
    notas = fields.Html("Notas")
    currency_id = fields.Many2one("res.currency", default=1)
    # primer parametro nombre del modelo que vamos a relacionar
    user_id = fields.Many2one(
        "res.users", string="Usuario", default=lambda self: self.env.user.id
    )
    category_id = fields.Many2one("sa.category", string="Categoria")
    # primer parametro la tabla con la que se va a relacionar + nombre de como se llamara la nueva tabla
    # + nombre de la columna
    tags_ids = fields.Many2many("sa.tag", "sa_mov_sa_tag_rel", "move_id", "tag_id")
    email = fields.Char(related="user_id.email", string="Correo Electronico")

    # Restriccion de pago
    @api.constrains("amount")
    def _check_amount(self):
        if not (self.amount >= 0 and self.amount <= 100000):
            raise ValidationError("El monto debe estar entre 0 a 100000")

    @api.onchange("type_move")
    def onchange_type_move(self):
        if self.type_move == "ingreso":
            self.name = "Ingreso: "
            self.amount = 50
        elif self.type_move == "gasto":
            self.name = "Gasto: "
            self.amount = 100


class Category(models.Model):
    _name = "sa.category"
    _description = "Categoria"

    name = fields.Char("Nombre")

    def ver_movimientos(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Moviemientos de categoria ",
            "res_model": "sa.movimiento",
            "views": [[False, "tree"]],
            "target": "new",
            "domain": [["category_id", "=", self.id]],
        }


class Tag(models.Model):
    _name = "sa.tag"
    _description = "Tag"

    name = fields.Char("Nombre")


class ResUsers(models.Model):
    # para campos que ya existen , a esto se llama extender un camppo
    _inherit = "res.users"

    movimiento_ids = fields.One2many("sa.movimiento", "user_id")
    total_ingresos = fields.Float("Total de Ingresos", compute="_compute_movimientos")
    total_gastos = fields.Float("Total de Gastos", compute="_compute_movimientos")

    @api.depends("movimiento_ids")
    def _compute_movimientos(self):
        for record in self:
            record.total_ingresos = sum(
                record.movimiento_ids.filtered(
                    lambda r: r.type_move == "ingreso"
                ).mapped("amount")
            )
            record.total_gastos = sum(
                record.movimiento_ids.filtered(lambda r: r.type_move == "gasto").mapped(
                    "amount"
                )
            )

    def mi_cuenta(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Mi cuenta",
            "res_model": "res.users",
            "res_id": self.env.user.id,
            "target": "self",
            "view_mode": "form",
            # "views": [(False, "form")],
        }
