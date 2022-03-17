from odoo import fields, models, api


class Pengembalian(models.Model):
    _name = 'toko.pengembalian'
    _description = 'Pengembalian Barang Sewa'

    name = fields.Many2one(
        comodel_name='toko.order',
        string='Order')
    tanggal_pengembalian = fields.Date(
        string='Tanggal Pengembalian',
        default=fields.Date.today(),
        required=False)
    penyewa = fields.Char(
        compute='_compute_penyewa',
        string='Nama Penyewa',
        required=False)
    tagihan = fields.Integer(
        compute='_compute_tagihan',
        string='Tagihan',
        required=False)

    @api.depends('name')
    def _compute_penyewa(self):
        for record in self:
            record.penyewa = self.env['toko.order'].search([('id', '=', record.name.id)]).mapped('pemesan').name

    @api.depends('name')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.name.total

    @api.model
    def create(self, values):
        # Add code here
        record = super(Pengembalian, self).create(values)
        if record.tanggal_pengembalian:
            self.env['toko.order'].search([('id', '=', record.name.id)]).write(
                {'sudah_kembali': True})
            self.env['toko.akunting'].create([{'kredit': record.tagihan, 'name': record.penyewa}])
            return record

    def unlink(self):
        for zhafron in self:
            self.env['toko.order'].search([('id', '=', zhafron.name.id)]).write({'sudah_kembali': False})
        record = super(Pengembalian, self).unlink()
