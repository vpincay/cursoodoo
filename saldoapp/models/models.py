# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Movimiento(models.Model):
    _name = 'sa.movimiento' # Nombre de la base de batos
    _description = 'Movimiento' # Nombre del modelo en Odoo
    
    name = fields.Char("Concepto")
    monto = fields.Char("Monto")
#    calorias2 = fields.Integer("Calorias2")
# class calorias(models.Model):
#     _name = 'calorias.calorias'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
