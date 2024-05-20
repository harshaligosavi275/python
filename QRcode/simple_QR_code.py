# Using Python to Generate a Basic QR Code
import qrcode as qc
# qrcode module you need to install-------pip install qrcode
# we want QR code in image format
img = qc.make("https://www.w3schools.com/python/")    #generate this link to qrcode
img.save("F:/python/practice/myproject/w3School_python_tutorial.png")

