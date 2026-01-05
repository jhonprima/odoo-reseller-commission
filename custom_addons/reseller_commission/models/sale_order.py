from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_agent_sale = fields.Boolean(string="Is Agent Sale", default=False)
    principal_id = fields.Many2one('res.partner', string="Principal Partner", 
                                   domain=[('is_principal', '=', True)])
    
    # KUNCI PERBAIKAN: Ubah menjadi compute dan tambahkan store=True
    commission_rate = fields.Float(
        string="Commission Rate (%)", 
        compute="_compute_commission_rate", 
        store=True, 
        readonly=True
    )
    
    commission_amount = fields.Monetary(
        string="Commission Amount", 
        compute="_compute_commission_amount", 
        store=True
    )
    
    commission_status = fields.Selection([
        ('draft', 'Draft'),
        ('invoiced', 'Invoiced'),
    ], string="Commission Status", default='draft', copy=False)

    # Menarik rate dari PT B secara otomatis dan menguncinya ke database
    @api.depends('principal_id')
    def _compute_commission_rate(self):
        for order in self:
            if order.principal_id:
                order.commission_rate = order.principal_id.commission_rate
            else:
                order.commission_rate = 0.0

    # Menghitung nominal komisi berdasarkan rate yang sudah tersimpan
    @api.depends('amount_total', 'commission_rate')
    def _compute_commission_amount(self):
        for order in self:
            order.commission_amount = order.amount_total * (order.commission_rate / 100)

    def action_create_commission_invoice(self):
        """Fungsi tetap sama seperti sebelumnya"""
        for order in self:
            if not order.is_agent_sale or not order.principal_id:
                raise UserError(_("Pilih Principal Partner terlebih dahulu."))
            
            invoice_vals = {
                'move_type': 'out_invoice',
                'partner_id': order.principal_id.id,
                'invoice_date': fields.Date.today(),
                'ref': f'Commission for {order.name}',
                'invoice_line_ids': [(0, 0, {
                    'name': f'Jasa Keagenan / Komisi atas {order.name}',
                    'quantity': 1,
                    'price_unit': order.commission_amount,
                    'tax_ids': [], 
                })],
            }
            new_invoice = self.env['account.move'].create(invoice_vals)
            order.commission_status = 'invoiced'
            
            return {
                'name': _('Commission Invoice'),
                'view_mode': 'form',
                'res_model': 'account.move',
                'res_id': new_invoice.id,
                'type': 'ir.actions.act_window',
            }