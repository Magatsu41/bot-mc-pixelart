# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 17:59:00 2021

@author: Magatsu
"""

#IMPORTS
import sys
import time
import pyautogui
import pydirectinput
from PIL import Image

#**********************************

#DEFINE VARIABLES
im = Image.open("./img/image.png", "r")
pix_val = list(im.getdata())
width, height = im.size
colors = []
pixel_arts = []
cur_block=0

#**********************************

#DEFINE FUNCTIONS
def jump():
    pydirectinput.keyDown('space')
    pydirectinput.keyUp('space')

def right_click():
    pyautogui.click(button='right')

def place_block():
    print("placing block")
    jump()
    time.sleep(0.09)
    right_click()

def move_f_one():
    pydirectinput.keyDown('w')
    time.sleep(0.26)
    print("go forward one block")
    pydirectinput.keyUp('w')

def move_b_one():
    pydirectinput.keyDown('s')
    time.sleep(0.26)
    print("go backward one block")
    pydirectinput.keyUp('s')

def move_l_one():
    pydirectinput.keyDown('a')
    time.sleep(0.26)
    print("go left one block")
    pydirectinput.keyUp('a')

def move_l_one_smol():
    pydirectinput.keyDown('shiftleft')
    time.sleep(0.01)
    pydirectinput.keyDown('a')
    time.sleep(0.05)
    print("go left one block")
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('shiftleft')
    time.sleep(0.05)

def move_r_one():
    pydirectinput.keyDown('d')
    time.sleep(0.26)
    print("go right one block")
    pydirectinput.keyUp('d')

def move_r_one_more():
    pydirectinput.keyDown('d')
    time.sleep(0.3)
    print("go right one block")
    pydirectinput.keyUp('d')
    
def change_block(block):
    print("change block to "+str(block))
    pydirectinput.keyDown(block)
    pydirectinput.keyUp(block)

def draw():
    i = 0
    time.sleep(5)
    global cur_block
    while i<len(pixel_arts):
        j=0
        if ((i+1) % 2) == 0:
            print("row is even")
            while j<width:
                k=len(pixel_arts[i])-(j+1)
                if j==0:
                    if (cur_block==0 or cur_block!=pixel_arts[i][k]):
                        change_block(str(pixel_arts[i][k]))
                        cur_block=pixel_arts[i][k]
                    place_block()
                else:
                    if (cur_block==0 or cur_block!=pixel_arts[i][k]):
                        change_block(str(pixel_arts[i][k]))
                        cur_block=pixel_arts[i][k]
                    move_b_one()
                    move_f_one()
                    place_block()
                j=j+1        
        else:
            print("row is odd")
            while j<width:
                if j==0:
                    if (cur_block==0 or cur_block!=pixel_arts[i][j]):
                        change_block(str(pixel_arts[i][j]))
                        cur_block=pixel_arts[i][j]
                    place_block()
                else:
                    if (cur_block==0 or cur_block!=pixel_arts[i][j]):
                        change_block(str(pixel_arts[i][j]))
                        cur_block=pixel_arts[i][j]
                    move_f_one()
                    move_b_one()
                    place_block()
                j=j+1
        move_l_one()
        move_r_one_more()
        move_l_one_smol()
        i=i+1
    print('')
    print("  PIXEL ART FINISHED  ")

def add_color():
    i = 0
    global colors
    while i<len(pix_val):
        if pix_val[i] in colors:
            i=i+1
        else:
            print("Adding color "+str(pix_val[i])+" at index "+str(len(colors)+1))
            colors.append(pix_val[i])
            i=i+1

def get_index(colo):
    if colo in colors:
        return colors.index(colo)+1

def define_pixel():
    i=0
    key=0
    global pixel_arts
    while i<height:
        list_w=[]
        j=0
        while j<width:
            list_w.append(str(get_index(pix_val[key])))
            j=j+1
            key=key+1
        pixel_arts.insert(0, list_w)
        i=i+1
        print("Line is "+str(list_w))
    print("Final variable is "+str(pixel_arts))

def init_img():
    print("Width : "+str(width))
    print("Height : "+str(height))
    print('')
    add_color()
    print(' ')
    define_pixel()
    print(' ')
    print("The image has been parsed")

def init():
    print("Please chose your action : ")
    print(' ')
    print("1 - Parse image")
    print("2 - Draw the pixel art in Minecraft")
    print("3 - Exit")
    action = input()
    action = int(action)
    print(' ')
    if action==1:
        print("*****************************************")
        print('')
        print("    +++ Beginning image parsing +++")
        print('')
        init_img()
        print('')
        print("*****************************************")
        print('')
        init()
    elif action==2:
        if len(colors)<1:
            print("The image has not been parsed")
            print("You must parse the image before running the bot")
            print('')
            init()
        if len(pixel_arts)<2:
            print("The image has not been parsed")
            print("You must parse the image before running the bot")
            print('')
            init()
        if len(colors)>9:
            print("The image color range is too large")
            print("The image can only have 9 color max")
            print('')
            init()
        print("*****************************************")
        print('')
        print("    +++ Beginning drawing the pixel art +++")
        draw()
        print('')
        print("*****************************************")
        print('')
        init()
    elif action==3:
        sys.exit("Exiting the program...")
    else:
        print("You did'nt enter a valid option")
        print('')

#*********************************************

#INIT
print("Welcome to Pixel art drawer bot for Minecraft")
print(' ')
print("This program was written by Magatsu")
print(' ')
init()