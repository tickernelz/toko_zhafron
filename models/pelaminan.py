from odoo import fields, models, api


class Pelaminan(models.Model):
    _name = 'toko.pelaminan'
    _description = 'Pelaminan'

    name = fields.Char(
        string='Nama Pelaminan')
    deskripsi = fields.Char(
        string='Deskripsi Pelaminan',
        required=False)
    harga = fields.Integer(
        string='Harga Sewa',
        required=False)
