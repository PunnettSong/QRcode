def qrcode():
    # Data to be encoded
    data = 'QR Code using make() function'
    
    # Encoding data using make() function
    img = qrcode.make(data)
    print(img)
    
    # Saving as an image file
    img.save('MyQRCode1.jpg')
    
if __name__ == '__main__':
    qrcode()