from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import createaccount
import select
import IDdatabase
import adminhome

#Creates the window where the admin inputs his login details.


def admin_login():
    root = Tk()
    #full screen geometry
#    root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))


    mainframe = ttk.Frame(root, padding='3 3 12 12')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    canvas = Canvas(mainframe, width=500, height=300)
    canvas.grid(columnspan=4, column=2, row=1)
    img = ImageTk.PhotoImage(Image.open("Use.png"))

    canvas.create_image(20, 20, anchor=NW, image=img)


    admin_entry = Entry(mainframe, width=30, borderwidth=3)
    admin_entry.grid(columnspan=2, column=2, row=2, sticky=(W, E))
    ttk.Label(mainframe, text='Admin ID').grid(column=1, row=2, sticky=W)

    password_entry = Entry(mainframe, width=30, borderwidth=3, show='*')
    password_entry.grid(columnspan=2, column=2, row=4, sticky=(W, E))
    ttk.Label(mainframe, text='Password').grid(column=1, row=4, sticky=W)

    #Clears all inputs in all entry fields

    def reset():
        try:
            option = messagebox.askquestion('Reset', 'Do you want to reset all inputs?')
            if option == 'yes':
                admin_entry.delete(0, END)
                password_entry.delete(0, END)
            else:
                pass
        except:
            pass

    error_output = Label(mainframe, text='')
    error_output.grid(column=2, row=3)

    pass_error_output = Label(mainframe, text='')
    pass_error_output.grid(column=2, row=5)

    #Redirects the admin to a create account window

    def createtoggle():
        try:
            root.destroy()
            createaccount.admin_window()
        except AttributeError:
            pass

    #Returns admin to the select login type window

    def toggle_home():
        home_message = messagebox.askquestion('', 'Do you want to return to the main page?')
        if home_message == 'yes':
            root.destroy()
            select.homepage()
        else:
            pass

    def toggle_login():
        a = admin_entry.get()
        curs = IDdatabase.curs
        email = curs.execute("SELECT Username FROM Employee")
        ach = curs.fetchall()
        usr = [a]
        data = []
        go = []

        for item in ach:
            data.append(list(item))

        #Checks if user name inputed in username entry field is in database.

        if usr in data:
            error_output.configure(text='')
            go.append(1)
        else:
            error_output.configure(text='Username not recognized')

        b = password_entry.get()
        passcode = curs.execute("SELECT Password FROM Employee")
        ache = curs.fetchall()
        action = [b]
        dataa = []

        for item in ache:
            dataa.append(list(item))
        try:
            #Checks if username index and password index based on collection from database match.
            if action in dataa and dataa.index(action) == data.index(usr):
                pass_error_output.configure(text='')
                go.append(1)
            else:
                pass_error_output.configure(text='Invalid Password')
        except:
            pass

        '''When both username and password checks pass a number is added to a list to help know the number of checks passed.
        When both checks are passed the length of the list then equals two and the login window is destroyed and the admin is then redirected to the main admin page.'''

        if len(go) == 2:
            root.destroy()
            adminhome.home()
        else:
            pass

    check = ttk.Button(mainframe, text='Login', command=toggle_login).grid(column=2, row=6, sticky=(W, E))
    ttk.Button(mainframe, text='Reset', command=reset).grid(column=3, row=6, sticky=(W, E))

    ttk.Button(mainframe, text='Home', command=toggle_home).grid(columnspan=2, column=2, row=8, stick=(W, E))

    for child in mainframe.winfo_children():
        admin_entry.focus()

    ttk.Button(mainframe, text='Create an account', command=createtoggle).grid(columnspan=2, column=2, row=7, sticky=(W,E))
    root.mainloop()
