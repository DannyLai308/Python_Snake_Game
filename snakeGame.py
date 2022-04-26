from cProfile import label
from tkinter import *
import random
from turtle import window_height, window_width

# Game Constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#0000FF"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

# Game setup initial phase
window = Tk()
window.title("Python Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text="Score:{}".format(score), font=("consolas", 40))
label.pack()

# Setup Canvas
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Center game window upon launching
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}") # Setup coordinates for centering game window

# Instantiate snake
snake = Snake()


window.mainloop()
