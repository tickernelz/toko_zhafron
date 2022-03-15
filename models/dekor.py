from odoo import fields, models, api


class Dekor(models.Model):
    _name = 'toko.dekor'
    _description = 'Dekorasi'

    name = fields.Char(
        string='Nama Dekorasi',
        required=False)
    harga = fields.Integer(
        string='Harga',
        required=False)
    deskripsi = fields.Char(
        string='Deskripsi',
        required=False)
