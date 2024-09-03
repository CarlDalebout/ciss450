# File: main.py
# Directory: ciss450/a/a01/a01q05
# Author: Carl Dalebout

import requests

def chars(s = None):
    char_list = {' ': 0}

    for char in s:
        # print(char)
        char_list[char] = char_list.get(char, 0) + 1
        {
        # match char:
        #     case '0':
        #         char_list['0'] = char_list.get('0', 0) + 1
        #         char_list[' '] += 1
        #     case '1':
        #         char_list['0'] = char_list.get('0', 0) + 1
        #         char_list[' '] += 1
        #     case '2':
        #         char_list['2'] += 1
        #         char_list[' '] += 1
        #     case '3':
        #         char_list['3'] += 1
        #         char_list[' '] += 1
        #     case '4':
        #         char_list['4'] += 1
        #         char_list[' '] += 1
        #     case '5':
        #         char_list['5'] += 1
        #         char_list[' '] += 1
        #     case '6':
        #         char_list['6'] += 1
        #         char_list[' '] += 1
        #     case '7':
        #         char_list['7'] += 1
        #         char_list[' '] += 1
        #     case '8':
        #         char_list['8'] += 1
        #         char_list[' '] += 1
        #     case '9':
        #         char_list['9'] += 1
        #         char_list[' '] += 1

        #     case 'a':
        #         char_list['a'] += 1
        #         char_list[' '] += 1
        #     case 'b':
        #         char_list['b'] += 1
        #         char_list[' '] += 1
        #     case 'c':
        #         char_list['c'] += 1
        #         char_list[' '] += 1
        #     case 'd':
        #         char_list['d'] += 1
        #         char_list[' '] += 1
        #     case 'e':
        #         char_list['e'] += 1
        #         char_list[' '] += 1
        #     case 'f':
        #         char_list['f'] += 1
        #         char_list[' '] += 1
        #     case 'g':
        #         char_list['g'] += 1
        #         char_list[' '] += 1
        #     case 'h':
        #         char_list['h'] += 1
        #         char_list[' '] += 1
        #     case 'i':
        #         char_list['i'] += 1
        #         char_list[' '] += 1
        #     case 'j':
        #         char_list['j'] += 1
        #         char_list[' '] += 1
        #     case 'k':
        #         char_list['k'] += 1
        #         char_list[' '] += 1
        #     case 'l':
        #         char_list['l'] += 1
        #         char_list[' '] += 1
        #     case 'm':
        #         char_list['m'] += 1
        #         char_list[' '] += 1
        #     case 'n':
        #         char_list['n'] += 1
        #         char_list[' '] += 1
        #     case 'o':
        #         char_list['o'] += 1
        #         char_list[' '] += 1
        #     case 'p':
        #         char_list['p'] += 1
        #         char_list[' '] += 1
        #     case 'q':
        #         char_list['q'] += 1
        #         char_list[' '] += 1
        #     case 'r':
        #         char_list['r'] += 1
        #         char_list[' '] += 1
        #     case 's':
        #         char_list['s'] += 1
        #         char_list[' '] += 1
        #     case 't':
        #         char_list['t'] += 1
        #         char_list[' '] += 1
        #     case 'u':
        #         char_list['u'] += 1
        #         char_list[' '] += 1
        #     case 'v':
        #         char_list['v'] += 1
        #         char_list[' '] += 1
        #     case 'w':
        #         char_list['w'] += 1
        #         char_list[' '] += 1
        #     case 'x':
        #         char_list['x'] += 1
        #         char_list[' '] += 1
        #     case 'y':
        #         char_list['y'] += 1
        #         char_list[' '] += 1
        #     case 'z':
        #         char_list['z'] += 1
        #         char_list[' '] += 1

        #     case 'A':
        #         char_list['A'] += 1
        #         char_list[' '] += 1
        #     case 'B':
        #         char_list['B'] += 1
        #         char_list[' '] += 1
        #     case 'C':
        #         char_list['C'] += 1
        #         char_list[' '] += 1
        #     case 'D':
        #         char_list['D'] += 1
        #         char_list[' '] += 1
        #     case 'E':
        #         char_list['E'] += 1
        #         char_list[' '] += 1
        #     case 'F':
        #         char_list['F'] += 1
        #         char_list[' '] += 1
        #     case 'G':
        #         char_list['G'] += 1
        #         char_list[' '] += 1
        #     case 'H':
        #         char_list['H'] += 1
        #         char_list[' '] += 1
        #     case 'I':
        #         char_list['I'] += 1
        #         char_list[' '] += 1
        #     case 'J':
        #         char_list['J'] += 1
        #         char_list[' '] += 1
        #     case 'K':
        #         char_list['K'] += 1
        #         char_list[' '] += 1
        #     case 'L':
        #         char_list['L'] += 1
        #         char_list[' '] += 1
        #     case 'M':
        #         char_list['M'] += 1
        #         char_list[' '] += 1
        #     case 'N':
        #         char_list['N'] += 1
        #         char_list[' '] += 1
        #     case 'O':
        #         char_list['O'] += 1
        #         char_list[' '] += 1
        #     case 'P':
        #         char_list['P'] += 1
        #         char_list[' '] += 1
        #     case 'Q':
        #         char_list['Q'] += 1
        #         char_list[' '] += 1
        #     case 'R':
        #         char_list['R'] += 1
        #         char_list[' '] += 1
        #     case 'S':
        #         char_list['S'] += 1
        #         char_list[' '] += 1
        #     case 'T':
        #         char_list['T'] += 1
        #         char_list[' '] += 1
        #     case 'U':
        #         char_list['U'] += 1
        #         char_list[' '] += 1
        #     case 'V':
        #         char_list['V'] += 1
        #         char_list[' '] += 1
        #     case 'W':
        #         char_list['W'] += 1
        #         char_list[' '] += 1
        #     case 'X':
        #         char_list['X'] += 1
        #         char_list[' '] += 1
        #     case 'Y':
        #         char_list['Y'] += 1
        #         char_list[' '] += 1
        #     case 'Z':
        #         char_list['Z'] += 1
        #         char_list[' '] += 1
        }

    return char_list
    
def print_char_list(char_list):
    for i in range(48, 58):
        if chr(i) in char_list:
            print(f"{chr(i)}: {char_list.get(chr(i))/char_list.get(' ', 1)}")

if __name__ == '__main__':
    
    target = input()

    s = requests.get(target).text
    # s = "abcd 12468"
    char_list = chars(s=s)

    print_char_list(char_list)