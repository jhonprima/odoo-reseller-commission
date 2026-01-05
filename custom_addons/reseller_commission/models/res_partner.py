from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_principal = fields.Boolean(string="Is Principal", default=False)
    commission_type = fields.Selection([
        ('percentage', 'Percentage'),
        ('fixed', 'Fixed Amount')
    ], string="Commission Type", default='percentage')
    commission_rate = fields.Float(string="Commission Rate")