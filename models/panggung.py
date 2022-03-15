from odoo import fields, models, api


class Panggung(models.Model):
    _name = 'toko.panggung'
    _description = 'Panggung'

    name = fields.Char(
        string='Name')
    pelaminan = fields.Char(
        string='Tipe Pelaminan',
        required=False)
    accesories = fields.Char(
        string='Accesories Pelaminan',
        required=False)
    harga = fields.Integer(
        string='Harga Sewa',
        required=False)
    bunga = fields.Selection(
        string='Tipe Bunga',
        required=False,
        selection=[('bunga mati', 'Bunga Mati'), ('bunga hidup', 'Bunga Hidup')])
