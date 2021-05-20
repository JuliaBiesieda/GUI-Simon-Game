from tkinter import *
import random
from playsound import playsound

is_on = True
game_pattern = []
user_clicked_pattern = []
button_colors = ["red", "blue", "green", "yellow"]

# GUI INTERFACE

window = Tk()
window.title("Simon game")
window.config(padx=100, pady=100, bg="MistyRose")

canvas = Canvas(width=800, height=800, bg="white")

level_label = Label(text="Level 1", fg="gray18", bg="MistyRose", font=("arial", 17))
level_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

red_img = PhotoImage(file="images/red.png")
green_img = PhotoImage(file="images/green.png")
yellow_img = PhotoImage(file="images/yellow.png")
blue_img = PhotoImage(file="images/blue.png")
yes_img = PhotoImage(file="images/yes.png")

red_button = Button(image=red_img, highlightthickness=0, command=lambda m="red": button_pushed(m, user_clicked_pattern))
red_button.grid(column=0, row=1)

green_button = Button(image=green_img, highlightthickness=0, command=lambda m="green": button_pushed(m, user_clicked_pattern))
green_button.grid(column=1, row=1)

blue_button = Button(image=blue_img, highlightthickness=0, command=lambda m="blue": button_pushed(m, user_clicked_pattern))
blue_button.grid(column=0, row=2)

yellow_button = Button(image=yellow_img, highlightthickness=0, command=lambda m="yellow": button_pushed(m, user_clicked_pattern))
yellow_button.grid(column=1, row=2)

# functions


def next_sequence():
    user_clicked_pattern.clear()
    random_color = button_colors[random.randint(0, 3)]
    game_pattern.append(random_color)

    if random_color == "red":
        yes_button(red_button)
        red_button.after(1000, lambda: red_button.config(image=red_img))
    elif random_color == "blue":
        yes_button(blue_button)
        blue_button.after(1000, lambda: blue_button.config(image=blue_img))
    elif random_color == "yellow":
        yes_button(yellow_button)
        yellow_button.after(1000, lambda: yellow_button.config(image=yellow_img))
    else:
        yes_button(green_button)
        green_button.after(1000, lambda: green_button.config(image=green_img))

    return user_clicked_pattern, game_pattern


def yes_button(current_button):
    current_button.config(image=yes_img)


def button_pushed(button_press, user_clicked_pattern):
    playsound(f"sounds/{button_press}.mp3")
    user_clicked_pattern.append(button_press)
    check_answer(len(user_clicked_pattern) - 1)


def check_answer(current_level):
    if game_pattern[current_level] == user_clicked_pattern[current_level]:
        if len(user_clicked_pattern) == len(game_pattern):
            current_level += 1
            level_label.config(text=f"Level: {current_level + 1}")
            canvas.after(1000, next_sequence)
    else:
        level_label.config(text="Wrong! Game Over!")
        red_button.config(state="disabled")
        blue_button.config(state="disabled")
        yellow_button.config(state="disabled")
        green_button.config(state="disabled")


canvas.after(1000, next_sequence)

window.mainloop()
