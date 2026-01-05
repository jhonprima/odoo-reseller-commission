import logging
from odoo.tests.common import TransactionCase

_logger = logging.getLogger(__name__) # 

class TestResellerCommission(TransactionCase):
    def setUp(self):
        super(TestResellerCommission, self).setUp()
        self.principal = self.env['res.partner'].create({
            'name': 'PT B (Principal)',
            'is_principal': True,
            'commission_rate': 10.0, # [cite: 58]
        })
        self.product = self.env['product.product'].create({
            'name': 'Bibit Sawit',
            'list_price': 100000.0,
        })

    def test_01_calculation(self):
        """Verifikasi perhitungan komisi PSAK 72"""
        order = self.env['sale.order'].create({
            'partner_id': self.principal.id,
            'is_agent_sale': True,
            'principal_id': self.principal.id,
            'order_line': [(0, 0, {
                'product_id': self.product.id,
                'product_uom_qty': 100, # Total Rp 10.000.000 [cite: 59]
                'price_unit': 100000.0,
                'tax_id': [(5, 0, 0)], # Tanpa Pajak
            })],
        })

        # MENAMPILKAN PERHITUNGAN DI TERMINAL
        _logger.info("==========================================")
        _logger.info("VERIFIKASI KOMISI AGEN (PT A)")
        _logger.info("Total Penjualan: Rp {:,.0f}".format(order.amount_untaxed))
        _logger.info("Rate Komisi: {}%".format(self.principal.commission_rate))
        _logger.info("Hasil Komisi: Rp {:,.0f}".format(order.commission_amount))
        _logger.info("==========================================")

        # Rumus: $10.000.000 \times 10\% = 1.000.000$ [cite: 61]
        self.assertEqual(order.commission_amount, 1000000.0)