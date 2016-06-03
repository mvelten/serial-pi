#!/usr/bin/env python

from os import system
from serialpiconfig import *
import curses


def execute_cmd(cmd_string):
    system("clear")
    system(cmd_string)


# define the function blocks
def dev01():
    curses.endwin()
    execute_cmd("sudo screen -S dev01 " + dev01_device + " " + dev01_baud + " && sudo screen -x dev01")


def dev02():
    curses.endwin()
    execute_cmd("sudo screen -S dev02 " + dev02_device + " " + dev02_baud + " && sudo screen -x dev02")


def dev03():
    curses.endwin()
    execute_cmd("sudo screen -S dev03 " + dev03_device + " " + dev03_baud + " && sudo screen -x dev03")


def resume():
    curses.endwin()
    execute_cmd("sudo screen -x")


def shell():
    curses.endwin()
    execute_cmd("bash")


def draw_menu(screen):
    screen.border(0)
    screen.addstr(0, 2, "serial-pi - https://github.com/mvelten/serial-pi")
    screen.addstr(2, 2, "Please press a key...")
    screen.addstr(4, 4, "1 : " + dev01_name)
    screen.addstr(5, 4, "2 : " + dev02_name)
    screen.addstr(6, 4, "3 : " + dev03_name)
    screen.addstr(8, 4, "5 : Resume broken/detached session")
    screen.addstr(9, 4, "6 : Shell")
    screen.addstr(11, 4, "q : Quit")
    screen.addstr(13, 4, "> ")


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
            screen.addstr(15, 6, "unknown key")
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
