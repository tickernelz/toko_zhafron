from odoo import fields, models, api


class OrderKursiTamu(models.Model):
    _name = 'toko.order_kursi_tamu'
    _description = 'Order Kursi Tamu'

    name = fields.Char(
        string='Kode Order')


class OrderDetailKursiTamu(models.Model):
    _name = 'toko.order_detail_kursi_tamu'
    _description = 'Order Detail Kursi Tamu'

    name = fields.Char(string='Nama')
