import random
from tkinter import *
from tkinter import messagebox

price = []
root = Tk()
root.title("Billing")
bg_color = 'sky blue'
root.geometry('1500x1000')
# Title--------------------------------------
title = Label(root, text='----------------Billing Software---------------', bg=bg_color, fg='black',font=('algerian', 25), relief=GROOVE, bd=12)
title.pack(fill=X)


# Customer Section-------------------------------------------
fc = LabelFrame(root, text='Customer Details', font=('algerian', 25), relief=GROOVE, bd=10, bg=bg_color, fg='yellow')
fc.place(x=0, y=70, relwidth=1)

name = Label(fc, text='Customer Name:', font=('times new romman', 25, 'bold'), bg=bg_color, fg='black')
name.grid(row=0, column=0, padx=10, pady=5)
name_txt = Entry(fc, width=20, font='arial 15 bold', relief=GROOVE,textvariable=name)
name_txt.grid(row=0, column=1, padx=10, pady=5)

num = Label(fc, text='Mobile No:', font=('times new romman', 25, 'bold'), bg=bg_color, fg='black')
num.grid(row=0, column=2, padx=10, pady=5)
num_txt = Entry(fc, width=20, font='arial 15 bold', relief=GROOVE,textvariable=num)
num_txt.grid(row=0, column=3, padx=10, pady=5)




# Bill Details-------------------------------
name = StringVar()
num = StringVar()
bno = StringVar()
item = StringVar()
Sno = StringVar()
rate = IntVar()
quantity = IntVar()
x = random.randint(4899 , 9999)
bno.set(str(x))


def welcome():
    txt.delete(1.0, END)
    txt.insert(END, "\t\t\t*****-----WELCOME-----*****")
    txt.insert(END, f"\n\nBill No:{bno.get()}")
    txt.insert(END,f"\n..........................................................................................................................................................................................")
    txt.insert(END, f"\n Customer Name:\t\t{name.get()}")
    txt.insert(END, f"\n Phone Number:\t\t{num.get()}")
    txt.insert(END, f"\n..........................................................................................................................................................................................")
    txt.insert(END, f"\nProduct\t\tSerial No.\t\tQuantity\t\tPrice")
    txt.insert(END, f"\n-----------\t\t-------------\t\t-----------\t\t-------")
    txt.configure(font='cambria 12')



# Func-----------------------------------------
def additem():
    m=rate.get()
    n=quantity.get()*m
    price.append(n)
    if item.get() == '':
        messagebox.showerror('Error','Enter product')
    else:
        txt.insert(END, f"\n{item.get()}\t\t{Sno.get()}\t\t{quantity.get()}\t\t{n}")
def bill():
    tx=txt.get(10.0,(10.0+float(len(price))))
    welcome()
    txt.insert(END,tx)
    txt.insert(END, f"\n.....................................................................")
    txt.insert(END,f"Total:\t{sum(price)}")
    txt.insert(END,f'........................................................................')




# Product Details------------------------
fp = LabelFrame(root, text='Enter Product Details', font=('algerian', 25), relief=GROOVE, bd=10, bg=bg_color,fg='yellow')
fp.place(x=0, y=180, width=500, height=550)

Iname = Label(fp, text='Product:', font=('times new romman', 25, 'bold'), bg=bg_color, fg='black')
Iname.grid(row=0, column=0, padx=10, pady=5)
Iname_txt = Entry(fp, width=20, font='arial 15 bold',textvariable=item)
Iname_txt.grid(row=0, column=1, padx=10, pady=5)

sno = Label(fp, text='Serial No:', font=('times new romman', 25, 'bold'), bg=bg_color, fg='black')
sno.grid(row=1, column=0, padx=10, pady=5)
sno_txt = Entry(fp, width=20, font='arial 15 bold',textvariable=Sno)
sno_txt.grid(row=1, column=1, padx=10, pady=5)

pri = Label(fp, text='Price:', font=('times new romman', 25, 'bold'), bg=bg_color, fg='black')
pri.grid(row=3, column=0, padx=10, pady=5)
pri_txt = Entry(fp, width=20, font='arial 15 bold',textvariable=rate)
pri_txt.grid(row=3, column=1, padx=10, pady=5)

q = Label(fp, text='Quantity:', font=('times new romman', 25, 'bold'), bg=bg_color, fg='black')
q.grid(row=2, column=0, padx=10, pady=5)
q_txt = Entry(fp, width=20, font='arial 15 bold',textvariable=quantity)
q_txt.grid(row=2, column=1, padx=10, pady=5)


# Buttons in the bill---------------
# Pop up window for Bill-------------------------------------------------------------------------------------
def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("600x900")
    Label(newWindow, text="Bill", font=('algerian', 25), bg="sky blue", fg="yellow", relief=GROOVE, bd=7).pack(fill=X)
    scrl = Scrollbar(newWindow, orient=VERTICAL)
    txt = Text(newWindow, yscrollcommand=scrl)
    scrl.pack(side=RIGHT, fill=Y)
    scrl.config(command=txt.yview)
    txt.delete(1.0, END)
    txt.insert(END, "\t\t\t*****-----WELCOME-----*****")
    txt.insert(END, f"\n\nBill No:{bno.get()}")
    txt.insert(END,f"\n..........................................................................................................................................................................................")
    txt.insert(END, f"\n Customer Name:\t\t{name.get()}")
    txt.insert(END, f"\n Phone Number:\t\t{num.get()}")
    txt.insert(END, f"\n..........................................................................................................................................................................................")
    txt.insert(END, f"\nProduct\t\tSerial No.\t\tQuantity\t\tPrice")
    txt.insert(END, f"\n-----------\t\t-------------\t\t-----------\t\t-------")
    txt.configure(font='cambria 12')
    txt.pack()



b1 = Button(fp, text='Add Item', font='arial 15 bold', bg='teal', width=12, height=2,command=additem)
b1.grid(row=4, column=0, padx=0, pady=15)

b2 = Button(fp, text='Clear', font='arial 15 bold', bg='teal', width=12, height=2)
b2.grid(row=5, column=0, padx=0, pady=15)

b3 = Button(fp, text='Exit', font='arial 15 bold', bg='teal', width=12, height=2)
b3.grid(row=6, column=0, padx=0, pady=15)

b4 = Button(fp, text='Generate Bill', font='arial 15 bold', bg='teal', width=12, height=2, command=openNewWindow)
b4.grid(row=6, column=1, padx=0, pady=15)

# Billing Area-------------------
fb = Frame(root, relief=GROOVE, bd=10)
fb.place(x=550, y=180, width=600, height=550)

title = Label(fb, text="INvoice", font=('algerian', 25), bg="sky blue", fg="yellow", relief=GROOVE, bd=7).pack(fill=X)
scrl = Scrollbar(fb, orient=VERTICAL)
txt = Text(fb,yscrollcommand=scrl)
scrl.pack(side=RIGHT, fill=Y)
scrl.config(command=txt.yview)
txt.pack()
#cust()we
welcome()

# Payement Method------------------------
fpay = LabelFrame(root, text='Payment Method', font=('algerian', 15), relief=GROOVE, bd=10, bg='sky blue', fg='yellow')
fpay.place(x=1200,y=180, width=250, height=550)

b1 = Button(fpay, text='CASH', font='arial 20 bold', bg='white', relief=GROOVE, width=10)
b1.grid(row=0, column=0, padx=10, pady=15)

b2 = Button(fpay, text='CARD', font='arial 20 bold', bg='white', relief=GROOVE, width=10)
b2.grid(row=2, column=0, padx=10, pady=15)

b3 = Button(fpay, text='UPI', font='arial 20 bold', bg='white', relief=GROOVE, width=10)
b3.grid(row=4, column=0, padx=10, pady=15)

b4 = Button(fpay, text='NET Banking', font='arial 20 bold', bg='white', relief=GROOVE, width=10)
b4.grid(row=6, column=0, padx=10, pady=15)

root.mainloop()


