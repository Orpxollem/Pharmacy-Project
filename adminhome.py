from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import select
import recess

#Creates the main page the admin sees when he logs in.

def home():
    top = Tk()

    frame = ttk.Frame(top, padding='3 3 12 12')
    frame.grid(column=0, row=0, sticky=(N, W, E, S))

    canvas = Canvas(frame, width=500, height=300)
    canvas.grid(columnspan=4, column=2, row=1)
    img = ImageTk.PhotoImage(Image.open("Use.png"))
    canvas.create_image(20, 20, anchor=NW, image=img)

    Label(frame, text='           ').grid(column=1, row=1, sticky=E)

    def out():
        home_message = messagebox.askquestion('', 'Do you want to sign out?')
        if home_message == 'yes':
            top.destroy()
            select.homepage()
        else:
            pass

    #Returns the admin to the main login page
    def quited():
        home_message = messagebox.askquestion('', 'Do you want to exit the app?')
        if home_message == 'yes':
            top.destroy()
            select.homepage()
        else:
            pass

    #Navigates the user to a screen where the admin can add new items to the shop or take out some items from the shop
    def inventory():
        top.destroy()
        recess.manage()

    '''This creates a window where the admin sees a list of users logged in with their details.
        This enables the admin to take out users he no longer wishes to provide services to.'''
    def manageuser():
        top.destroy()
        recess.approve()

    '''This creates a window a where the admin sees details( Customer's name and address, admin who attended to customer
    , Items purchased, Receipt number and total amount paid'''

    def viewhistory():
        top.destroy()
        recess.history()

    Button(frame, text='Inventory Management', height=3, borderwidth=5, command=inventory).grid(column=3, row=2, sticky=(W, E))
    Button(frame, text='User Management', height=3, borderwidth=5, command=manageuser).grid(column=3, row=3, sticky=(W, E))
    Button(frame, text='Transactions History', height=3, borderwidth=5, command=viewhistory).grid(column=3, row=4, sticky=(W, E))

    Button(frame, text='Sign Out', command=out, height=2, width=10, borderwidth=2).grid(column=5, row=6, stick=(W, E))
    Label(frame, text='').grid(column=2, row=5)

    Button(frame, text='Close', command=quited, height=2, width=10, borderwidth=2).grid(column=6, row=6, stick=(W, E))

    top.mainloop()
