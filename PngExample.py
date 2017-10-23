# 2017-10-21
# Code from Stack Overflow post
# "Display and Hide PNG image in Tkinter Python3"
# https://stackoverflow.com/questions/34915202/display-and-hide-png-image-in-tkinter-python3
# by contributor "Constantly Confused"
# https://stackoverflow.com/users/4071682/constantly-confused
#
# Orignal code cut-n-pasted from webpage apart from png file used.

import tkinter

def hideBG():
    global state
    if state == "Hidden":
        background_label.pack()
        state = "Showing"

    elif state == "Showing":
        background_label.pack_forget()
        state = "Hidden"

window = tkinter.Tk()

background_image=tkinter.PhotoImage(file="Conifers_32x32.png")
background_label = tkinter.Label(window, image=background_image)

hideBttn = tkinter.Button(window, text="Hide Background", command=hideBG)
state = "Showing"

hideBttn.pack()
background_label.pack()

window.mainloop()