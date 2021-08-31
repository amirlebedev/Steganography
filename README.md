# Steganography

Please install opencv-python and numpy on your computer for the program to work.

https://en.wikipedia.org/wiki/Steganography

This is Least Significant Bit steganography. It changes the LSB of each pixel in an image in order to encode data.
Currently only works for grayscale images but can be expanded to encode and decode in RGB channels.

Packages: opencv-python, numpy.

Operation:
Encoding:
1. Put the desired text file and image to encode in the INPUT folder.
2. Run main.
3. The program converts the text to its binary representation. 
Example: Text: Hello World! -> 010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000100001
4. Each bit in the text replaces the LSB of each pixel in the image in sequence.
5. The encoded image is written in the OUTPUT folder.

Decoding:
1. Put the desired image to decode in the INPUT folder.
2. Run main.
3. The program gets the LSB of each pixel in the image and writes the text in a text file in the OUTPUT folder.
