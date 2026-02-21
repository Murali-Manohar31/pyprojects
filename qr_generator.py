import qrcode

url=input("enter the URL: ").strip()
file_path="C:\\Users\\Victus\\OneDrive\\Desktop\\PYTHON\\qrcode.png"

qr=qrcode.QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(file_path)

print("QR generated succcesfully")
