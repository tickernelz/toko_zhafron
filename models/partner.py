from odoo import fields, models, api


class Partner(models.Model):
    _name = 'toko.partner'
    _description = 'Partner'

    name = fields.Char(
        string='Nama')
    alamat = fields.Char(
        string='Alamat',
        required=False)
    no_telp = fields.Char(
        string='Telepon/HP',
        required=False)
