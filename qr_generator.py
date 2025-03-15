#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 10:20:59 2025

@author: harshjoshi
"""

import qrcode
from qrcode.constants import ERROR_CORRECT_L 
#AIM=to generate qr code for yhe customer.

data="https://www.ybifoundation.org"
qr=qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=5
    
    )

qr.add_data(data)
qr.make(fit=True)

image=qr.make_image(fill="black",back_color="white")
image.show()
image.save("qrcode.png")

print("QR code is ready.")