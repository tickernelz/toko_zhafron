from odoo import fields, models, api


class Order(models.Model):
    _name = 'toko.order'
    _description = 'Order'

    name = fields.Char(
        string='Kode Order',
        required=True)
    order_detail_ids = fields.One2many(
        comodel_name='toko.order_detail',
        inverse_name='order_id',
        string='Order Detail',
        required=False)
    total = fields.Integer(
        string='Total Harga',
        store=True,
        required=False)

    @api.depends('order_detail_ids')
    def _compute_total(self):
        for record in self:
            search_harga = sum(self.env['toko.order_detail'].search([('order_id', '=', record.id)]).mapped('harga'))
            record.total = search_harga


class OrderDetail(models.Model):
    _name = 'toko.order_detail'
    _description = 'Order Detail'

    name = fields.Selection(
        string='Name',
        selection=[('panggung', 'Panggung'), ('kursi tamu', 'Kursi Tamu')])
    order_id = fields.Many2one(
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
        
