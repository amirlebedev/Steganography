import cv2 as cv
import sys
from binary import *
from coding import *
from ui import *

option = encode_or_decode()
list_files = find_files()

if option == '1':  # encode
    encode_data = choose_files_encode(list_files)
    print("\n"+"Files: "+str(encode_data))
    img = cv.imread(".\\INPUT\\"+encode_data[0])
    txt = read_file(".\\INPUT\\"+encode_data[1])
    print("Text: "+txt)

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    txt_binary = string_to_binary(txt)
    print("Text in binary: "+txt_binary)

    method = choose_encode_method(img_gray, len(txt_binary))
    if method == '1':
        cv.imshow("Display window", img_gray)
        encode_grayscale(img_gray, txt_binary, encode_data[0])
    else:
        pass

elif option == '2':  # decode
    decode_data = choose_file_to_decode(list_files)
    print("\n"+"File: "+str(decode_data))
    img = cv.imread(".\\INPUT\\"+decode_data)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    binary_code = decode_grayscale(img_gray, decode_data)
    txt = binary_to_string(binary_code)
    write_path = ".\\OUTPUT\\" + decode_data[:-4] + ".txt"
    with open(write_path, "w") as f:
        f.write(txt)


print("#####################")
print("Done")
cv.waitKey(0)
