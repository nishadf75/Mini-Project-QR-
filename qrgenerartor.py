import qrcode
# url as input
input_URL = "https://www.spotify.com/"
#  Defining size of the code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)
# Making QR code
qr.add_data(input_URL)
qr.make(fit=True)
# saving the QR as a image
img = qr.make_image(fill_color="black", back_color="white")
img.save("url_qrcode.png")
# printing list of Qr's
print(qr.data_list)
