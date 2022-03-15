from odoo import fields, models, api


class Panggung(models.Model):
    _name = 'toko.panggung'
    _description = 'Panggung'

    name = fields.Char(
        string='Nama Panggung',
        required=True,)
    pelaminan = fields.Many2one(
        comodel_name='toko.pelaminan',
        string='Tipe Pelaminan',
        domain="[('harga', '>', '0')]",
        required=False)
    accesories = fields.Char(
        string='Accesories Pelaminan',
        required=False)
    bunga = fields.Selection(
        string='Tipe Bunga',
        required=False,
        selection=[('bunga mati', 'Bunga Mati'), ('bunga hidup', 'Bunga Hidup')])
    harga = fields.Char(
        compute='_compute_harga',
        string='Harga Sewa',
        required=False)

    @api.depends('pelaminan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.pelaminan.harga



