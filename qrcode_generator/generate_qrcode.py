import qrcode

code = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,
)

code.add_data("https://scintillagh.herokuapp.com/")
code.make(fit=True)

code_image = code.make_image(fill_color="white", back_color="black")
code_image.save("./qrcode_generator/scintilla_qrcode.png")
