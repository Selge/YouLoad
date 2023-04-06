import tkinter
from tkinter import scrolledtext, INSERT

import youload as yl


def pushed():
    res = link.get()
    check_link(res)


def check_link(res):
    check = str(res).lower()
    if 'playlist' in check:
        check = yl.Multi()
        check.reprint()

    else:
        check = yl.Single()
        check.reprint()


window = tkinter.Tk()
window.title('YouLoad')
window.geometry('400x300')

label = tkinter.Label(window,
                      text="Please, insert your link into the field below:",
                      font=("Arial Bold", 10))
label.grid(column=0, row=0)
# button
button = tkinter.Button(window,
                        text="DOWNLOAD",
                        font=("Arial Bold", 15),
                        bg="red",
                        fg="white",
                        command=pushed)
button.grid(column=0, row=2)
# request link field
link = tkinter.Entry(window, width=50)
link.grid(column=0, row=1)
# result message window
text = scrolledtext.ScrolledText(window, width=40, height=10)
text.grid(column=0, row=4)
text.insert(INSERT, 'Текстовое поле')

window.mainloop()
