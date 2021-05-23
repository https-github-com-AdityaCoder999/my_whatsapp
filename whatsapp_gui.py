from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

def picsend():
    global f2
    global f1

    file = askopenfilename(defaultextension=".png",
                           filetypes=[("Image File", "*.png"), ("Text Documents", "*.jpg")])

    image = Image.open(file)
    photo = ImageTk.PhotoImage(image)
    
    label1 = Label(f2, image=photo, bg="white")
    label1.image = photo
    label1.pack(side=TOP, fill=X, pady=15)

    label1 = Label(f1, image=photo, bg="green")
    label1.image = photo
    label1.pack(side=TOP, fill=X, pady=15)

def picsend1():
    global f1
    global f2

    file = askopenfilename(defaultextension=".png",
                           filetypes=[("Image File", "*.png"), ("Text Documents", "*.jpg")])

    image = Image.open(file)
    photo = ImageTk.PhotoImage(image)
    
    label1 = Label(f1, image=photo, bg="white")
    label1.image = photo
    label1.pack(side=TOP, fill=X, pady=15)

    label1 = Label(f2, image=photo, bg="green")
    label1.image = photo
    label1.pack(side=TOP, fill=X, pady=15)

def Send1():
    global msg
    global f2   

    Label(f2, text=msg.get(), bg="white").pack(side=TOP, fill=X, pady=15)
    Label(f1, text=msg.get(), bg="green").pack(side=TOP, fill=X, pady=15)

    msg.set("")
    # pass

def Send2():
    global msg2
    global f1  

    Label(f2, text=msg2.get(), bg="green").pack(side=TOP, fill=X, pady=15)
    Label(f1, text=msg2.get(), bg="white").pack(side=TOP, fill=X, pady=15)

    msg2.set("")
    # pass

root = Tk()
#our logic starts here --> 
root.geometry("1000x830")

f1 = Frame(root, bg = "#ffffb3", borderwidth=6, relief=SUNKEN)
f1.pack(side="left", fill=Y, ipadx=280)

f2 = Frame(root, bg = "#ffffb3", borderwidth=6, relief=SUNKEN)
f2.pack(side="left", fill=Y, ipadx=360)

l1 = Label(f1, text="Me", font="lucida 13 bold").pack()
l2 = Label(f2, text="You", font="lucida 13 bold").pack()

pic = Button(f1, text="Pics", command=picsend, font="lucida 9", fg="white", bg="blue").pack(side=BOTTOM)

Button(f1, text="Send", command=Send1, font="lucida 9", fg="white", bg="blue").pack(side=BOTTOM)
# Label(f1, text="aditya is my good name.").pack(side=BOTTOM) --> This is a experiment
msg = StringVar()
msgval = Entry(f1, textvariable=msg, font="lucida 15")
msgval.pack(fill=X, ipady=10, side=BOTTOM, pady=10)


# root.mainloop()

pic1 = Button(f2, text="Pics", command=picsend1, font="lucida 9", fg="white", bg="blue").pack(side=BOTTOM)
Button(f2, text="Send", command=Send2, font="lucida 9", fg="white", bg="blue").pack(side=BOTTOM)
msg2 = StringVar()
msgval = Entry(f2, textvariable=msg2, font="lucida 15")
msgval.pack(fill=X, ipady=10, side=BOTTOM, pady=10)

root.mainloop()