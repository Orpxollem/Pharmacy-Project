from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import select
import IDdatabase

con = IDdatabase.con
curs = IDdatabase.curs
username = '^\w+([.-]?w+)*'

email = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

passLimit = '\w{8,12}\d{4,8}'

option_1 = [
    '01',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    '23',
    '24',
    '25',
    '26',
    '27',
    '28',
    '29',
    '30',
    '31'
]

option_2 = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

option_3 = [
    '1990',
    '1991',
    '1992',
    '1993',
    '1994',
    '1995',
    '1996',
    '1997',
    '1998',
    '1999',
    '2000',
    '2001',
    '2002',
    '2003',
    '2004',
    '2005',
    '2006',
    '2007',
    '2008',
    '2009',
    '2010',
    '2011',
    '2012',
    '2013',
    '2014',
    '2015',
    '2016',
    '2017',
    '2018',
    '2019',
]

name = '^[a-zA-Z .\'-]+$'


'''This file contains two functions which both create login windows.
The reason for this action was to separate the customer's create account from the admin's create account'''


#Customer Create Account Window

def window():
    try:
        root4 = Tk()
        root4.title('Create an account')

        secondframe = ttk.Frame(root4, padding='3 3 12 12')
        secondframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(secondframe, text='First name').grid(column=1, row=1, sticky=W)
        f_name = Entry(secondframe, width=20, borderwidth=3)
        f_name.grid(columnspan=2, column=2, row=1, sticky=(W, E))

        ttk.Label(secondframe, text='Last name').grid(column=1, row=3, sticky=W)
        l_name = Entry(secondframe, width=20, borderwidth=3)
        l_name.grid(columnspan=2, column=2, row=3, sticky=(W, E))

        lastname_error = Label(secondframe, text='')
        lastname_error.grid(column=2, row=4)
        firstname_error = ttk.Label(secondframe, text='')
        firstname_error.grid(column=2, row=2)
        day_error = ttk.Label(secondframe, text='')
        day_error.grid(column=2, row=6)
        month_error = ttk.Label(secondframe, text='')
        month_error.grid(column=3, row=6)
        year_error = ttk.Label(secondframe, text='')
        year_error.grid(column=5, row=6)
        radio_error = ttk.Label(secondframe, text='')
        radio_error.grid(column=2, row=8)
        email_error = ttk.Label(secondframe, text='')
        email_error.grid(column=2, row=10)
        username_error = ttk.Label(secondframe, text='')
        username_error.grid(column=2, row=12)
        create_pass_error = ttk.Label(secondframe, text='')
        create_pass_error.grid(column=2, row=14)
        confirm_pass_error = ttk.Label(secondframe, text='')
        confirm_pass_error.grid(column=2, row=16)

        ttk.Label(secondframe, text='Date of birth').grid(column=1, row=5, sticky=W)

        day = ttk.Combobox(secondframe, values=option_1, width=3)
        day.grid(column=2, row=5, sticky=(W, E))
        day.set('Day')

        month = ttk.Combobox(secondframe, values=option_2, width=6)
        month.grid(columnspan=2, column=3, row=5, sticky=(W, E))
        month.set('Month')

        year = ttk.Combobox(secondframe, values=option_3, width=5)
        year.grid(columnspan=2, column=5, row=5, sticky=(W, E))
        year.set('Year')

        radio = StringVar()

        ttk.Label(secondframe, text='Gender').grid(column=1, row=7, sticky=W)
        male = Radiobutton(secondframe, text='Male', variable=radio, value='Male', indicatoron=0)
        male.grid(columnspan=2, column=2, row=7, sticky=(W, E))
        female = Radiobutton(secondframe, text='Female', variable=radio, value='Female', indicatoron=0)
        female.grid(columnspan=2, column=4, row=7, sticky=(W, E))

        ttk.Label(secondframe, text='Email Address').grid(column=1, row=9, sticky=W)
        email_entry = Entry(secondframe, width=40, borderwidth=3)
        email_entry.grid(columnspan=4, column=2, row=9, sticky=(W, E))

        ttk.Label(secondframe, text='Username').grid(column=1, row=11, sticky=W)
        username_entry = Entry(secondframe, width=20, borderwidth=3)
        username_entry.grid(column=2, row=11, sticky=(W, E))

        ttk.Label(secondframe, text='Create Password').grid(column=1, row=13, sticky=W)
        password_entry = Entry(secondframe, width=22, borderwidth=3)
        password_entry.grid(columnspan=2, column=2, row=13, sticky=(W, E))

        ttk.Label(secondframe, text='Confirm Password').grid(column=1, row=15, sticky=W)
        confirm_password = Entry(secondframe, width=22, borderwidth=3)
        confirm_password.grid(columnspan=2, column=2, row=15, sticky=(W, E))
    except:
        pass

    def doned():
        last = l_name.get()
        first = f_name.get()
        days = day.get()
        months = month.get()
        years = year.get()
        user_name = email_entry.get()
        user_id = username_entry.get()
        create_pass = password_entry.get()
        confirm_pass = confirm_password.get()
        radio_s = radio.get()

        curs.execute("SELECT Username FROM Customer")
        ach = curs.fetchall()
        ache = []

        for item in ach:
            ache.append(list(item))

        errors = []

        #Checks if first name provided matches the regex "name"
        if re.search(name, first):
            firstname_error.configure(text='')
            firs = first
            errors.append(1)
        elif first == '':
            firstname_error.configure(text='Field must not be left blank')
        else:
            firstname_error.configure(text='Input a valid name')

        # Checks if last name provided matches the regex "name"
        if re.search(name, last):
            lastname_error.configure(text='')
            las = last
            errors.append(1)
        elif last == '':
            lastname_error.configure(text='Field must not be left blank')
        else:
            lastname_error.configure(text='Input a valid name')

        if days == 'Day' or days == '':
            day_error.configure(text='Field must not be left blank')
        elif days not in option_1:
            day_error.configure(text='Invalid Input')
        elif days in option_1:
            day_error.configure(text='')
            dy = days
            errors.append(1)

        if months == 'Month' or months == '':
            month_error.configure(text='Field must not be left blank')
        elif months not in option_2:
            month_error.configure(text='Invalid Input')
        elif days in option_1:
            month_error.configure(text='')
            mn = months
            errors.append(1)

        if years == 'Year' or years == '':
            year_error.configure(text='Field must not be left blank')
        elif years not in option_3:
            year_error.configure(text='Invalid Input')
        elif years in option_3:
            year_error.configure(text='')
            yr = years
            errors.append(1)

        if radio_s == 'Male':
            radio_error.configure(text='')
            radi_s = 'Male'
            errors.append(1)
        elif radio_s == 'Female':
            radio_error.configure(text='')
            radi_s = 'Female'
            errors.append(1)
        else:
            radio_error.configure(text='Select a gender')

        # Checks if username name provided matches the regex "username" which specifies valid usernames the user can create
        if re.search(username, user_id):
            if user_id in ache:
                username_error.configure(text='Username taken')
            else:
                pass

            username_error.configure(text='')
            use_id = user_id
            errors.append(1)
        else:
            username_error.configure(text='Examples of valid usernames: joe, joe.smith, joe-smith, joesmith16')

        if user_id == '':
            username_error.configure(text='Field must not be left blank')

        if re.search(email, user_name):
            email_error.configure(text='')
            user_nam = user_name
            errors.append(1)
        else:
            email_error.configure(text='Enter a valid email Address')

        if username == '':
            email_error.configure(text='field must not be left blank')

        if re.search(passLimit, create_pass):
            create_pass_error.configure(text='Strong')
            create_p = create_pass
            errors.append(1)
        else:
            create_pass_error.configure(
                text=' Password not strong. Your password must contain at least 8 letters and 4 numbers.')

        if len(create_pass) > 16:
            create_pass_error.configure(text='You are limited to only 16 characters!')
        else:
            pass

        if confirm_pass == create_pass:
            confirm_pass_error.configure(text='')
        else:
            confirm_pass_error.configure(text='Passwords do not match')

        def check():
            if len(errors) == 9:
                date = dy + '.' + mn + '.' + yr
                curs.execute(
                    "INSERT INTO Customer(FIRSTNAME, LASTNAME, DOB, GENDER, EMAIL, PASSWORD, USERNAME) VALUES(?, ?, ?, ?, ?, ?, ?)",
                    (
                        str(firs), str(las), str(date), str(radi_s), str(user_nam), str(create_p), str(use_id)))
                con.commit()
                root4.destroy()
                select.homepage()
            else:
                messagebox.showwarning('Error', 'Make sure all details provided are correct')
        check()

    def cancel():
        message_box = messagebox.askquestion('', 'Cancel?')
        if message_box == 'yes':
            root4.destroy()
        else:
            pass

    def reset():
        option = messagebox.askquestion('Reset', 'Do you want to reset all inputs?')
        if option == 'yes':
            l_name.delete(0, END)
            lastname_error.configure(text='')
            f_name.delete(0, END)
            firstname_error.configure(text='')
            day.set('Day')
            day_error.configure(text='')
            month.set('Month')
            month_error.configure(text='')
            year.set('Year')
            year_error.configure(text='')
            radio_error.configure(text='')
            email_entry.delete(0, END)
            email_error.configure(text='')
            username_entry.delete(0, END)
            username_error.configure(text='')
            password_entry.delete(0, END)
            create_pass_error.configure(text='')
            confirm_password.delete(0, END)
            confirm_pass_error.configure(text='')
        else:
            pass

    def toggle_home():
        home_message = messagebox.askquestion('', 'Do you want to return to the main page?')
        if home_message == 'yes':
            root4.destroy()
            select.homepage()
        else:
            pass

    ttk.Button(secondframe, text='Done', command=doned).grid(columnspan=2, column=2, row=17, stick=(W, E))
    ttk.Button(secondframe, text='Cancel', command=cancel).grid(columnspan=2, column=4, row=18, sticky=(W, E))
    ttk.Button(secondframe, text='Home', command=toggle_home).grid(columnspan=2, column=2, row=18, sticky=(W, E))
    ttk.Button(secondframe, text='Reset', command=reset).grid(columnspan=2, column=4, row=17, sticky=(W, E))


#Admin Create Account Window

def admin_window():
    root4 = Tk()
    root4.title('Create an account')

    secondframe = ttk.Frame(root4, padding='3 3 12 12')
    secondframe.grid(column=0, row=0, sticky=(N, W, E, S))

    Label(secondframe, text='First name').grid(column=1, row=1, sticky=W)
    f_name = Entry(secondframe, width=20, borderwidth=3)
    f_name.grid(columnspan=2, column=2, row=1, sticky=(W, E))

    Label(secondframe, text='Last name').grid(column=1, row=3, sticky=W)
    l_name = Entry(secondframe, width=20, borderwidth=3)
    l_name.grid(columnspan=2, column=2, row=3, sticky=(W, E))

    lastname_error = Label(secondframe, text='')
    lastname_error.grid(column=2, row=4)
    firstname_error = ttk.Label(secondframe, text='')
    firstname_error.grid(column=2, row=2)
    day_error = ttk.Label(secondframe, text='')
    day_error.grid(column=2, row=6)
    month_error = ttk.Label(secondframe, text='')
    month_error.grid(column=3, row=6)
    year_error = ttk.Label(secondframe, text='')
    year_error.grid(column=5, row=6)
    radio_error = ttk.Label(secondframe, text='')
    radio_error.grid(column=2, row=8)
    email_error = ttk.Label(secondframe, text='')
    email_error.grid(column=2, row=10)
    username_error = ttk.Label(secondframe, text='')
    username_error.grid(column=2, row=12)
    create_pass_error = ttk.Label(secondframe, text='')
    create_pass_error.grid(column=2, row=14)
    confirm_pass_error = ttk.Label(secondframe, text='')
    confirm_pass_error.grid(column=2, row=16)

    ttk.Label(secondframe, text='Date of birth').grid(column=1, row=5, sticky=W)

    day = ttk.Combobox(secondframe, values=option_1, width=3)
    day.grid(column=2, row=5, sticky=(W, E))
    day.set('Day')

    month = ttk.Combobox(secondframe, values=option_2, width=6)
    month.grid(columnspan=2, column=3, row=5, sticky=(W, E))
    month.set('Month')

    year = ttk.Combobox(secondframe, values=option_3, width=5)
    year.grid(columnspan=2, column=5, row=5, sticky=(W, E))
    year.set('Year')

    radio = StringVar()

    Label(secondframe, text='Gender').grid(column=1, row=7, sticky=W)
    male = Radiobutton(secondframe, text='Male', variable=radio, value='Male', indicatoron=0)
    male.grid(columnspan=2, column=2, row=7, sticky=(W, E))
    female = Radiobutton(secondframe, text='Female', variable=radio, value='Female', indicatoron=0)
    female.grid(columnspan=2, column=4, row=7, sticky=(W, E))

    Label(secondframe, text='Email Address').grid(column=1, row=9, sticky=W)
    email_entry = Entry(secondframe, width=40, borderwidth=3)
    email_entry.grid(columnspan=4, column=2, row=9, sticky=(W, E))

    Label(secondframe, text='Admin ID').grid(column=1, row=11, sticky=W)
    username_entry = Entry(secondframe, width=20, borderwidth=3)
    username_entry.grid(column=2, row=11, sticky=(W, E))

    Label(secondframe, text='Create Password').grid(column=1, row=13, sticky=W)
    password_entry = Entry(secondframe, width=22, borderwidth=3)
    password_entry.grid(columnspan=2, column=2, row=13, sticky=(W, E))

    Label(secondframe, text='Confirm Password').grid(column=1, row=15, sticky=W)
    confirm_password = Entry(secondframe, width=22, borderwidth=3)
    confirm_password.grid(columnspan=2, column=2, row=15, sticky=(W, E))

    def done():
        last = l_name.get()
        first = f_name.get()
        days = day.get()
        months = month.get()
        years = year.get()
        user_name = email_entry.get()
        user_id = username_entry.get()
        create_pass = password_entry.get()
        confirm_pass = confirm_password.get()
        radio_s = radio.get()

        errors = []

        if re.search(name, first):
            firstname_error.configure(text='')
            firs = first
            errors.append(1)
        elif first == '':
            firstname_error.configure(text='Field must not be left blank')
        else:
            firstname_error.configure(text='Input a valid name')

        if re.search(name, last):
            lastname_error.configure(text='')
            las = last
            errors.append(1)
        elif last == '':
            lastname_error.configure(text='Field must not be left blank')
        else:
            lastname_error.configure(text='Input a valid name')

        if days == 'Day' or days == '':
            day_error.configure(text='Field must not be left blank')
        elif days not in option_1:
            day_error.configure(text='Invalid Input')
        elif days in option_1:
            day_error.configure(text='')
            dy = days
            errors.append(1)

        if months == 'Month' or months == '':
            month_error.configure(text='Field must not be left blank')
        elif months not in option_2:
            month_error.configure(text='Invalid Input')
        elif days in option_1:
            month_error.configure(text='')
            mn = months
            errors.append(1)

        if years == 'Year' or years == '':
            year_error.configure(text='Field must not be left blank')
        elif years not in option_3:
            year_error.configure(text='Invalid Input')
        elif years in option_3:
            year_error.configure(text='')
            yr = years
            errors.append(1)

        if radio_s == 'Male':
            radio_error.configure(text='')
            radi_s = 'Male'
            errors.append(1)
        elif radio_s == 'Female':
            radio_error.configure(text='')
            radi_s = 'Female'
            errors.append(1)
        else:
            radio_error.configure(text='Select a gender')

        if re.search(username, user_id):
            username_error.configure(text='')
            use_id = user_id
            errors.append(1)
        else:
            username_error.configure(text='Examples of valid id names: joe, joe.smith, joe-smith, joesmith16')

        if user_id == '':
            username_error.configure(text='Field must not be left blank')

        if re.search(email, user_name):
            email_error.configure(text='')
            user_nam = user_name
            errors.append(1)
        else:
            email_error.configure(text='Enter a valid email Address')

        if username == '':
            email_error.configure(text='field must not be left blank')

        if re.search(passLimit, create_pass):
            create_pass_error.configure(text='Strong')
            create_p = create_pass
            errors.append(1)
        else:
            create_pass_error.configure(
                text=' Password not strong. Your password must contain at least 8 letters and 4 numbers.')

        if len(create_pass) > 16:
            create_pass_error.configure(text='You are limited to only 16 characters!')
        else:
            pass

        if confirm_pass == create_pass:
            confirm_pass_error.configure(text='')
        else:
            confirm_pass_error.configure(text='Passwords do not match')

        def check():
            if len(errors) == 9:
                date = dy + '.' + mn + '.' + yr
                curs.execute(
                    "INSERT INTO Employee(FIRSTNAME, LASTNAME, DOB, GENDER, EMAIL, PASSWORD, USERNAME) VALUES(?, ?, ?, ?, ?, ?, ?)",
                    (
                        str(firs), str(las), str(date), str(radi_s), str(user_nam), str(create_p), str(use_id)))
                con.commit()
                root4.destroy()
                select.homepage()
            else:
                messagebox.showwarning('Error', 'Make sure all details provided are correct')

        check()

    def cancel():
        message_box = messagebox.askquestion('', 'Cancel?')
        if message_box == 'yes':
            root4.destroy()
        else:
            pass

    def reset():
        option = messagebox.askquestion('Reset', 'Do you want to reset all inputs?')
        if option == 'yes':
            l_name.delete(0, END)
            lastname_error.configure(text='')
            f_name.delete(0, END)
            firstname_error.configure(text='')
            day.set('Day')
            day_error.configure(text='')
            month.set('Month')
            month_error.configure(text='')
            year.set('Year')
            year_error.configure(text='')
            radio_error.configure(text='')
            email_entry.delete(0, END)
            email_error.configure(text='')
            username_entry.delete(0, END)
            username_error.configure(text='')
            password_entry.delete(0, END)
            create_pass_error.configure(text='')
            confirm_password.delete(0, END)
            confirm_pass_error.configure(text='')
        else:
            pass

    def toggle_home():
        home_message = messagebox.askquestion('', 'Do you want to return to the main page?')
        if home_message == 'yes':
            root4.destroy()
            select.homepage()
        else:
            pass

    Button(secondframe, text='Done', command=done).grid(columnspan=2, column=2, row=17, stick=(W, E))
    Button(secondframe, text='Cancel', command=cancel).grid(columnspan=2, column=4, row=18, sticky=(W, E))
    Button(secondframe, text='Home', command=toggle_home).grid(columnspan=2, column=2, row=18, sticky=(W, E))
    Button(secondframe, text='Reset', command=reset).grid(columnspan=2, column=4, row=17, sticky=(W, E))

    root4.mainloop()
