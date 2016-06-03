#!/usr/bin/env python

from os import system
import curses


def execute_cmd(cmd_string):
    system("clear")
    system(cmd_string)


# define the function blocks
def dev01():
    curses.endwin()
    execute_cmd("sudo screen -S pfsense01 /dev/ttyUSB0 115200 && sudo screen -x pfsense01")


def dev02():
    curses.endwin()
    execute_cmd("sudo screen -S pfsense02 /dev/ttyUSB1 115200 && sudo screen -x pfsense02")


def dev03():
    curses.endwin()
    execute_cmd("sudo screen -S switch /dev/ttyUSB2 115200 && sudo screen -x switch")


def resume():
    curses.endwin()
    execute_cmd("sudo screen -x")


def shell():
    curses.endwin()
    execute_cmd("bash")


def draw_menu(screen):
    screen.border(0)
    screen.addstr(2, 2, "Please enter a number...")
    screen.addstr(4, 4, "1 - Firewall 01")
    screen.addstr(5, 4, "2 - Firewall 02")
    screen.addstr(6, 4, "3 - Switch")
    screen.addstr(8, 4, "5 - Resume session")
    screen.addstr(9, 4, "6 - Shell")
    screen.addstr(12, 4, "q - Quit")


#
# main loop
#
if __name__ == '__main__':

    x = 0
    wrong_key = None
    while 1:
        screen = curses.initscr()

        screen.clear()
        draw_menu(screen)
        if wrong_key:
            screen.addstr(14, 6, "unknown key")
        screen.refresh()

        # map the inputs to the functions
        options = {1: dev01,
                   2: dev02,
                   3: dev03,
                   5: resume,
                   6: shell,
                   }

        x = screen.getch()
        if x == ord('q'):
            break

        try:
            options[int(chr(x))]()
            wrong_key = None
        except:
            wrong_key = True

    curses.endwin()
