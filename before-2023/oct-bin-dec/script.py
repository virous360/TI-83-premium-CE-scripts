# bin ascii text hex (Ali Naim) 2023
menu = input("""1. Text
2. Ascii(code/number)
3. Bin
4. Hex
from : """)

if menu == "1":
    text = input("text:")
    print("Text =",text)
    ascii = [str(ord(letter)) for letter in text]
    print("ascii ="," ".join(ascii))
    print("binary =", " ".join([str(bin(int(number)))[2:] for number in ascii]))
    print("hexadecimal ="," ".join([str(hex(int(letter)))[2:] for letter in ascii]))
elif menu == "2":
    ascii_list = input("ascii: ").split(" ")
    print("text = " + "".join([chr(int(x)) for x in ascii_list]))
    print("binary =", " ".join([str(bin(int(number)))[2:] for number in ascii_list]))
    print("hexadecimal ="," ".join([str(hex(int(letter)))[2:] for letter in ascii_list]))
elif menu == "3":
    binary = [str(int(x,2)) for x in input("bin = ").split(" ")]
    print("ascii = "+" ".join(binary))
    print("text = " + "".join([chr(int(x)) for x in binary]))
    print("hexadecimal ="," ".join([str(hex(int(letter)))[2:] for letter in binary]))
elif menu == "4":
    hex_list = [str(int(x,16)) for x in input("hex = ").split(" ")]
    print("ascii = "+" ".join(hex_list))
    print("text = " + "".join([chr(int(x)) for x in hex_list]))
    print("binary =", " ".join([str(bin(int(number)))[2:] for number in hex_list]))

