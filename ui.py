import os
import sys
import cv2 as cv


def quit_illegal_input():
    print("Illegal input entered. Exiting applications.")
    sys.exit()


def find_files():
    list_files = []

    path = '.\\INPUT'
    files = os.listdir(path)
    for f in files:
        list_files.append(f)

    return list_files


def encode_or_decode():
    print("To ENCODE a text file into image, enter 1.")
    print("To DECODE an image into a text file, enter 2.")
    option = input("Your option: ")
    if option != '1' and option != '2':
        quit_illegal_input()
    return option


def choose_files_encode(list_files):
    list_image = []
    list_text = []

    for file in list_files:
        if file[-3:] == 'jpg' or file[-3:] == 'png':
            list_image.append(file)

    for file in list_files:
        if file[-3:] == 'txt':
            list_text.append(file)

    if len(list_image) < 1 or len(list_text) < 1:
        print("Make sure there is at least 1 image and 1 text file.")
        quit_illegal_input()
    elif len(list_image) == 1 and len(list_text) == 1:
        return (list_image[0], list_text[0])
    else:
        print("\nPlease choose image to ENCODE.")
        count = 0
        for file in list_image:
            print("Enter", str(count+1), "for", file)
            count += 1
        user_input = input("Your option: ")
        image_name = list_image[int(user_input)-1]

        print("\nPlease choose text to ENCODE.")
        count = 0
        for file in list_text:
            print("Enter", str(count+1), "for", file)
            count += 1
        user_input = input("Your option: ")
        image_text = list_text[int(user_input)-1]

        return (image_name, image_text)


def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


def choose_encode_method(img_gray, txt_legnth):
    print("\nText bit length:", txt_legnth)
    print("Image LSB bit length:", img_gray.size)
    print("Image 2-bit-LSB bit length:", 2*img_gray.size)
    print("Image 3-channel BGR bit length:", 3*img_gray.size)
    print("Image 3-channel BGR 2-bit-LSB length:", 2*3*img_gray.size)

    print("\nFor grayscale encoding, enter 1.")
    print("For 3-channel BGR encoding, enter 2. [UNAVAILABLE]")
    method = input("")
    if method != '1':
        quit_illegal_input()

    return method


def choose_file_to_decode(list_files):
    list_image = []

    for file in list_files:
        if file[-3:] == 'jpg' or file[-3:] == 'png':
            list_image.append(file)

    if len(list_image) < 1:
        print("Make sure there is at least 1 image in folder.")
        quit_illegal_input()
    elif len(list_image) == 1:
        return list_image[0]
    else:
        print("\nPlease choose image to DECODE.")
        count = 0
        for file in list_image:
            print("Enter", str(count+1), "for", file)
            count += 1
        user_input = input("Your option: ")
        image_name = list_image[int(user_input)-1]

        return image_name
