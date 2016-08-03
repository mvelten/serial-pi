#!/usr/bin/env python

from os import system
from serialpiconfig import *
import curses

line_counter = 4

def execute_cmd(cmd_string):
    system("clear")
    system(cmd_string)


# define the function blocks
def connect_dev(dev):
    print(dev)
    curses.endwin()
    execute_cmd("sudo screen -S dev0" + dev + " " + eval("dev0" + dev + "_device") + " " + eval( "dev0" + dev + "_baud") + " && sudo screen -x dev0" + dev)

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

    line_counter = 4
    for var in ['dev01_name', 'dev02_name', 'dev03_name', 'dev04_name', 'dev05_name', 'dev06_name', 'dev07_name', 'dev08_name']:
        if var in globals():
            screen.addstr(line_counter, 4, str((line_counter - 3)) + ": " + eval(var) )
            line_counter += 1

    screen.addstr((line_counter + 2), 4, "r : Resume broken/detached session")
    screen.addstr((line_counter + 3), 4, "s : Shell")
    screen.addstr((line_counter + 4), 4, "q : Quit")
    screen.addstr((line_counter + 5), 4, "> ")


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
            screen.addstr(2, 2, "you pressed an unknown key")
        screen.refresh()

        x = screen.getch()
        if x == ord('q'):
            break
        elif x == ord('r'):
            resume()
            continue
        elif x == ord('s'):
            shell()
            continue

        try:
            connect_dev(chr(x))
            wrong_key = None
        except:
            wrong_key = True

    curses.endwin()
