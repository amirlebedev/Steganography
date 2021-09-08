import cv2 as cv


def encode_grayscale(img_gray, txt_binary, img_name):
    width = img_gray.shape[0]
    height = img_gray.shape[1]
    print("width:", str(width), "height:", str(height))

    #  encode
    print("Encoding...")
    x = 0
    y = 0
    pixel_counter = 0
    while y < height:
        while x < width:
            if pixel_counter >= len(txt_binary):
                img_gray.itemset((x, y), img_gray.item(x, y) & ~1)
            elif txt_binary[pixel_counter] == '0':
                img_gray.itemset((x, y), img_gray.item(x, y) & ~1)
            elif txt_binary[pixel_counter] == '1':
                img_gray.itemset((x, y), img_gray.item(x, y) | 1)
            pixel_counter += 1
            x += 1
        x = 0
        y += 1

    print("Encoding complete. \nWriting file...")
    write_path = ".\\OUTPUT\\"+img_name[:-4]+"_encoded.png"
    cv.imwrite(write_path, img_gray)


def decode_grayscale(img_gray, img_name):
    width = img_gray.shape[0]
    height = img_gray.shape[1]
    print("width:", str(width), "height:", str(height))

    #  decode
    x = 0
    y = 0
    pixel_counter = 0
    binary_decode = ""
    while y < height:
        while x < width:
            binary_decode += str(img_gray.item(x, y) & 1)
            pixel_counter += 1
            x += 1
        x = 0
        y += 1

    return binary_decode