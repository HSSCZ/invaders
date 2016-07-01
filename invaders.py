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
    for i in range(rows):
        print_row(num_invaders, mode=mode)

def print_row(num_invaders, mode=None):
    ws = (TERM_WIDTH - (INVADER_WIDTH * num_invaders)) // 2

    if mode == None or mode == 'random_row':
        print(random_row(ws, num_invaders))
    elif mode == 'random_all':
        print(random_all(ws, num_invaders))
    elif mode == 'random_line':
        print(random_line(ws, num_invaders))
    else:
        print(random_row(ws, num_invaders))

def random_row(whitespace, num_invaders):
    color = '\x1b[38;5;%dm' % random.randint(1, 255)
    string = '\n'
    for i in range(INVADER_HEIGHT):
        string += ' '*whitespace
        string += color + INVADER[i]*num_invaders
        string += '\n'
    string += RESET
    return string

def random_all(whitespace, num_invaders):
    colors = [random.randint(1, 255) for _ in range(num_invaders)]
    string = '\n'
    for i in range(INVADER_HEIGHT):
        string += ' '*whitespace
        for j in range(num_invaders):
            string += '\x1b[38;5;%dm'%colors[j] + INVADER[i]
        string += '\n'
    string += RESET
    return string

def random_line(whitespace, num_invaders):
    string = '\n'
    for i in range(INVADER_HEIGHT):
        string += ' '*whitespace
        for j in range(num_invaders):
            color = random.randint(1, 255)
            string += '\x1b[38;5;%dm'%color + INVADER[i]
        string += '\n'
    string += RESET
    return string

def main():
    if TERM_WIDTH <= INVADER_WIDTH or TERM_HEIGHT <= INVADER_HEIGHT:
        exit('Current terminal too small')

    num_invaders = TERM_WIDTH // INVADER_WIDTH
    num_rows     = TERM_HEIGHT // (INVADER_HEIGHT + 2)

    os.system('cls' if os.name == 'nt' else 'clear')
    print_invaders(num_rows, num_invaders)

if __name__ == '__main__':
    main()

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
