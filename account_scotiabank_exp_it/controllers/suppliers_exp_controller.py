# -*- coding: utf-8 -*-
import StringIO
from zipfile import ZipFile

from odoo import http
from odoo.http import request


class SuppliersExpController(http.Controller):
    @http.route('/report/scotiabank/supplier-payment', auth='user')
    def get_report(self, report_id, **kw):
        report_id = int(report_id)
        report = request.env['rpt.scotiabank.supplier'].browse(report_id)

        zip_buffer = StringIO.StringIO()
        zip_archive = ZipFile(zip_buffer, mode="w")

        file_content = report.supplier_line_ids.get_file_rows().encode('utf-8')
        # file_buffer.write(file_content)
        zip_archive.writestr('PROVEEDORES.txt', file_content)
        zip_archive.close()

        return request.make_response(zip_buffer.getvalue(),
                                     [('Content-Type', 'application/octet-stream'),
                                      ('Content-Disposition', 'attachment; filename=PROVEEDORES.zip;')])
