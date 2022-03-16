from odoo import fields, models, api


class Panggung(models.Model):
    _name = 'toko.panggung'
    _description = 'Panggung'

    name = fields.Char(
        string='Nama Panggung',
        required=True)
    pelaminan_id = fields.Many2one(
        comodel_name='toko.pelaminan',
        string='Tipe Pelaminan',
        required=True)
    kursi_pengantin_id = fields.Many2one(
        comodel_name='toko.kursi_pengantin',
        string='Kursi Pengantin',
        required=False)
    accesories = fields.Char(
        string='Accesories Pelaminan',
        required=True)
    bunga = fields.Selection(
        string='Tipe Bunga',
        required=True,
        selection=[('bunga mati', 'Bunga Mati'), ('bunga hidup', 'Bunga Hidup')])
    harga = fields.Integer(
        compute='_compute_harga',
        string='Harga Sewa',
        required=True)
    stok = fields.Integer(
        string='Stok Paket Panggung',
        required=False)
    des_pelaminan = fields.Char(
        compute='_compute_des_pelaminan',
        string='Deskripsi Pelaminan',
        required=False)
    des_kursi = fields.Char(
        compute='_compute_des_kursi',
        string='Deskripsi Kursi',
        required=False)
    order_detail_ids = fields.One2many(
        comodel_name='toko.order_detail',
        inverse_name='panggung_id',
        string='Order Detail',
        required=False)

    @api.depends('pelaminan_id', 'kursi_pengantin_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.pelaminan_id.harga + record.kursi_pengantin_id.harga

    @api.depends('pelaminan_id')
    def _compute_des_pelaminan(self):
        for record in self:
            record.des_pelaminan = record.pelaminan_id.deskripsi

    @api.depends('kursi_pengantin_id')
    def _compute_des_kursi(self):
        for record in self:
            record.des_kursi = record.kursi_pengantin_id.deskripsi
