from tkinter import *
from tkinter.ttk import Combobox
import random

def play_game():
    global score
    user = user_choice.get()
    computer = random.choice(["Rock", "Paper", "Scissor"])

    result_message = "It's a tie!"
    if (user == "Rock" and computer == "Scissor") or \
       (user == "Paper" and computer == "Rock") or \
       (user == "Scissor" and computer == "Paper"):
        result_message = "You win!"
        score += 1
    elif (user == "Rock" and computer == "Paper") or \
         (user == "Paper" and computer == "Scissor") or \
         (user == "Scissor" and computer == "Rock"):
        result_message = "You lose!"

    user_label.config(text="You choice: " + user)
    computer_label.config(text="Computer choice: " + computer)
    result_label.config(text=result_message)
    score_label.config(text="Score: " + str(score))

def quit_game():
    global score
    Label(root, text="Your final score: "+str(score), font=("Arial", 15, "bold"), bg="#A6665E", fg="orange").pack()

root = Tk()
root.geometry("400x280")
root.title("Rock Paper Scissor")
root.configure(bg="#A6665E")

title = Label(root, text="Rock Paper Scissors", font=("Arial", 15, "bold"), bg="#A6665E", fg="sky blue")
title.pack()

score = 0
score_label = Label(root, text="Score: " + str(score), font=("Arial", 15, "bold"), bg="#A6665E", fg="gold")
score_label.pack()

user_choice = Combobox(root, values=["Rock", "Paper", "Scissor"], font=("Arial", 15, "bold"))
user_choice.pack()

play_button = Button(root, text="Play", command=play_game, font=("Arial", 12, "bold"), bg="sky blue", fg="white")
play_button.pack()

quit_button = Button(root, text="Quit", command=quit_game, font=("Arial", 12, "bold"), bg="red", fg="white")
quit_button.pack()

user_label = Label(root, font=("Arial", 15, "bold"), bg="#A6665E", fg="light green")
user_label.pack()
computer_label = Label(root, font=("Arial", 15, "bold"), bg="#A6665E", fg="light green")
computer_label.pack()
result_label = Label(root, font=("Arial", 15, "bold"), bg="#A6665E", fg="light green")
result_label.pack()

root.mainloop()
