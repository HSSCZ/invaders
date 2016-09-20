#!/usr/bin/env python3
'''
Fills the terminal with invaders!

usage: invaders [-h] [-c {row,seg,all,sys}] [-i] [-l]

optional arguments:
  -h, --help            show this help message and exit
  -c {row,seg,all,sys}  Color mode (default: row)
  -i                    Wait for Enter keypress before quitting
  -l, -L                Clear terminal before printing invaders
'''
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

def print_invaders(num_rows, num_invaders, mode, clear):
    '''
    Prints a grid of invaders `num_invaders` wide by `num_rows` tall

    Colored according to `mode` which must be one of 'row', 'seg', 'all', 'sys'
    Clear the terminal before printing if `clear` is True
    Terminal is always cleared if mode is 'sys'
    '''
    # leading whitespace for invader strings
    whitespace = (TERM_WIDTH - (INVADER_WIDTH * num_invaders)) // 2
    # amount of newlines to center invaders vertically
    topspace = (TERM_HEIGHT - ((INVADER_HEIGHT + 2) * num_rows)) // 2 - 1

    if clear:
        os.system('clear')

    if mode == 'sys':
        if not clear:
            os.system('clear')
        print('\n' * topspace)
        print(system_colors(whitespace), end='')
    else:
        print('\n' * topspace)
        for i in range(num_rows):
            print_row(num_invaders, whitespace, mode)

def print_row(num_invaders, whitespace, mode):
    ''' Prints a row of invaders '''
    if mode == 'row':
        print(random_row(num_invaders, whitespace), end='')
    elif mode == 'all':
        print(random_all(num_invaders, whitespace), end='')
    elif mode == 'seg':
        print(random_seg(num_invaders, whitespace), end='')
    else:
        print(random_row(num_invaders, whitespace), end='')

def random_row(num_invaders, whitespace):
    ''' Returns a row of invaders with the entire row a random color '''
    color = '\x1b[38;5;%dm' % random.randint(1, 255)
    string = '\n'
    for i in range(INVADER_HEIGHT):
        string += ' '*whitespace
        string += color + INVADER[i]*num_invaders
        string += '\n'
    string += '\n'
    string += RESET
    return string

def random_all(num_invaders, whitespace):
    ''' Returns a row of invaders with each invader a random color '''
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

def random_seg(num_invaders, whitespace):
    ''' Returns a row of invaders with each segment a random color '''
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

def system_colors(whitespace):
    ''' Returns a system color display of 6, 6, 4 invaders centered on screen '''
    if TERM_WIDTH <= INVADER_WIDTH * 6:
        exit('Current terminal too small: Increase width')
    if TERM_HEIGHT <= (INVADER_HEIGHT * 3) + 6:
        exit('Current terminal too small: Increase height')
    colors = list(range(1,7)) + list(range(9,15))

    #grayscale
    gs_whitespace= (TERM_WIDTH - (INVADER_WIDTH * 4)) // 2
    gs_colors = [0, 8, 7, 15]

    string = ''
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
    if TERM_WIDTH < INVADER_WIDTH or TERM_HEIGHT < INVADER_HEIGHT:
        exit('Current terminal too small')

    mode = args.c
    clear = args.l

    num_invaders = 6 if mode == 'sys' else TERM_WIDTH // INVADER_WIDTH
    num_rows     = 3 if mode == 'sys' else TERM_HEIGHT // (INVADER_HEIGHT + 2)

    print_invaders(num_rows, num_invaders, mode, clear)

    if args.i:
        input()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='invaders')
    parser.add_argument('-c', default='row', choices=['row', 'seg', 'all', 'sys'],
                        help='Color mode (default: %(default)s)')
    parser.add_argument('-i', action='store_true',
                        help='Wait for Enter keypress before quitting')
    parser.add_argument('-l', '-L', action='store_true',
                        help='Clear terminal before printing invaders')
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
