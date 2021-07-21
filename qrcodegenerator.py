import qrcode

qrcode_data = "https://github.com/MattTMLive/qr-code-generator/" # Change this line to whatever you want

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(qrcode_data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('qrcode.png')
