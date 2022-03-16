from odoo import fields, models, api


class Order(models.Model):
    _name = 'toko.order'
    _description = 'Order'

    name = fields.Char(
        string='Kode Order',
        required=True)
    order_detail_panggung_ids = fields.One2many(
        comodel_name='toko.order_detail_panggung',
        inverse_name='name',
        string='Order Detail Panggung',
        required=False)
    order_detail_kursi_tamu_ids = fields.One2many(
        comodel_name='toko.order_detail_kursi_tamu',
        inverse_name='name',
        string='Order Detail Panggung',
        required=False)
    total = fields.Integer(
        compute='_compute_total',
        string='Total Harga',
        store=True,
        required=False)
    tanggal_pesan = fields.Datetime(
        string='Tanggal Pemesanan',
        default=fields.Datetime.now(),
        required=False)
    tanggal_pengiriman = fields.Date(
        string='Tanggal Pengiriman',
        default=fields.Date.today(),
        required=False)

    @api.depends('order_detail_panggung_ids', 'order_detail_kursi_tamu_ids')
    def _compute_total(self):
        for record in self:
            search_harga_panggung = sum(
                self.env['toko.order_detail_panggung'].search([('name', '=', record.id)]).mapped('harga'))
            search_harga_kursi_tamu = sum(
                self.env['toko.order_detail_kursi_tamu'].search([('name', '=', record.id)]).mapped('harga'))
            record.total = search_harga_panggung + search_harga_kursi_tamu


class OrderDetailPanggung(models.Model):
    _name = 'toko.order_detail_panggung'
    _description = 'Order Detail Panggung'

    name = fields.Many2one(
        comodel_name='toko.order',
        string='Order',
        required=False)
    panggung_id = fields.Many2one(
        comodel_name='toko.panggung',
        string='Panggung',
        required=False)
    harga = fields.Integer(
        compute='_compute_harga',
        string='Harga',
        required=False)
    qty = fields.Integer(
        string='Quantity',
        required=False)
    harga_satuan = fields.Integer(
        compute='_compute_harga_satuan',
        string='Harga Satuan',
        required=False)

    @api.depends('panggung_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.panggung_id.harga

    @api.depends('qty', 'harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty

    @api.model
    def create(self, values):
        # Add code here
        record = super(OrderDetailPanggung, self).create(values)
        if record.qty:
            self.env['toko.panggung'].search([('id', '=', record.panggung_id.id)]).write(
                {'stok': record.panggung_id.stok - record.qty})
            return record


class OrderDetailKursiTamu(models.Model):
    _name = 'toko.order_detail_kursi_tamu'
    _description = 'Order Detail Kursi Tamu'

    name = fields.Many2one(
        comodel_name='toko.order',
        string='Order',
        required=False)
    kursi_tamu_id = fields.Many2one(
        comodel_name='toko.kursi_tamu',
        string='Kursi Tamu',
        required=False)
    harga = fields.Integer(
        compute='_compute_harga',
        string='Harga',
        required=False)
    qty = fields.Integer(
        string='Quantity',
        required=False)
    harga_satuan = fields.Integer(
        compute='_compute_harga_satuan',
        string='Harga Satuan',
        required=False)

    @api.depends('kursi_tamu_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.kursi_tamu_id.harga

    @api.depends('qty', 'harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty

    @api.model
    def create(self, values):
        # Add code here
        record = super(OrderDetailKursiTamu, self).create(values)
        if record.qty:
            self.env['toko.kursi_tamu'].search([('id', '=', record.kursi_tamu_id.id)]).write(
                {'stok': record.kursi_tamu_id.stok - record.qty})
            return record
