#!/usr/bin/env python3
import argparse
import os
import random
import shutil

INVADER = [
'     ▀▄   ▄▀     ',
'    ▄█▀███▀█▄    ',
'   █▀███████▀█   ',
'   ▀ ▀▄▄ ▄▄▀ ▀   ']

INVADER_WIDTH = len(INVADER[0])
INVADER_HEIGHT = len(INVADER)

TERM_WIDTH, TERM_HEIGHT = shutil.get_terminal_size()

RESET = '\x1b[0m'

def print_invaders(rows, num_invaders, mode=None):
    if mode == 'sys':
        print(system_colors(), end='')
    else:
        topspace = (TERM_HEIGHT - ((INVADER_HEIGHT + 2) * rows)) // 2 - 1
        print('\n'*topspace)
        for i in range(rows):
            print_row(num_invaders, mode=mode)

def print_row(num_invaders, mode=None):
    if mode == 'row':
        print(random_row(num_invaders), end='')
    elif mode == 'all':
        print(random_all(num_invaders), end='')
    elif mode == 'line':
        print(random_line(num_invaders), end='')
    else:
        print(random_row(num_invaders), end='')

def random_row(num_invaders):
    whitespace = (TERM_WIDTH - (INVADER_WIDTH * num_invaders)) // 2
    color = '\x1b[38;5;%dm' % random.randint(1, 255)
    string = '\n'
    for i in range(INVADER_HEIGHT):
        string += ' '*whitespace
        string += color + INVADER[i]*num_invaders
        string += '\n'
    string += '\n'
    string += RESET
    return string

def random_all(num_invaders):
    whitespace = (TERM_WIDTH - (INVADER_WIDTH * num_invaders)) // 2
    colors = [random.randint(1, 255) for _ in range(num_invaders)]
    string = '\n'
    for i in range(INVADER_HEIGHT):
        string += ' '*whitespace
        for j in range(num_invaders):
            string += '\x1b[38;5;%dm'%colors[j] + INVADER[i]
        string += '\n'
    string += '\n'
    string += RESET
    return string

def random_line(num_invaders):
    whitespace = (TERM_WIDTH - (INVADER_WIDTH * num_invaders)) // 2
    string = '\n'
    for i in range(INVADER_HEIGHT):
        string += ' '*whitespace
        for j in range(num_invaders):
            color = random.randint(1, 255)
            string += '\x1b[38;5;%dm'%color + INVADER[i]
        string += '\n'
    string += '\n'
    string += RESET
    return string

def system_colors():
    if TERM_WIDTH <= INVADER_WIDTH * 6:
        exit('Current terminal too small: Increase width')
    if TERM_HEIGHT <= (INVADER_HEIGHT * 3) + 6:
        exit('Current terminal too small: Increase height')

    whitespace = (TERM_WIDTH - (INVADER_WIDTH * 6)) // 2
    topspace = (TERM_HEIGHT - ((INVADER_HEIGHT + 2) * 3)) // 2
    colors = [_ for _ in range(1,7)] + [_ for _ in range(9,15)]

    #grayscale
    gs_whitespace= (TERM_WIDTH - (INVADER_WIDTH * 4)) // 2
    gs_colors = [0, 8, 7, 15]

    string = '\n' * topspace
    for i in range(2):
        string += '\n'
        for j in range(INVADER_HEIGHT):
            string += ' '*whitespace
            for k in range(6):
                if i == 1:
                    string += '\x1b[38;5;%dm'%colors[6+k]+ INVADER[j]
                else:
                    string += '\x1b[38;5;%dm'%colors[k]+ INVADER[j]
            string += '\n'
        string += '\n'
    # grayscale colors
    string += '\n'
    for i in range(INVADER_HEIGHT):
        string += ' '*gs_whitespace
        for j in range(4):
            string += '\x1b[38;5;%dm'%gs_colors[j] + INVADER[i]
        string += '\n'
    string += RESET
    return string

def main(args):
    # INVADER_HEIGHT + 2 because each row gets a newline before and after
    if TERM_WIDTH <= INVADER_WIDTH or TERM_HEIGHT <= INVADER_HEIGHT + 2:
        exit('Current terminal too small')

    num_invaders = TERM_WIDTH // INVADER_WIDTH
    num_rows     = TERM_HEIGHT // (INVADER_HEIGHT + 2)

    print_invaders(num_rows, num_invaders, mode=args.c)
    if args.i:
        input()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='invaders')
    parser.add_argument('-i', action='store_true', help='Wait for input before quitting')
    parser.add_argument('-c', default='row', help='Color mode [row, line, all, sys]')
    args = parser.parse_args()

    try:
        main(args)
    except KeyboardInterrupt:
        exit()

'''

   ▀▄   ▄▀      ▄▄▄████▄▄▄      ▄██▄       ▀▄   ▄▀      ▄▄▄████▄▄▄      ▄██▄  
  ▄█▀███▀█▄    ███▀▀██▀▀███   ▄█▀██▀█▄    ▄█▀███▀█▄    ███▀▀██▀▀███   ▄█▀██▀█▄
 █▀███████▀█   ▀▀███▀▀███▀▀   ▀█▀██▀█▀   █▀███████▀█   ▀▀███▀▀███▀▀   ▀█▀██▀█▀
 ▀ ▀▄▄ ▄▄▀ ▀    ▀█▄ ▀▀ ▄█▀    ▀▄    ▄▀   ▀ ▀▄▄ ▄▄▀ ▀    ▀█▄ ▀▀ ▄█▀    ▀▄    ▄▀


 ▄ ▀▄   ▄▀ ▄    ▄▄▄████▄▄▄      ▄██▄     ▄ ▀▄   ▄▀ ▄    ▄▄▄████▄▄▄      ▄██▄  
 █▄█▀███▀█▄█   ███▀▀██▀▀███   ▄█▀██▀█▄   █▄█▀███▀█▄█   ███▀▀██▀▀███   ▄█▀██▀█▄
 ▀█████████▀   ▀▀▀██▀▀██▀▀▀   ▀▀█▀▀█▀▀   ▀█████████▀   ▀▀▀██▀▀██▀▀▀   ▀▀█▀▀█▀▀
  ▄▀     ▀▄    ▄▄▀▀ ▀▀ ▀▀▄▄   ▄▀▄▀▀▄▀▄    ▄▀     ▀▄    ▄▄▀▀ ▀▀ ▀▀▄▄   ▄▀▄▀▀▄▀▄

'''
