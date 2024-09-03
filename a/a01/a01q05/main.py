# File: main.py
# Directory: ciss450/a/a01/a01q05
# Author: Carl Dalebout

import requests

def chars(s = None):
    char_list = {' ': 0}

    for char in s:
        # print(char)
        match char:
            case '0':
                char_list['0'] = char_list.get('0', 0) + 1
                char_list[' '] += 1
            case '1':
                char_list['1'] = char_list.get('1', 0) + 1
                char_list[' '] += 1
            case '2':
                char_list['2'] = char_list.get('2', 0) + 1
                char_list[' '] += 1
            case '3':
                char_list['3'] = char_list.get('3', 0) + 1
                char_list[' '] += 1
            case '4':
                char_list['4'] = char_list.get('4', 0) + 1
                char_list[' '] += 1
            case '5':
                char_list['5'] = char_list.get('5', 0) + 1
                char_list[' '] += 1
            case '6':
                char_list['6'] = char_list.get('6', 0) + 1
                char_list[' '] += 1
            case '7':
                char_list['7'] = char_list.get('7', 0) + 1
                char_list[' '] += 1
            case '8':
                char_list['8'] = char_list.get('8', 0) + 1
                char_list[' '] += 1
            case '9':
                char_list['9'] = char_list.get('9', 0) + 1
                char_list[' '] += 1

            case 'a':
                char_list['a'] = char_list.get('a', 0) + 1
                char_list[' '] += 1
            case 'b':
                char_list['b'] = char_list.get('b', 0) + 1
                char_list[' '] += 1
            case 'c':
                char_list['c'] = char_list.get('c', 0) + 1
                char_list[' '] += 1
            case 'd':
                char_list['d'] = char_list.get('d', 0) + 1
                char_list[' '] += 1
            case 'e':
                char_list['e'] = char_list.get('e', 0) + 1
                char_list[' '] += 1
            case 'f':
                char_list['f'] = char_list.get('f', 0) + 1
                char_list[' '] += 1
            case 'g':
                char_list['g'] = char_list.get('g', 0) + 1
                char_list[' '] += 1
            case 'h':
                char_list['h'] = char_list.get('h', 0) + 1
                char_list[' '] += 1
            case 'i':
                char_list['i'] = char_list.get('i', 0) + 1
                char_list[' '] += 1
            case 'j':
                char_list['j'] = char_list.get('j', 0) + 1
                char_list[' '] += 1
            case 'k':
                char_list['k'] = char_list.get('k', 0) + 1
                char_list[' '] += 1
            case 'l':
                char_list['l'] = char_list.get('l', 0) + 1
                char_list[' '] += 1
            case 'm':
                char_list['m'] = char_list.get('m', 0) + 1
                char_list[' '] += 1
            case 'n':
                char_list['n'] = char_list.get('n', 0) + 1
                char_list[' '] += 1
            case 'o':
                char_list['o'] = char_list.get('o', 0) + 1
                char_list[' '] += 1
            case 'p':
                char_list['p'] = char_list.get('p', 0) + 1
                char_list[' '] += 1
            case 'q':
                char_list['q'] = char_list.get('q', 0) + 1
                char_list[' '] += 1
            case 'r':
                char_list['r'] = char_list.get('r', 0) + 1
                char_list[' '] += 1
            case 's':
                char_list['s'] = char_list.get('s', 0) + 1
                char_list[' '] += 1
            case 't':
                char_list['t'] = char_list.get('t', 0) + 1
                char_list[' '] += 1
            case 'u':
                char_list['u'] = char_list.get('u', 0) + 1
                char_list[' '] += 1
            case 'v':
                char_list['v'] = char_list.get('v', 0) + 1
                char_list[' '] += 1
            case 'w':
                char_list['w'] = char_list.get('w', 0) + 1
                char_list[' '] += 1
            case 'x':
                char_list['x'] = char_list.get('x', 0) + 1
                char_list[' '] += 1
            case 'y':
                char_list['y'] = char_list.get('y', 0) + 1
                char_list[' '] += 1
            case 'z':
                char_list['z'] = char_list.get('z', 0) + 1
                char_list[' '] += 1

            case 'A':
                char_list['A'] = char_list.get('A', 0) + 1
                char_list[' '] += 1
            case 'B':
                char_list['B'] = char_list.get('B', 0) + 1
                char_list[' '] += 1
            case 'C':
                char_list['C'] = char_list.get('C', 0) + 1
                char_list[' '] += 1
            case 'D':
                char_list['D'] = char_list.get('D', 0) + 1
                char_list[' '] += 1
            case 'E':
                char_list['E'] = char_list.get('E', 0) + 1
                char_list[' '] += 1
            case 'F':
                char_list['F'] = char_list.get('F', 0) + 1
                char_list[' '] += 1
            case 'G':
                char_list['G'] = char_list.get('G', 0) + 1
                char_list[' '] += 1
            case 'H':
                char_list['H'] = char_list.get('H', 0) + 1
                char_list[' '] += 1
            case 'I':
                char_list['I'] = char_list.get('I', 0) + 1
                char_list[' '] += 1
            case 'J':
                char_list['J'] = char_list.get('J', 0) + 1
                char_list[' '] += 1
            case 'K':
                char_list['K'] = char_list.get('K', 0) + 1
                char_list[' '] += 1
            case 'L':
                char_list['L'] = char_list.get('L', 0) + 1
                char_list[' '] += 1
            case 'M':
                char_list['M'] = char_list.get('M', 0) + 1
                char_list[' '] += 1
            case 'N':
                char_list['N'] = char_list.get('N', 0) + 1
                char_list[' '] += 1
            case 'O':
                char_list['O'] = char_list.get('O', 0) + 1
                char_list[' '] += 1
            case 'P':
                char_list['P'] = char_list.get('P', 0) + 1
                char_list[' '] += 1
            case 'Q':
                char_list['Q'] = char_list.get('Q', 0) + 1
                char_list[' '] += 1
            case 'R':
                char_list['R'] = char_list.get('R', 0) + 1
                char_list[' '] += 1
            case 'S':
                char_list['S'] = char_list.get('S', 0) + 1
                char_list[' '] += 1
            case 'T':
                char_list['T'] = char_list.get('T', 0) + 1
                char_list[' '] += 1
            case 'U':
                char_list['U'] = char_list.get('U', 0) + 1
                char_list[' '] += 1
            case 'V':
                char_list['V'] = char_list.get('V', 0) + 1
                char_list[' '] += 1
            case 'W':
                char_list['W'] = char_list.get('W', 0) + 1
                char_list[' '] += 1
            case 'X':
                char_list['X'] = char_list.get('X', 0) + 1
                char_list[' '] += 1
            case 'Y':
                char_list['Y'] = char_list.get('Y', 0) + 1
                char_list[' '] += 1
            case 'Z':
                char_list['Z'] = char_list.get('Z', 0) + 1
                char_list[' '] += 1

    char_list = dict(sorted(char_list.items(), key=lambda item: item[1], reverse=True))
    print(char_list)
    
    return char_list
    
def print_char_list(char_list):
    for i in range(48, 58):
        if chr(i) in char_list:
            print(f"{chr(i)} {char_list.get(chr(i), 1)} {char_list.get(chr(i))/char_list.get(' ', 1)}")
    for i in range(65, 91):
        if chr(i) in char_list:
            print(f"{chr(i)} {char_list.get(chr(i), 1)} {char_list.get(chr(i))/char_list.get(' ', 1)}")
    for i in range(97, 123):
        if chr(i) in char_list:
            print(f"{chr(i)} {char_list.get(chr(i), 1)} {char_list.get(chr(i))/char_list.get(' ', 1)}")

def print_char_list_accending(char_list):
    for i in char_list:
        if i != ' ':
            print(f"{i} {char_list.get(i, 1)} {char_list.get(i, 1)/char_list.get(' ', 1)}")

    # for i in range(48, 58):
    #     if chr(i) in char_list:
    #         print(f"{chr(i)}: {char_list.get(chr(i))/char_list.get(' ', 1)}")
    # for i in range(65, 91):
    #     if chr(i) in char_list:
    #         print(f"{chr(i)}: {char_list.get(chr(i))/char_list.get(' ', 1)}")
    # for i in range(97, 123):
    #     if chr(i) in char_list:
    #         print(f"{chr(i)}: {char_list.get(chr(i))/char_list.get(' ', 1)}")

if __name__ == '__main__':
    
    target = input()

    s = requests.get(target).text
    # s = "Abc,,,,,,abc?????"
    char_list = chars(s=s)

    print_char_list(char_list)
    print()
    print_char_list_accending(char_list)
