# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Movimiento(models.Model):
    _name = 'sa.movimiento' # Nombre de la base de batos
    _description = 'Movimiento' # Nombre del modelo en Odoo
    
    name = fields.Char(string="Concepto", size=15, index=True)
    #monto = fields.Char("Monto")
    monto_total = fields.Float(string="Monto")
    tipo = fields.Selection(string="Tipo", selection=[("I","Ingreso"),("E","Egreso")])
    fecha = fields.Date(string="Fecha operación")
    moneda = fields.Selection(string="Moneda", selection=[("PEN","Soles"), ("USD","Dolares")])
