import qrcode


out = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)


#out.add_data('Name:KAMALESH R\nAge:21\nBlood group: B+ve\nFather\'s Name:Ravi K\nNumber:9080218139')
out.add_data('onnu illa delete pannu ga')
out.make(fit=True)
qr_out = out.make_image(fill_color='black',back_color='white')
qr_out.save('learning/qr_code.png')
