from tkinter import *
from tkinter import ttk
import database
import IDdatabase
import re
from tkinter import messagebox
import adminhome

letter = '\w+'

con = database.connect
conn = IDdatabase.con
curs = database.cursor
cur = IDdatabase.curs

#Creates a window where the admin adds or removes items from the shop

def manage():
    root = Tk()

    container = Canvas(root)

    frame = ttk.Frame(container, padding='3 3 12 12')
    frame.grid(column=0, row=0, sticky=(W, E, S, N))

    horizonscroll = Scrollbar(root)
    verticalscroll = Scrollbar(root)

    horizonscroll = Scrollbar(root)
    verticalscroll = Scrollbar(root)

    container.config(xscrollcommand=horizonscroll.set, yscrollcommand=verticalscroll.set, highlightthickness=3)
    horizonscroll.config(orient=HORIZONTAL, command=container.xview)
    verticalscroll.config(orient=VERTICAL, command=container.yview)

    horizonscroll.pack(fill=X, side=BOTTOM, expand=False)
    verticalscroll.pack(fill=Y, side=RIGHT, expand=False)
    container.pack(fill=BOTH, side=LEFT, expand=True)
    container.create_window(0, 0, window=frame, anchor=NW)

    Label(frame, text='ADD PRODUCT', font=30).grid(column=2, row=1, sticky=(W, E))

    Label(frame, text='Item:').grid(column=1, row=3, sticky=W)
    item = Entry(frame, width=18, borderwidth=3)
    item.grid(column=2, row=3, sticky=(W, E))

    Label(frame, text='Image Name:').grid(column=1, row=2, sticky=W)
    pic_path = Entry(frame, width=25, borderwidth=3)
    pic_path.grid(column=2, row=2, sticky=(W, E))

    Label(frame, text='Price:').grid(column=1, row=4, sticky=W)
    cost = Entry(frame, width=7, borderwidth=3)
    cost.grid(column=2, row=4, sticky=(W, E))

    Label(frame, text='Amount:').grid(column=1, row=5, sticky=W)
    amt = Entry(frame, width=10, borderwidth=3)
    amt.grid(column=2, row=5, sticky=(W, E))

    Label(frame, text='Description:').grid(column=1, row=6, sticky=W)
    des = Entry(frame, width=50, borderwidth=3)
    des.grid(columnspan=4, column=2, row=6, sticky=(W, E))

    Label(frame, text='').grid(column=2, row=11)
    Label(frame, text='REMOVE PRODUCT', font=30).grid(column=2, row=12, sticky=W)
    Label(frame, text='Item:').grid(column=1, row=13, sticky=W)
    deleted = Entry(frame, width=15, borderwidth=3)
    deleted.grid(column=2, row=13, sticky=(W, E))

    def done():
        name = item.get()
        path = pic_path.get()
        cos = cost.get()
        amo = amt.get()
        scribe = des.get()

        count = []

        if re.search(letter, name):
            na_me = name
            count.append(1)
        else:
            pass

        if re.search(letter, path):
            pa_th = path
            count.append(1)
        else:
            pass

        if re.search(letter, cos):
            cos_t = cos
            count.append(1)
        else:
            pass

        if re.search(letter, amo):
            amo_t = amo
            count.append(1)
        else:
            pass

        if re.search(letter, scribe):
            scr_ibe = scribe
            count.append(1)
        else:
            pass

        if len(count) == 5:
            curs.execute("INSERT INTO Inputs(path, name, price, amount, description) VALUES(?, ?, ?, ?, ?)",
                         (str(pa_th), str(na_me), str(cos_t), str(amo_t), str(scr_ibe)))
            con.commit()
            messagebox.showinfo('', 'Added')
            pic_path.delete(0, END)
            item.delete(0, END)
            cost.delete(0, END)
            amt.delete(0, END)
            des.delete(0, END)
        else:
            messagebox.showwarning('Error', 'Make sure all fields are filled')

    def close():
        message_box = messagebox.askquestion('', 'Exit?')
        if message_box == 'yes':
            root.destroy()
        else:
            pass

    def reset():
        message = messagebox.askquestion('', 'Reset all inputs?')
        if message == 'yes':
            pic_path.delete(0, END)
            item.delete(0, END)
            cost.delete(0, END)
            amt.delete(0, END)
            des.delete(0, END)
        else:
            pass

    def back():
        message = messagebox.askquestion('', 'Return to main page?')
        if message == 'yes':
            root.destroy()
            adminhome.home()
        else:
            pass

    def remove():
        out = deleted.get()

        if out == '':
            messagebox.showwarning('Error', 'You must input an item to delete \n to run this command')
            return

        message = messagebox.askquestion('', 'Remove this product?')
        if message == 'yes':
            del_out = out
            curs.execute("DELETE FROM Inputs WHERE name = '%s'" % str(del_out))
            con.commit()
            deleted.delete(0, END)
        else:
            pass

    def res():
        message = messagebox.askquestion('', 'Reset inputs?')
        if message == 'yes':
            deleted.delete(0, END)
        else:
            pass

    Button(frame, text='Reset', width=10, borderwidth=3, command=reset).grid(column=3, row=10, sticky=(W, E))
    Button(frame, text='Add', width=10, borderwidth=3, command=done).grid(column=4, row=10)
    Button(frame, text='Reset', width=10, borderwidth=3, command=res).grid(column=2, row=14, sticky=E)
    Button(frame, text='Remove', width=10, borderwidth=3, command=remove).grid(column=3, row=14)
    Label(frame, text='      ').grid(column=2, row=15)
    Button(frame, text='Home', width=10, borderwidth=3, command=back).grid(column=3, row=16, sticky=(W, E))
    Button(frame, text='Close', width=10, borderwidth=3, command=close).grid(column=4, row=16, sticky=(W, E))

    container.update_idletasks()
    container.config(scrollregion=frame.bbox())

    root.mainloop()


#Creates a window where the admin can take out customers from the database
def approve():
    root = Tk()

    root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))

    container = Canvas(root)

    frame = ttk.Frame(container, padding='3 3 12 12')
    frame.grid(column=0, row=0, sticky=(W, E, S, N))

    horizonscroll = Scrollbar(root)
    verticalscroll = Scrollbar(root)

    horizonscroll = Scrollbar(root)
    verticalscroll = Scrollbar(root)

    container.config(xscrollcommand=horizonscroll.set, yscrollcommand=verticalscroll.set, highlightthickness=3)
    horizonscroll.config(orient=HORIZONTAL, command=container.xview)
    verticalscroll.config(orient=VERTICAL, command=container.yview)

    horizonscroll.pack(fill=X, side=BOTTOM, expand=False)
    verticalscroll.pack(fill=Y, side=RIGHT, expand=False)
    container.pack(fill=BOTH, side=LEFT, expand=True)
    container.create_window(0, 0, window=frame, anchor=NW)

    Label(frame, text='CUSTOMERS', font=30).grid(column=1, row=1, sticky=W)
    Label(frame, text='            ', font=30).grid(column=2, row=1, sticky=W)
    Label(frame, text='EMAIL ADDRESSES', font=30).grid(column=3, row=1, sticky=E)
    Label(frame, text='            ', font=30).grid(column=4, row=1, sticky=W)
    Label(frame, text='USERNAMES', font=30).grid(column=5, row=1, sticky=E)

    get = cur.execute("SELECT Firstname FROM Customer")
    ach = cur.fetchall()
    get2 = cur.execute("SELECT Lastname FROM Customer")
    ach2 = cur.fetchall()
    get3 = cur.execute("SELECT Email FROM Customer")
    ach3 = cur.fetchall()
    get4 = cur.execute("SELECT Username FROM Customer")
    ach4 = cur.fetchall()

    f_names = []
    l_names = []
    address = []
    user_names = []

    for i in ach:
        f_names.append(list(i))

    for x in ach2:
        l_names.append(list(x))

    for r in ach3:
        address.append(list(r))

    for p in ach4:
        user_names.append(list(p))

    rew = 0

    for i in f_names:
        index = f_names.index(i)

        for item in f_names[index]:
            name1 = item

        for item in l_names[index]:
            name2 = item

        fullname = name1 + ' ' + name2

        Label(frame, text=fullname).grid(column=1, row=rew + 2, sticky=W)
        Label(frame, text='       ').grid(column=2, row=rew + 2, sticky=(W, E))
        Label(frame, text=address[index]).grid(column=3, row=rew + 2, sticky=W)
        Label(frame, text='       ').grid(column=4, row=rew + 2, sticky=(W, E))
        Label(frame, text=user_names[index]).grid(column=5, row=rew + 2, sticky=(W, E))
        last = Label(frame, text='       ')
        last.grid(column=1, row=rew + 3, sticky=W)

        container.update_idletasks()
        container.config(scrollregion=frame.bbox())

        info = last.grid_info()
        ref = info['row']
        rew += ref

    Label(frame, text='REMOVE CUSTOMER', font=20).grid(column=2, row=rew + 2, sticky=(W, E))
    Label(frame, text='Customer\'s Username').grid(column=1, row=rew + 3, sticky=(W, E))
    out_entry = Entry(frame, width=20, borderwidth=3)
    out_entry.grid(column=2, row=rew + 3, sticky=(W, E))

    def remove():
        out = out_entry.get()

        if out == '':
            messagebox.showwarning('Error', 'You must input an item to delete \n to run this command')
            return

        message = messagebox.askquestion('', 'Remove this Customer?')
        if message == 'yes':
            del_out = out
            cur.execute("DELETE FROM Customer WHERE Username= '%s'" % str(del_out))
            conn.commit()
            root.destroy()
            approve()
            out_entry.delete(0, END)
        else:
            pass

    def closed():
        message_box = messagebox.askquestion('', 'Exit?')
        if message_box == 'yes':
            root.destroy()
        else:
            pass

    def reset():
        message = messagebox.askquestion('', 'Reset inputs?')
        if message == 'yes':
            out_entry.delete(0, END)
        else:
            pass

    def back():
        message = messagebox.askquestion('', 'Return to main page?')
        if message == 'yes':
            root.destroy()
            adminhome.home()
        else:
            pass

    Button(frame, text='Remove', width=10, borderwidth=3, command=remove).grid(column=3, row=rew + 4, sticky=W)
    Button(frame, text='Reset', width=10, borderwidth=3, command=reset).grid(column=2, row=rew + 4, sticky=E)
    Label(frame, text='           ').grid(column=2, row=rew + 5, sticky=(W, E))
    Button(frame, text='Home', width=10, borderwidth=3, command=back).grid(column=4, row=rew + 6, sticky=(W, E))
    Button(frame, text='Close', width=10, borderwidth=3, command=closed).grid(column=5, row=rew + 6, sticky=W)

    root.mainloop()

#Creates a page with all receipts and their details
def history():
    main = Tk()

    container = Canvas(main, bg='Grey')

    frame = Frame(container, bg='Grey')
    frame.grid(column=0, row=0, sticky=(W, E, S, N))

    horizonscroll = Scrollbar(main)
    verticalscroll = Scrollbar(main)

    horizonscroll = Scrollbar(main)
    verticalscroll = Scrollbar(main)

    container.config(xscrollcommand=horizonscroll.set, yscrollcommand=verticalscroll.set, highlightthickness=3)
    horizonscroll.config(orient=HORIZONTAL, command=container.xview)
    verticalscroll.config(orient=VERTICAL, command=container.yview)

    horizonscroll.pack(fill=X, side=BOTTOM, expand=False)
    verticalscroll.pack(fill=Y, side=RIGHT, expand=False)
    container.pack(fill=BOTH, side=LEFT, expand=True)
    container.create_window(0, 0, window=frame, anchor=NW)

    Label(frame, text='RECEIPT HISTORY').grid(column=4, row=1, sticky=(W, E))

    curs.execute("SELECT Number from Receipts")
    get = curs.fetchall()
    curs.execute("SELECT Day From Receipts")
    ach1 = curs.fetchall()
    curs.execute("SELECT Time FROM Receipts")
    ache = curs.fetchall()
    curs.execute("SELECT User FROM Receipts")
    ache3 = curs.fetchall()
    curs.execute("SELECT Admin FROM Receipts")
    ache4 = curs.fetchall()
    curs.execute("SELECT Items FROM Receipts")
    ache5 = curs.fetchall()
    curs.execute("SELECT Total FROM Receipts")
    ache6 = curs.fetchall()

    get1 = []
    ach = []
    ach2 = []
    ach3 = []
    ach4 = []
    ach5 = []
    ach6 = []

    for x in ache6:
        ach6.append(list(x))

    for p in ache5:
        ach5.append(list(p))

    for r in ache3:
        ach3.append(list(r))

    for i in ache4:
        ach4.append(list(i))

    for item in get:
        get1.append(list(item))

    for item in ach1:
        ach.append(list(item))

    for item in ache:
        ach2.append(list(item))

    rew = 1

    for item in get1:
        index = get1.index(item)

        for r in ach[index]:
            reget = r

        for x in ach5[index]:
            items = x

        for i in ach6[index]:
            total = '$' + i

        dat = reget, '/', ach2[index]

        Label(frame, text='Receipt No.', bg='Grey').grid(column=1, row=rew + 1)
        Label(frame, text=get1[index], bg='Grey').grid(column=2, row=rew + 1, sticky=W)
        Label(frame, text='Date/Time:', bg='Grey').grid(column=1, row=rew + 2)
        Label(frame, text=dat, bg='Grey').grid(column=2, row=rew + 2, sticky=W)
        Label(frame, text='Customer\'s Name:', bg='Grey').grid(column=1, row=rew + 3)
        Label(frame, text=ach3[index], bg='Grey').grid(column=2, row=rew + 3, sticky=W)
        Label(frame, text='Attended to by:', bg='Grey').grid(column=1, row=rew + 4, sticky=W)
        Label(frame, text=ach4[index], bg='Grey').grid(column=2, row=rew + 4, sticky=W)
        Label(frame, text='Items Purchased:', bg='Grey').grid(column=1, row=rew + 5, sticky=W)
        Label(frame, text=items, bg='Grey').grid(column=2, row=rew + 5, sticky=W)
        Label(frame, text='Receipt Total:', bg='Grey').grid(column=1, row=rew + 6, sticky=W)
        Label(frame, text=total, bg='Grey').grid(column=2, row=rew + 6, sticky=W)
        Label(frame, text='            ', bg='Grey').grid(column=2, row=rew + 7, sticky=W)
        last = Label(frame, text='           ', bg='Grey')
        last.grid(column=2, row=rew + 8, sticky=W)

        info = last.grid_info()
        iinfo = info['row']
        rew = iinfo

    def homee():
        message = messagebox.askquestion('', 'Do you want to return to the main screen?')
        if message == 'yes':
            main.destroy()
            adminhome.home()
        else:
            pass

    Button(frame, text='Home', width=10, borderwidth=3, command=homee).grid(column=4, row = rew + 2)

    container.update_idletasks()
    container.config(scrollregion=frame.bbox())

    main.mainloop()
