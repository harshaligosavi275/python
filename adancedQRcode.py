import qrcode as qc
from PIL import Image
# here we need to from pil library which will responsible to format the qr image
qr = qc.QRCode(version=1,error_correction=qc.constants.ERROR_CORRECT_H,box_size = 10,border=10)
# advanced QR code
qr.add_data("https://www.youtube.com/watch?v=YDH7f9dTXAs")
qr.make(fit = True)
img = qr.make_image(fill_color ="red",back_color="white")
img.save("F:/python/practice/myproject/advancedQrCode.png")

