# pip install qrcode[pil]

import qrcode

# Data jo QR me encode karna hai
data = input("Enter text or URL to generate QR Code: ")

# QR Code object create karo
qr = qrcode.QRCode(
    version=1,  # size control (1 = small)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Image generate karo
img = qr.make_image(fill_color="black", back_color="white")

# Save file
img.save("qrcode.png")

print("✅ QR Code successfully generated and saved as qrcode.png")
