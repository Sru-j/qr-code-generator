import qrcode

data = "https://github.com/sru-j"

qr = qrcode.make(data)
qr.save("my_qr.png")

print("QR Code generated successfully!")
