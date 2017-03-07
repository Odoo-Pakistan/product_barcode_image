# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2017- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Barcode Image for Product',
    'category': 'Product',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'depends': ['product'],
    'description': """
Barcode Image for Product
=========================
* Adds a new field to product that contains an EAN13 image of the product's barcode
* Barcode dimensions are configurable by adding 'product_barcode_image.barcode_width' and 'product_barcode_image.barcode_height' to system parameters
* Mainly intended as a helper field for Aeroo Reports where resizing features of EAN13s are limited. With QWeb reports you can just use the /report/barcode/ controller of Odoo core.

""",
    'data': [
    ],
}
