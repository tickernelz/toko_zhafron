from odoo import fields, models, api


class Pegawai(models.Model):
    _inherit = 'res.partner'

    is_pegawai = fields.Boolean(
        string='Pegawai',
        required=False)
    is_customer = fields.Boolean(
        string='Customer',
        required=False)
