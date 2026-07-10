from tkinter import *

window = Tk()

window.geometry('720x480')
window.title("Quiz App.")
window.config(background="#E99FBF")

quiztitle = Label(window, text= "Quiz app",
                  font = ("Georgia",25,'italic'),
                  padx=5,pady=5
                  )
quiztitle.pack(anchor='center')


window.mainloop()