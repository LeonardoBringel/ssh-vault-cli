import os
import curses

def display_menu():
    curses.curs_set(0)
    stdscr.clear()

    menu = {

    }

def repl():
    try:
        os.system('clear')
        while True:
            read = input('>> ')
            print(read)
    except KeyboardInterrupt:
        os.system('clear')
        print('\nleaving...')
        exit(0)
    except Exception:
        print('\nsomething weird happened, exiting...')
        exit(1)
