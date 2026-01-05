Odoo 18 – Reseller Commission Module (PSAK 72 Compliant)
1. Business Case & Background

Modul ini dikembangkan untuk menangani skema bisnis keagenan (reseller/agent) antara:

PT A → Agen / Perusahaan Pengguna Odoo

PT B → Principal / Vendor

Sesuai dengan standar akuntansi PSAK 72 – Pendapatan dari Kontrak dengan Pelanggan, PT A bertindak sebagai agen, bukan sebagai principal. PT A tidak menanggung risiko persediaan dan tidak mengendalikan barang yang dijual.

Oleh karena itu, pendapatan yang diakui oleh PT A hanya sebesar komisi jasa yang diperoleh dari PT B, bukan nilai bruto penjualan barang. Modul ini dirancang untuk memastikan proses bisnis dan pencatatan akuntansi patuh terhadap PSAK 72.

2. Fitur Utama
🔹 Konfigurasi Partner Agen

Penambahan flag Is Principal pada model res.partner

Pengaturan Commission Rate (%) per Principal

Fleksibel untuk multi-principal

🔹 Otomatisasi Sales Order

Identifikasi otomatis transaksi Reseller Agent Sale

Perhitungan nilai komisi secara otomatis menggunakan computed field

Komisi dihitung berdasarkan nilai Sales Order sesuai konfigurasi partner

🔹 Integrasi Akuntansi (Accounting Integration)

Pembuatan Commission Invoice otomatis ke Principal (PT B) setelah Sales Order dikonfirmasi

Faktur hanya mencatat nilai komisi jasa

Mendukung prinsip Net Revenue Recognition (PSAK 72)

🔹 Pelaporan (Reporting)

Dashboard analitik berbasis Pivot View

Visualisasi performa komisi menggunakan Graph View

Monitoring pendapatan komisi secara real-time

3. Spesifikasi Teknis
Komponen	Detail
Versi Odoo	18.0 (Community / Enterprise)
Bahasa	Python 3.10+
Standar Kode	PEP 8
Framework	Odoo ORM
Testing	Functional & Unit Test
4. Struktur Modul

Modul ini mengikuti arsitektur standar Odoo untuk kemudahan pengembangan dan pemeliharaan:

reseller_commission/
├── models/
│   ├── sale_order.py
│   └── res_partner.py
├── views/
│   ├── sale_order_view.xml
│   ├── res_partner_view.xml
│   └── commission_report_view.xml
├── security/
│   └── ir.model.access.csv
├── tests/
│   └── test_reseller_commission.py
├── __manifest__.py
└── README.md

5. Pengujian (Unit Test)

Modul ini memenuhi persyaratan mandatory testing dengan minimum code coverage 80%.

Menjalankan Unit Test via CLI
python odoo-bin -c odoo.conf -d odoo \
-u reseller_commission \
--test-enable \
--stop-after-init \
--log-level=test

6. Compliance Note (PSAK 72)

✔ Pendapatan diakui hanya sebesar komisi
✔ Tidak mencatat nilai penjualan bruto
✔ Sesuai model Agent vs Principal
✔ Aman untuk audit keuangan
