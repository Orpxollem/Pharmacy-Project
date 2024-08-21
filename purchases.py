from tkinter import *
import cesspool
from time import ctime
import database
import IDdatabase


curr = IDdatabase.curs
conn = IDdatabase.con
con = database.connect
curs = database.cursor

#Provides a receipt based on items in the cart
def payment():
    main = Tk()
    main.title("Check_Out")

    main.geometry('{0}x{1}+0+0'.format(main.winfo_screenwidth(), main.winfo_screenheight()))

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

    curs.execute("SELECT Number FROM Receipts")
    acch1 = curs.fetchone()
    #Gets the name of the current customer logged in.
    curs.execute("SELECT Name FROM Logins")
    acch2 = curs.fetchone()
    #Gets the email address of the current customer logged in
    curs.execute("SELECT Email FROM Logins")
    acch4 = curs.fetchone()

    count = 0

    for item in acch2:
        name1 = ''.join(item)

    for item in acch4:
        mail = ''.join(item)

    for item in acch1:
        for x in item:
            receipt = ''.join(x)

    ach1 = curs.execute("SELECT Item FROM Cart")
    ache1 = curs.fetchall()
    ach2 = curs.execute("SELECT Amount FROM Cart")
    ache2 = curs.fetchall()
    ach3 = curs.execute("SELECT Price FROM Cart")
    ache3 = curs.fetchall()


    product = []
    amount = []
    cost = []

    for item in ache1:
        product.append(list(item))

    for item in ache2:
        amount.append(list(item))

    for item in ache3:
        cost.append(list(item))


    receipt_no = 'RECEIPT No.' + '' + receipt

    day = ctime().split()[0]

    date = ctime().split()[2]

    month = ctime().split()[1]

    year = ctime().split()[4]

    minute = ctime().split()[3]

    ti = day + ' ' + date + ' ' + month + ' ' + year

    Label(frame, text='                  ', bg='Grey').grid(column=1, row=1, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=1, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=3, row=1, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=4, row=1, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=5, row=1, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=7, row=1, sticky=W)
    Label(frame, text='RECEIPT', font="'Bold', 50", bg='Grey').grid(column=8, row=1, sticky=(W, E))
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=2, sticky=(W, E))

    Label(frame, text='                  ', bg='Grey').grid(column=1, row=3, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=3, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=3, row=3, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=4, row=3, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=5, row=3, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=7, row=3, sticky=W)
    Label(frame, text='PHARMACY', font="Italic, 20", bg='Grey').grid(column=8, row=3, sticky=(W, E))
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=4, sticky=(W, E))

    Label(frame, text='                  ', bg='Grey').grid(column=1, row=5, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=5, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=3, row=5, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=4, row=5, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=5, row=5, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=7, row=5, sticky=W)
    Label(frame, text=ti, font=15, bg='Grey').grid(column=8, row=5, sticky=(W, E))
    Label(frame, text=minute, font=15, bg='Grey').grid(column=8, row=6, sticky=(W, E))

    Label(frame, text='                  ', bg='Grey').grid(column=1, row=7, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=7, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=3, row=7, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=4, row=7, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=5, row=7, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=7, row=7, sticky=W)
    Label(frame, text='PHONE : xxx - xxx - xxx', font=12, bg='Grey').grid(column=8, row=7, sticky=(W, E))
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=8, sticky=(W, E))

    Label(frame, text='                  ', bg='Grey').grid(column=1, row=9, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=9, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=3, row=9, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=4, row=9, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=5, row=9, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=7, row=9, sticky=W)
    Label(frame, text='pharmacy@gmail.com',font=5, bg='Grey').grid(column=8, row=9, sticky=(W, E))
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=9, sticky=(W, E))

    Label(frame, text='                  ', bg='Grey').grid(column=1, row=11, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=11, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=3, row=11, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=4, row=11, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=5, row=11, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=7, row=11, sticky=W)
    Label(frame, text=receipt_no, font=10, bg='Grey').grid(column=8, row=11, sticky=(W, E))
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=12, sticky=(W, E))

    Label(frame, text='                  ', bg='Grey').grid(column=1, row=13, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=13, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=3, row=13, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=4, row=13, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=5, row=13, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=7, row=13, sticky=W)
    Label(frame, text='Online Purchase', font=10, bg='Grey').grid(column=8, row=13, sticky=(W, E))
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=14, sticky=(W, E))

    Label(frame, text='=======================================', bg='Grey').grid(column=8, row=15, sticky=E)
    Label(frame, text='=================', bg='Grey').grid(column=9, row=15, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=17, sticky=E)

    Label(frame, text='AMOUNT', bg='Grey').grid(column=8, row=18, sticky=W)
    Label(frame, text='ITEMS', bg='Grey').grid(column=8, row=18)
    Label(frame, text='PRICE', bg='Grey').grid(column=9, row=18, sticky=W)
    Label(frame, text='           ', bg='Grey').grid(column=2, row=19, sticky=(W, E))

    rew = 19
    f_total = 0

    for item in product:

        index = product.index(item)

        for x in cost[index]:
            am_total = int(x)
            price = '$' + x

        for i in amount[index]:
            cos_total = int(i)

        f = am_total * cos_total
        f_total += f
        total = '$' + str(f_total)

        Label(frame, text=product[index], bg='Grey').grid(column=8, row=rew + 1)
        Label(frame, text=amount[index], bg='Grey').grid(column=8, row=rew + 1, stick=W)
        final = Label(frame, text=price, bg='Grey')
        final.grid(column=9, row=rew + 1, sticky=W)

        info = final.grid_info()
        get = info['row']
        rew = get

    Label(frame, text='TOTAL = ', bg='Grey').grid(column=8, row=rew + 1, sticky=E)
    Label(frame, text=total, bg='Grey').grid(column=9, row=rew + 1, sticky=W)
    Label(frame, text='PAYMENT METHOD = ', bg='Grey').grid(column=8, row=rew + 2, sticky=E)
    Label(frame, text='CARD', bg='Grey').grid(column=9, row=rew + 2, sticky=W)
    Label(frame, text='                  ', bg='Grey').grid(column=2, row=rew + 3)
    Label(frame, text='=======================================', bg='Grey').grid(column=8, row=rew + 4, sticky=E)
    Label(frame, text='=================', bg='Grey').grid(column=9, row=rew + 4, sticky=W)

    Label(frame, text="CUSTOMER'S NAME:", bg='Grey').grid(column=8, row=rew + 5, sticky=W)
    Label(frame, text=name1, bg='Grey').grid(column=8, row=rew + 5, sticky=E)
    Label(frame, text="    EMAIL:", bg='Grey').grid(column=8, row=rew + 6, sticky=W)
    Label(frame, text=mail, bg='Grey').grid(column=8, row=rew + 6, sticky=E)
    Label(frame, text="ATTENDED TO BY:", bg='Grey').grid(column=8, row=rew + 7, sticky=W)
    Label(frame, text='Jonathan Tsekpo', bg='Grey').grid(column=8, row=rew + 7)

    container.update_idletasks()
    container.config(scrollregion=frame.bbox())

    main.mainloop()
