from tkinter import *
from tkinter import ttk
#from PIL import ImageTk, Image




def poziv_probe(root):

    dugme = Button(root,text="klikni me")
    dugme.grid()
    root.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.geometry('400x190')
    root.title("PACIJENT")

    poziv_probe(root)


    # app_root = Tk()
    #
    # # Setting it up
    # img = ImageTk.PhotoImage(Image.open("../slike/doktor.jpg"))
    #
    # # Displaying it
    # imglabel = Label(app_root, image=img).grid(row=1, column=1)
    #
    # app_root.mainloop()