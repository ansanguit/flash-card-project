BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME= "Arial"
SOURCE_LANG = "French"
from tkinter import *


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
button_right = Button(image = right_img, highlightthickness=0)
button_right.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image = wrong_img, highlightthickness=0)
button_wrong.grid(column=0, row=1)





window.mainloop()



