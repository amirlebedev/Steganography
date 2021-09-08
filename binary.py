def switch_to_binary(string):
    unicode_value = []
    binaries = []

    for letter in string:
        unicode_value.append(ord(letter))
    for value in unicode_value:
        binaries.append(int(bin(value)[2:]))

    return binaries


def pad_with_zeroes(binaries):
    padded_binaries = []
    for cell in binaries:
        temp = str(cell)
        for i in range(0, 8 - len(temp)):
            temp = "0" + temp
        padded_binaries.append(temp)

    return padded_binaries


def stringify(binaries):
    binary_string = ""
    for value in binaries:
        binary_string += value
    return binary_string


def string_to_binary(string):
    binaries = switch_to_binary(string)
    padded_binaries = pad_with_zeroes(binaries)
    binary_string = stringify(padded_binaries)
    return binary_string


def binary_to_string(binary_code):
    byte = divide_to_bytes(binary_code)
    byte = remove_zero_bytes(byte)
    list_unicode = binary_to_int(byte)
    text = int_to_text(list_unicode)

    return text



def divide_to_bytes(binary_decode):
    length = len(binary_decode)
    start = 0
    end = 8
    decode_list = []
    for i in range(0, length - 1):
        if end > length:
            decode_list.append(binary_decode[start:length - end])
            break
        decode_list.append(binary_decode[start:end])
        start += 8
        end += 8

    return decode_list


def remove_zero_bytes(decode_list):
    # print(decode_list)
    index = 0
    final_index = 0
    for cell in decode_list:
        if cell != '' and int(cell) != 0:
            final_index = index
        index += 1
    sliced = decode_list[:final_index + 1]
    print(sliced)

    return sliced


def binary_to_int(sliced):
    unix = []
    for cell in sliced:
        temp = cell[::-1]
        x = 1
        number = 0
        for digit in temp:
            number += int(digit) * x
            x = x * 2
        unix.append(number)

    print(unix)
    return unix


def int_to_text(unix):
    text = ""
    for cell in unix:
        text += chr(cell)
    print(text)
    return text