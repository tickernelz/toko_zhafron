from odoo import fields, models, api


class KursiTamu(models.Model):
    _name = 'toko.kursi_tamu'
    _description = 'Kursi Tamu'

    name = fields.Char(
        string='Nama Kursi Tamu',
        required=True)
    tipe = fields.Selection(
        string='Tipe Kursi',
        selection=[('plastik', 'Plastik'), ('stainless', 'Stainless')],
        required=False)
    stok = fields.Integer(
        string='Stok Kursi',
        required=False)
    harga = fields.Integer(
        string='Harga Sewa per Unit',
        required=False)
