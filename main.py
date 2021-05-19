BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME= "Arial"
SOURCE_LANG = "French"
TIME =3
from tkinter import *
import pandas as pd
import random

#-------------CREATE NEW FLASH CARD--------

data =pd.read_csv("data/french_words.csv")
new_dict=data.to_dict(orient="records")
print(new_dict)


word= {}

def generate_word():

    """ This function allows to pick a random word from the dictionary created fin the csv file """
    global word, flip_timer
    window.after_cancel(flip_timer)
    word= random.choice(list(new_dict))
    print(word)
    french_word=word["French"]
    canvas.itemconfig(source_language, text=SOURCE_LANG, fill="black")
    canvas.itemconfig(source_word, text=french_word, fill="black")
    canvas.itemconfig(card ,image= card_front)
    flip_timer = window.after(3000, func= flip_card)

#---------------CREATE A COUNTDOWN TO FLIP CARD ---------

def flip_card():
    """ This function will flip the card after 3 seconds to show the traslation in English"""
    global word
    canvas.itemconfig(card ,image= card_back)
    canvas.itemconfig(source_language,text="English",fill= "white")
    canvas.itemconfig(source_word, text = word["English"], fill="white")

#---------------CREATE USER INTERFACE-------------------

window =Tk()
window.title("Flash Card")
window.config(padx = 50, pady= 50, width= 800 , height=525, bg = BACKGROUND_COLOR)
flip_timer = window.after( 3000, flip_card)


canvas= Canvas(width=800, height= 525, bg= BACKGROUND_COLOR, highlightthickness= 0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 260, image=card_front)
source_language= canvas.create_text(400,150, text= SOURCE_LANG, font= (FONT_NAME, 40, "italic"))
source_word= canvas.create_text(400,263, text="trouve", font= (FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_img = PhotoImage(file="images/right.png")
button_right = Button(image = right_img, highlightthickness=0, command=generate_word)
button_right.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image = wrong_img, highlightthickness=0, command=generate_word)
button_wrong.grid(column=0, row=1)


generate_word() #this will make it show the first word when running



window.mainloop()



