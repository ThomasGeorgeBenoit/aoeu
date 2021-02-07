import curses
import time
import sys
import os

from lessons.lesson import Lesson
import lessons.lessonIntros

scr = curses.initscr()

def main():

    # init
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    #height, width = scr.getmaxyx()
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()
    scr.keypad(1)
    
    lessons = ['Lesson 0, Starting out', 'Lesson 1, The home row', 
            'Lesson 2, The top row', 'Lesson 3, The bottom row', 
            'Lesson 4:, ,. <> "" :: ;;',
            'Lesson 5, () {} []', 'Lesson 6: _- += |\ ',
            'Lesson 6: Putting it together',
            'Lesson 7: common shell commands', 'Lesson 8: vim commands'
            'Lesson 9: All together']

    q = 0
    while(q==0):
        msg_welcome = "welcome to aoeu"
        print_title()
        print_center(msg_welcome, 3)
        msgl_intro = ["aoeu is made for programmers to easily switch to dvorak.",
                "aoeu focuses on practical phrases and commands for programmers.",
                "We quickly review the normal letters so it is recommended to practice those beforehand.",
                "(There are plenty great tools for that elsewhere)",
                "To start, type any number to select that lesson."]
        print_center_stepped(msgl_intro, 6)
        print_lessons(lessons)

        f=Lesson(0)

        scr.refresh()

        c = scr.getch()

        if c >= 48 and c <= len(lessons)+48:
            intro = get_lesson_intro(c-48)
            scr.clear()
            print_title()
            print_center_stepped([intro[0]], 3)
            print_stepped(intro[1:], 6, 3)
        else:
            print_error("please type a number or press esc to quit")
        
        scr.refresh()
        time.sleep(3)
        q = 1
    #scr.refresh()

    #c = scr.getch()


    #cleanup()
    curses.endwin()

    return

# the top bar
def print_title(): 
    height, width = scr.getmaxyx()
    msg = "AOEU"
    scr.addstr(0, int(width/2)-int(int(len(msg)/2)), msg, curses.color_pair(2))
    msg = "v.0.1"
    scr.addstr(0,0, msg, curses.color_pair(1))

def print_center(msg, x=0):
    height, width = scr.getmaxyx()
    if x == 0:
        scr.addstr(int(height/2), int(width/2)-int(int(len(msg)/2)), msg)
    else:
        scr.addstr(x, int(width/2)-int(int(len(msg)/2)), msg)


def print_lessons(lessons):
    x_start = 13
    y = 4
    for i, lesson in enumerate(lessons):
        m = ''+str(i)+':  '+lesson
        scr.addstr(x_start, y, m)
        x_start+=1

def print_stepped(msgl, x_start, y):
    for msg in msgl:
        scr.addstr(x_start, y, msg)
        x_start+=1

def cleanup():
    curses.nocbreak()   # Turn off cbreak mode
    curses.echo()       # Turn echo back on
    curses.curs_set(1)  # Turn cursor back on
    scr.keypad(0) # Turn off keypad keys

def print_error(msg):
    height, width = scr.getmaxyx()
    scr.addstr(0, int(width)-int(len(msg)), msg, curses.color_pair(2))

#print intro
def get_lesson_intro(num):
    if num == 0:
        return lessons.lessonIntros.get_intro(num)

def print_center_stepped(msgl, x_start):
    x_curr = x_start
    for msg in msgl:
        print_center(msg, x_curr)
        x_curr+=1
    

main()

















