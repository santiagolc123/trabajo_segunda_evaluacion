# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class Ventas (models.Model):
    _name = "ventas.coches"
    _description = "Ventas"
    _order = "marca asc"

    marca = fields.Char("Marca", required=True)
    modelo = fields.Char("Modelo", required=True)
    precio = fields.Float("Precio", required = True)
    state = fields.Selection(
        [('disponible','Disponible'),
        ('reparación','Reparación'),
        ('vendido','Vendido'),
        ('no disponible','No Disponible')],
        'Estado', default="vendido")
    infoextra = fields.Char("Información extra")
    fecha_venta = fields.Date('Fecha venta')
    fecha_now = fields.Date('Fecha registro', default=lambda *a:datetime.now().strftime('%Y-%m-%d'), readonly=True)
    precio_iva = fields.Float(string='Total', compute='_total' )
    iva = fields.Float(string='IVA', default=1.21)
    comprador = fields.Many2one("res.partner", String="Compradores")

    @api.one
    @api.depends('precio', 'iva')
    def _total(self):
        self.precio_iva = self.precio * self.iva

    @api.constrains('fecha_venta','fecha_now')
    def check_fecha(self):
         for coche in self:
             if coche.fecha_venta > coche.fecha_now:
                 raise models.ValidationError('La fecha de compra debe ser inferior a la fecha actual')
    #PONER CAMPO CALCULADO DE IVA

class Stock (models.Model):
    _name = "stock.coches"
    _description = "Coches disponibles para venta directa"

    marca = fields.Char("Marca", required=True)
    modelo = fields.Char("Modelo", required=True)
    precio = fields.Float("Precio", required = True)
    color = fields.Char("Color", required=True)
    extras = fields.Char("Extras")
    CV = fields.Integer("CV", required=True)
    cilindrada = fields.Float("cc", required=True)
    año = fields.Integer("año",required=True)
    state = fields.Selection(
        [('gasolina','Gasolina'),
        ('diésel','Diésel'),
        ('eléctrico','Eléctrico'),
        ('otro','Otro')],
        'Combustible', default="gasolina")
    img_coche = fields.Binary ("Foto coche")

class Clientes (models.Model):
    _name = "clientes.coches"
    _description = "Compradores de coches"
    _inherits = {"res.partner": "dni"}

    dni = fields.Many2one("res.partner", ondelete="cascade", string="ficha cliente")
    nombre = fields.Char("Nombre")
    domicilio = fields.Text("Domicilio")
    teléfono = fields.Integer("Teléfono")
    edad = fields.Integer("Edad")
    descuentomarca = fields.Boolean("Descuento")

