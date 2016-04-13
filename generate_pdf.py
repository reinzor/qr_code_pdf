from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.graphics.barcode.qr import QrCodeWidget 
from reportlab.graphics import renderPDF

import os
import sys

if len(sys.argv) < 2 or "--help" in sys.argv:
    print "Usage ./generate_pdf.py [filename, e.g. codes.txt] [url_prefix, e.g. http://eindspel.baasvanhorstaandemaas.nl?code=]"
    sys.exit(1)

filename = sys.argv[1] 

url_prefix = ""
if len(sys.argv) > 2:
    url_prefix = sys.argv[2] 

# Create page
p = canvas.Canvas("qr_codes.pdf")
p.setPageSize((90, 90))

with open(filename) as f:
    content = f.readlines()

for c in content:
    qr_data = (url_prefix + c).strip()

    # Generate qr code
    qrw = QrCodeWidget(qr_data) 

    d = Drawing(0,0) 
    d.add(qrw)

    renderPDF.draw(d, p, 0, 0)

    p.showPage()

    print "Drawing qr code for qr_data %s" % qr_data

p.save()