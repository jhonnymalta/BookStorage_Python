import  tkinter as tk

from tkinter import *


def register():
    file = open(f'{title_value.get()}.txt', 'w')
    file.write(f"The Book {title_value.get()} Launched in {date_value.get()} by the publisher {publish_value.get()} is priced at {price_value.get()} \n")
    file.close()

    Label(text="Registration success",fg="green",font=("calibri",11)).place(x=30,y=450)
    title_value.set("")
    date_value.set("")
    publish_value.set("")
    price_value.set(0.0)


root=Tk()
root.title("Book Storage")
root.geometry("300x500")
root.resizable(False,False)


Label(root,text="Register a new book", font="arial 20").pack(pady=50)


Label(text="Title",font=20).place(x=15,y=150)
Label(text="publisher",font=20).place(x=15,y=200)
Label(text="Year",font=20).place(x=15,y=250)
Label(text="Price",font=20).place(x=15,y=300)

#entry
title_value=StringVar()
publish_value=StringVar()
date_value=StringVar()
price_value=DoubleVar()

title_entry = Entry(root,textvariable=title_value,width=20,bd=1,font=18)
publish_entry = Entry(root,textvariable=publish_value,width=20,bd=1,font=18)
date_entry = Entry(root,textvariable=date_value,width=20,bd=1,font=18)
price_entry = Entry(root,textvariable=price_value,width=20,bd=1,font=18)

title_entry.place(x=110,y=150)
publish_entry.place(x=110,y=200)
date_entry.place(x=110,y=250)
price_entry.place(x=110,y=300)


Button(text="SALVAR",font=12,width=30,height=2,command=register).place(x=10,y=370)



root.mainloop()
