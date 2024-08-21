from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import createaccount
import select
import IDdatabase
import cesspool
import database

curr = database.cursor
conn = database.connect

#Customer Login Window

def customer_login():
    root3 = Tk()
    root3.title("Login")

    mainframe = ttk.Frame(root3, padding='3 3 12 12')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    canvas = Canvas(mainframe, width=500, height=300)
    canvas.grid(columnspan=4, column=2, row=1)
    img = ImageTk.PhotoImage(Image.open("Use.png"))

    canvas.create_image(20, 20, anchor=NW, image=img)

    user_entry = Entry(mainframe, width=30, borderwidth=3)
    user_entry.grid(columnspan=2, column=2, row=2, sticky=(W, E))
    ttk.Label(mainframe, text='Username').grid(column=1, row=2, sticky=W)

    password_entry = Entry(mainframe, width=30, borderwidth=3, show='*')
    password_entry.grid(columnspan=2, column=2, row=4, sticky=(W, E))
    ttk.Label(mainframe, text='Password').grid(column=1, row=4, sticky=W)

    def toggle_login():
        count = 0
        a = user_entry.get()
        usr = [a]
        data = []
        curs = IDdatabase.curs

        email = curs.execute("SELECT Username FROM Customer")
        ach = curs.fetchall()
        curs.execute("SELECT EMAIL FROM Customer")
        get = curs.fetchall()
        curs.execute("SELECT Firstname FROM Customer")
        get1 = curs.fetchall()
        curs.execute("SELECT Lastname FROM Customer")
        get2 = curs.fetchall()

        name1 = []
        name2 = []
        address = []

        for item in get:
            address.append(list(item))

        for item in get1:
            name1.append(list(item))

        for item in get2:
            name2.append(list(item))

        for item in ach:
            data.append(list(item))

        #Checks if the username inputed in the username entry filed is in the database.
        if usr in data:
            index = data.index(usr)
            for item in name1[index]:
                f_name = ''.join(item)

            for item in name2[index]:
                r_name = ''.join(item)

            for item in address[index]:
                f_mail = ''.join(item)

            error_output.configure(text='')
            count += 1

            rf_name = f_name + ' ' + r_name
        else:
            error_output.configure(text='Username not recognized')

        b = password_entry.get()
        passcode = curs.execute("SELECT Password FROM Customer")
        ache = curs.fetchall()
        action = [b]
        dataa = []

        for item in ache:
            dataa.append(list(item))

        #Checks if the password inputed matches the username provided
        try:
            if action in dataa and dataa.index(action) == data.index(usr):
                pass_error_output.configure(text='')
                count += 1
            else:
                pass_error_output.configure(text='Invalid Password')
        except ValueError:
            pass

        if count == 2:
            curr.execute("INSERT INTO Logins(Name, Email) VALUES(?, ?)", (str(rf_name), str(f_mail)))
            conn.commit()
            root3.destroy()
            cesspool.shop()

    def reset():
        try:
            option = messagebox.askquestion('Reset', 'Do you want to reset all inputs?')
            if option == 'yes':
                user_entry.delete(0, END)
                password_entry.delete(0, END)
                error_output.configure(text='')
                pass_error_output.configure(text='')
            else:
                pass
        except:
            pass

    error_output = Label(mainframe, text='')
    error_output.grid(column=2, row=3)

    pass_error_output = Label(mainframe, text='')
    pass_error_output.grid(column=2, row=5)

    check = ttk.Button(mainframe, text='Login', command=toggle_login).grid(column=2, row=6, sticky=(W, E))
    ttk.Button(mainframe, text='Reset', command=reset).grid(column=3, row=6, sticky=(W, E))

    def createtoggle():
        root3.destroy()
        createaccount.window()

    def toggle_home():
        home_message = messagebox.askquestion('', 'Do you want to return to the main page?')
        if home_message == 'yes':
            root3.destroy()
            select.homepage()
        else:
            pass

    ttk.Button(mainframe, text='Home', command=toggle_home).grid(columnspan=2, column=2, row=8, stick=(W, E))

    for child in mainframe.winfo_children():
        user_entry.focus()

    ttk.Button(mainframe, text='Create an account', command=createtoggle).grid(columnspan=2, column=2, row=7, sticky=(W, E))
    root3.mainloop()
