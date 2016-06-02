#!/usr/bin/env python

from os import system
import curses


def get_param(prompt_string):
    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, prompt_string)
    screen.refresh()
    input = screen.getstr(10, 10, 60)
    return input


def execute_cmd(cmd_string):
    system("clear")
    system(cmd_string)


x = 0

while x != ord('q'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Please enter a number...")
    screen.addstr(4, 4, "1 - Firewall 01")
    screen.addstr(5, 4, "2 - Firewall 02")
    screen.addstr(6, 4, "3 - Switch")
    screen.addstr(8, 4, "r - Resume session")
    screen.addstr(9, 4, "s - Shell")
    screen.addstr(12, 4, "q - Quit")
    screen.refresh()

    x = screen.getch()

    if x == ord('1'):
        curses.endwin()
        execute_cmd("sudo screen -S pfsense01 /dev/ttyUSB0 115200 && sudo screen -x pfsense01")
    if x == ord('2'):
        curses.endwin()
        execute_cmd("sudo screen -S pfsense02 /dev/ttyUSB1 115200 && sudo screen -x pfsense02")
    if x == ord('3'):
        curses.endwin()
        execute_cmd("sudo screen -S switch /dev/ttyUSB2 115200 && sudo screen -x switch")
    if x == ord('r'):
        curses.endwin()
        execute_cmd("sudo screen -x")
    if x == ord('s'):
        curses.endwin()
        execute_cmd("bash")

curses.endwin()
