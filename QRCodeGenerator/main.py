import qrcode

class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str, bg: str):
        user_input: str = input('Enter your text: ')

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print('QR code generated successfully!')
            print('File saved as:', file_name)
        except Exception as e:
            print('Error generating QR code: ', e)

def main():
    myqr = MyQR(size=30, padding=2)
    myqr.create_qr(file_name='sample.png',fg="red",bg="white")

if __name__ == '__main__':
    main()