from tkinter import *

home = Tk()

home.geometry('720x480')
home.title("Quiz App.")
home.config(background="#E99FBF")

quiztitle = Label(home, text= "Quiz app",
                  font = ("Georgia",25,'italic'),
                  padx=5,pady=5,
                  bg="#E99FBF",
                  )
quiztitle.pack(anchor='center')


welcome = Label(home, text= 'Welcome to quiz app.\n Select the topics you want to take a quiz on.',
                font = ("Arial", 20),bg="#E874A6",
                )
welcome.pack(anchor='center')

questiondict = {}

math = {"What is the sum of the angles inside a triangle?" : ['A) 90°','B) 180°','C) 270°','D) 360°'],
"answer": "B) 180°"}

x = IntVar()
y = IntVar()
z = IntVar()
a = IntVar()

science = Checkbutton(home, text = 'Science',font = ('Georgia',15),
                      bg="#E99FBF",activebackground="#E99FBF",
                      variable = x,onvalue=1,offvalue=0)
science.place(x=100,y=130)

math = Checkbutton(home, text= 'Maths', font = ('Georgia',15),
                   bg="#E99FBF",activebackground="#E99FBF",
                   variable = y,onvalue=1,offvalue=0)
math.place(x=100,y=160)

gk = Checkbutton(home, text= 'General Knowledge', font = ('Georgia',15),
                   bg="#E99FBF",activebackground="#E99FBF",
                   variable = z,onvalue=1,offvalue=0)
gk.place(x=100,y=190)

def toggle():
    math.toggle()
    science.toggle()
    gk.toggle()

all = Checkbutton(home, text = "All", font = ('Georgia',15),
                   bg="#E99FBF",activebackground="#E99FBF",
                   variable = a,onvalue=1,offvalue=0, command = toggle)

all.place(x=100,y=220)

# def proceed():
#     questions()

startquiz = Button(home, text = "Start quiz.",font = ('Georgia',20),)
startquiz.pack()

home.mainloop()



questions = Tk()

questions.geometry('720x480')
questions.config(background="#E99FBF")
questions.title('Quiz started!')


for key,value in questiondict.items():
    questionlabel = Label(questions,text = key,
                          font= ('Georgia',15),
                          bg="#E874A6",
                          )


questions.mainloop()