BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME= "Arial"
SOURCE_LANG = "French"
from tkinter import *
import pandas as pd
import random

#-------------CREATE NEW FLASH CARD--------

data =pd.read_csv("data/french_words.csv")
new_dict=data.to_dict(orient="records")
print(new_dict)


def generate_word():

    """ This function allows to pick a random word from the dictionary created fin the csv file """
    word= random.choice(list(new_dict))
    print(word)
    french_word=word["French"]
    english_word=word["English"]
    canvas.itemconfig(source_word, text=french_word)



#---------------CREATE USER INTERFACE-------------------

window =Tk()
window.title("Flash Card")
window.config(padx = 50, pady= 50, width= 800 , height=525, bg = BACKGROUND_COLOR)

canvas= Canvas(width=800, height= 525, bg= BACKGROUND_COLOR, highlightthickness= 0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 260, image=card_front)
source_language= canvas.create_text(400,150, text= SOURCE_LANG, font= (FONT_NAME, 40, "italic"))
source_word= canvas.create_text(400,263, text="trouve", font= (FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_img = PhotoImage(file="images/right.png")
button_right = Button(image = right_img, highlightthickness=0, command=generate_word)
button_right.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image = wrong_img, highlightthickness=0, command=generate_word)
button_wrong.grid(column=0, row=1)


generate_word()


window.mainloop()



