# -*- coding: utf-8 -*-
from openerp import fields, models, api
from reportlab.graphics.barcode import createBarcodeDrawing
import base64


class ProductProduct(models.Model):

    _inherit = 'product.product'

    @api.one
    def _get_barcode_image(self):
        if self.ean13:
            # Get dimensions from system parameters
            width = self.env['ir.config_parameter'].get_param('product_barcode_image.barcode_width') or 450
            height = self.env['ir.config_parameter'].get_param('product_barcode_image.barcode_height') or 200

            barcode = createBarcodeDrawing('EAN13', value=str(self.ean13), format='png', width=float(width), height=float(height))
            bc_data = barcode.asString('png')
            self.barcode_image = base64.encodestring(bc_data)

            barcode_jpg = createBarcodeDrawing('EAN13', value=str(self.ean13), format='jpg', width=float(width), height=float(height))
            bc_data_jpg = barcode_jpg.asString('jpg')
            self.barcode_image = base64.encodestring(bc_data_jpg)

            barcode_gif = createBarcodeDrawing('EAN13', value=str(self.ean13), format='gif', width=float(width), height=float(height))
            bc_data_gif = barcode_gif.asString('gif')
            self.barcode_image = base64.encodestring(bc_data_gif)

    barcode_image = fields.Binary(compute=_get_barcode_image, string='Barcode Image', store=False)
    barcode_image_jpg = fields.Binary(compute=_get_barcode_image, string='Barcode Image (JPG)', store=False)
    barcode_image_gif = fields.Binary(compute=_get_barcode_image, string='Barcode Image (GIF)', store=False)
