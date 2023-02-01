# BASIC VERSION 
import qrcode as qr
img = qr.make(str(input("Enter the content to store in QR : ")))
img.save(str(input("Save as : ")) + ".png")
