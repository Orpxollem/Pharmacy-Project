from tkinter import *
from tkinter import ttk
import database
from PIL import ImageTk, Image
from tkinter import messagebox
import customerpage
import random
from time import ctime
import purchases


con = database.connect
curs = database.cursor


def shop():
    rots = Tk()
    rots.title('Shop')

    container = Canvas(rots, width=1200, height=700)

    frame = ttk.Frame(container, padding='3 3 12 12')
    frame.grid(column=0, row=0, sticky=(W, E, S, N))
    #canvas = Canvas(frame, width=800, height=500)

    #Adds scroll bars to the window

    horizonscroll = Scrollbar(rots)
    verticalscroll = Scrollbar(rots)

    horizonscroll = Scrollbar(rots)
    verticalscroll = Scrollbar(rots)

    container.config(xscrollcommand=horizonscroll.set, yscrollcommand=verticalscroll.set, highlightthickness=3)
    horizonscroll.config(orient=HORIZONTAL, command=container.xview)
    verticalscroll.config(orient=VERTICAL, command=container.yview)

    horizonscroll.pack(fill=X, side=BOTTOM, expand=False)
    verticalscroll.pack(fill=Y, side=RIGHT, expand=False)
    container.pack(fill=BOTH, side=LEFT, expand=True)
    container.create_window(0, 0, window=frame, anchor=NW)

    ach1 = curs.execute("SELECT path FROM Inputs")
    ache1 = curs.fetchall()
    ach2 = curs.execute("SELECT name FROM Inputs")
    ache2 = curs.fetchall()
    ach3 = curs.execute("SELECT price FROM Inputs")
    ache3 = curs.fetchall()
    ach4 = curs.execute("SELECT amount FROM Inputs")
    ache4 = curs.fetchall()
    ach5 = curs.execute("SELECT description FROM Inputs")
    ache5 = curs.fetchall()

    get = []
    get1 = []
    et1 = []
    get2 = []
    get3 = []
    get4 = []
    get5 = []
    var = []

    count = 0

    for item in ache1:
        count += 1
        get1.append(list(item))
        #Creates a list of varaible which all have the set of numbers but end with different numbers.
        var.append('img' + str(count))

    # Directs user to the cart where the user can check for items he has currently placed in his cart
    def cartitem():
        rots.destroy()
        cart()

    for item in ache2:
        get2.append(item)

    for item in ache3:
        get3.append(item)

    for item in ache4:
        get4.append(item)

    for item in ache5:
        get5.append(item)

    Label(frame, text='SHOP', font=50).grid(column=1, row=1)
    Button(frame, text='Cart', font=20, width=10, borderwidth=3, command=cartitem).grid(column=2, row=1)

    rew = 1

    #This function gets the product name, selected quantity to be bought and price of the product and inserts it into a database
    def add_item(a, s, d):
        d = d.get()
        curs.execute("INSERT INTO Cart(Item, Amount, Price) VALUES(?, ?, ?)", (str(a), str(d), str(s)))
        con.commit()

    for item in get1:

        index = get1.index(item)

        for x in get4[index]:
            reason = int(x) + 1

        box_item = []

        for r_item in range(1, reason):
            boxed = str(r_item)
            box_item.append(boxed)

        for i in get1[index]:
            pic = i

        canvas = Canvas(frame, width=100, height=100)
        canvas.grid(column=1, row=rew + 1)

        '''The below variable is based on variables obtained from a list because with if the variable doesn't change, only the
         last object of the loop with get an image. But with constantly changing variables all images will be placed correctly'''
        var[index] = ImageTk.PhotoImage(Image.open(pic))
        canvas.create_image(20, 50, anchor=W, image=var[index])

        Label(frame, text='Item:', font=10).grid(column=1, row=rew + 2, sticky=(W, E))
        qad1 = Label(frame, text=get2[index])
        qad1.grid(column=2, row=rew + 2, sticky= W)
        Label(frame, text='Price:', font=10).grid(column=1, row=rew + 3, sticky=(W, E))
        qad2 = Label(frame, text=get3[index])
        qad2.grid(column=2, row=rew + 3, sticky=W)
        hert = qad1['text']
        hert2 = qad2['text']

        number = ttk.Combobox(frame, width=4, values=box_item)
        number.grid(column=2, row=rew + 5, sticky=W)
        number.set('1')

        Label(frame, text='Quantity:', font=10).grid(column=1, row=rew + 5)
        Label(frame, text='Description:', font=10).grid(column=1, row=rew + 7)
        last = Label(frame, text=get5[index])
        last.grid(column=2, row=rew + 8, sticky=W)
        Label(frame, text='          ').grid(column=1, row=rew + 9, sticky=(W, E))

        b = Button(frame, text='+Add to Cart')
        b.config(command=lambda num1=hert, num2=hert2, num3=number: add_item(num1, num2, num3))
        b.grid(column=2, row=rew + 6, sticky=W)

        '''Gets the last row number and reassigns *rew(which is serving as the current row number) so items can be
        added to the window in a loop without having to add items to the window individually'''

        info = last.grid_info()
        ref = info['row']
        rew = ref

    def back():
        message = messagebox.askquestion('', 'Do you want to Sign Out?')
        if message == 'yes':
            #Clears the details in the login database because when the user sign outs no user is in the system.
            curs.execute("DELETE FROM Logins")
            con.commit()
            rots.destroy()
            customerpage.customer_login()
        else:
            pass

    def closed():
        message_box = messagebox.askquestion('', 'Exit?')
        if message_box == 'yes':
            rots.destroy()
        else:
            pass

    Label(frame, text='       ').grid(column=2, row=rew + 1)
    Button(frame, text='Close', font=20, width=10, borderwidth=3, command=closed).grid(column=7, row=rew + 2)
    Button(frame, text='Sign Out', font=20, width=10, borderwidth=3, command=back).grid(column=6, row=rew + 2)

    #Actives scrollbar and causes it to adjust with all window items
    container.update_idletasks()
    container.config(scrollregion=frame.bbox())

    rots.mainloop()


#Cart Window

def cart():
    top = Tk()
    top.title('Cart')

    container = Canvas(top, width=800, height=450)

    frame = ttk.Frame(container, padding='3 3 12 12')
    frame.grid(column=0, row=0, sticky=(W, E, S, N))


    horizonscroll = Scrollbar(top)
    verticalscroll = Scrollbar(top)

    horizonscroll = Scrollbar(top)
    verticalscroll = Scrollbar(top)

    container.config(xscrollcommand=horizonscroll.set, yscrollcommand=verticalscroll.set, highlightthickness=3)
    horizonscroll.config(orient=HORIZONTAL, command=container.xview)
    verticalscroll.config(orient=VERTICAL, command=container.yview)

    horizonscroll.pack(fill=X, side=BOTTOM, expand=False)
    verticalscroll.pack(fill=Y, side=RIGHT, expand=False)
    container.pack(fill=BOTH, side=LEFT, expand=True)
    container.create_window(0, 0, window=frame, anchor=NW)

    day = ctime().split()[0]

    date = ctime().split()[2]

    month = ctime().split()[1]

    year = ctime().split()[4]

    minute = ctime().split()[3]

    ti = day + ' ' + date + ' ' + month + ' ' + year

    digits = "0123456789"

    numbers = True

    al = ''

    if numbers:
        al += digits

    length = 5

    #Generates 5 random numbers
    receipt = "".join(random.sample(al, length))

    Label(frame, text='Items', font=20).grid(column=1, row=2, sticky=(W, E))
    Label(frame, text='      ').grid(column=2, row=2, sticky=(W, E))
    Label(frame, text='Quantity', font=20).grid(column=3, row=2, sticky=(W, E))
    Label(frame, text='      ').grid(column=4, row=2, sticky=(W, E))
    Label(frame, text='Price per Item', font=20).grid(column=5, row=2, sticky=(W, E))

    ach1 = curs.execute("SELECT Item FROM Cart")
    ache1 = curs.fetchall()
    ach2 = curs.execute("SELECT Amount FROM Cart")
    ache2 = curs.fetchall()
    ach3 = curs.execute("SELECT Price FROM Cart")
    ache3 = curs.fetchall()
    curs.execute("SELECT Name FROM Logins")
    ach4 = curs.fetchone()

    products = []
    amount = []
    cost = []

    f_prod = []
    f_am = []
    f_cost = []

    for item in ach4:
        u_name = ''.join(item)

    for item in ache1:
        products.append(list(item))

    for item in ache2:
        amount.append(list(item))

    for item in ache3:
        cost.append(list(item))

    for item in products:
        for x in item:
            f_prod.append(x)

    for item in amount:
        for x in item:
            f_am.append(x)

    for item in cost:
        for x in item:
            f_cost.append(x)

    rew = 2

    for item in products:

        index = products.index(item)

        for x in cost[index]:
            price = '$' + x

        label = Label(frame, text=products[index])
        label.grid(column=1, row=rew + 1, sticky=(W, E))
        a = label['text']
        Label(frame, text=amount[index]).grid(column=3, row=rew + 1, sticky=(W, E))
        Label(frame, text=price).grid(column=5, row=rew + 1, sticky=(W, E))
        Button(frame, text='x', width=1, borderwidth=2, command=lambda out=a: itemout(out)).grid(column=6, row=rew + 1, sticky=W)
        lfinal = Label(frame, text='          ')
        lfinal.grid(column=1, row=rew + 2, sticky=(W, E))

        info = lfinal.grid_info()
        ref = info['row']
        rew = ref

    f_total = 0

    for item in amount:
        index = amount.index(item)

        for x in amount[index]:
            am_total = int(x)
            price = '$' + x

        for i in cost[index]:
            cos_total = int(i)

        f = am_total * cos_total
        f_total += f

    def itemout(outitem):
        curs.execute("DELETE FROM Cart WHERE Item= '%s'" % str(outitem))
        con.commit()
        top.destroy()
        cart()

    def back():
        top.destroy()
        shop()

    def buy():
        top.destroy()
        top2 = Tk()
        buy.variable = top2

        container = Canvas(top2)

        frame = ttk.Frame(container, padding='3 3 12 12')
        frame.grid(column=0, row=0, sticky=(W, E, S, N))

        horizonscroll = Scrollbar(top2)
        verticalscroll = Scrollbar(top2)

        horizonscroll = Scrollbar(top2)
        verticalscroll = Scrollbar(top2)

        container.config(xscrollcommand=horizonscroll.set, yscrollcommand=verticalscroll.set, highlightthickness=3)
        horizonscroll.config(orient=HORIZONTAL, command=container.xview)
        verticalscroll.config(orient=VERTICAL, command=container.yview)

        horizonscroll.pack(fill=X, side=BOTTOM, expand=False)
        verticalscroll.pack(fill=Y, side=RIGHT, expand=False)
        container.pack(fill=BOTH, side=LEFT, expand=True)
        container.create_window(0, 0, window=frame, anchor=NW)

        Label(frame, text=receipt, font=10).grid(column=4, row=2, sticky=(W, E))

        Label(frame, text='                  ').grid(column=1, row=1, sticky=W)
        Label(frame, text='                  ').grid(column=2, row=1, sticky=W)
        Label(frame, text='                  ').grid(column=3, row=1, sticky=W)
        Label(frame, text='Check Out', font=20).grid(column=4, row=1, sticky=(W, E))

        Label(frame, text='AMOUNT', font=15).grid(column=4, row=3, sticky=(W, E))
        Label(frame, text='ITEMS', font=15).grid(column=3, row=3, sticky=W)
        Label(frame, text='PRICE', font=15).grid(column=5, row=3, sticky=(W, E))

        rews = 6
        ff_total = 0

        for items in products:
            indexd = products.index(items)

            for rf in cost[indexd]:
                am_totals = int(rf)
                prices = '$' + rf

            for rp in cost[indexd]:
                cos_totals = int(rp)

            Label(frame, text=products[indexd], font=5).grid(column=3, row=rews + 1, sticky=(W, E))
            Label(frame, text=amount[indexd], font=5).grid(column=4, row=rews + 1, sticky=(W, E))
            final = Label(frame, text=prices, font=5)
            final.grid(column=5, row=rews + 1, sticky=(W, E))

            iinfo = final.grid_info()
            get = iinfo['row']
            rews = get

        def rert():
            top2.destroy()
            cart()

        def okay():
            message = messagebox.askquestion('', 'Buy Items?!')

            if message == 'yes':
                finalise()
                shop()
            else:
                pass

        Label(frame, text='TOTAL = ', font=10).grid(column=5, row=rews + 1, sticky=(W, E))
        Label(frame, text=total, font=10).grid(column=6, row=rews + 1, sticky=W)
        Label(frame, text='PAYMENT METHOD = ', font=10).grid(column=5, row=rews + 2, sticky=E)
        Label(frame, text='CARD', font=10).grid(column=6, row=rews + 2, sticky=W)
        Label(frame, text='                  ').grid(column=2, row=rews + 3)
        Button(frame, text='BUY', font=20, width=5, command=okay).grid(column=6, row=rews + 4)
        Button(frame, text='CART', font=20, width=5, command=rert).grid(column=5, row=rews + 4, sticky=E)

        container.update_idletasks()
        container.config(scrollregion=frame.bbox())

        top2.mainloop()

    def purdone():
        messagebox.showinfo('', 'Bought')
        buy.variable.destroy()
        purchases.payment()
        curs.execute("DELETE FROM Cart")
        con.commit()

    def finalise():
        if f_total <= 0:
            messagebox.showwarning('Error', 'There are no items in the cart to be purchased')
            return
        else:
            curs.execute("INSERT INTO Receipts(Number, Amounts, Items, Prices, Day, Time, Total, User, Admin) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (receipt, str(f_am), str(f_prod), str(f_cost), str(ti), str(minute), str(f_total), str(u_name), str('Jonathan Tsekpo')))
            con.commit()
            purdone()

    def closed():
        message_box = messagebox.askquestion('', 'Proceed To Checkout')
        if message_box == 'yes':
            top.destroy()
        else:
            pass

    total = '$' + str(f_total)

    Label(frame, text=total, font=15).grid(column=6, row=rew + 3, sticky=W)
    Label(frame, text='Final Total = ', font=15).grid(column=5, row=rew + 3, sticky=(W, E))
    Label(frame, text='          ').grid(column=2, row=rew + 4, sticky=(W, E))
    Button(frame, text='< Home', font=15, command=back).grid(column=1, row=1, sticky=E)
    Button(frame, text='Proceed To Checkout', font=15, command=buy).grid(column=6, row=rew + 5, sticky=(W, E))

    container.update_idletasks()
    container.config(scrollregion=frame.bbox())

    top.mainloop()
