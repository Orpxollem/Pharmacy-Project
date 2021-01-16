from tkinter import *
from PIL import Image, ImageTk
import adminpage
import customerpage
import createaccount

#The main page of the program where users either select to log in as admins, customers or create a customer's account


def homepage():
    try:
        roots = Tk()
        roots.title('ID Selection')

        img = ImageTk.PhotoImage(Image.open('Use.png'))
        canvas = Canvas(roots, width=500, height=300)
        canvas.pack()
        canvas.create_image(20, 20, anchor=NW, image=img)

        #Navigates to the admin section of the program
        def admin_toggle():
            try:
                roots.destroy()
                adminpage.admin_login()
            except:
                pass

        #Navigates to the customer section of the prgram
        def customer_toggle():
            roots.destroy()
            customerpage.customer_login()

        admin = Button(roots, text='Administrator Login', height=2, width=30, borderwidth=5,
                       command=admin_toggle).pack()
        customer = Button(roots, text='Customer Login', height=2, width=30, borderwidth=5,
                          command=customer_toggle).pack()

        #Navigates to the create customer account section of the program
        def create_toggle():
            roots.destroy()
            createaccount.window()

        Button(roots, text='Create An Account', height=2, width=30, borderwidth=5, command=create_toggle).pack()
        roots.mainloop()
    except:
        pass


homepage()
