from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time
from subprocess import call

#connecting to other file
def open_py_file():
    call(["python","Council window.py"])
#connecting to the database
db = mysql.connector.connect(host="127.0.0.1",user="root",passwd="Shan@2003",database="miniproject")
mycur = db.cursor()


def login():
    
    global root2
    root2 = Tk()
    logo_img = PhotoImage(file="login.png")
    logo_widget = Label(root2, image=logo_img, bg=root2.cget("bg"), bd=0)
    logo_widget.image = logo_img
    logo_widget.place(x=0, y=0, relwidth=1, relheight=1)


    root2.title("Log-In Portal")
    root2.geometry("1800x1800")
    root2.configure(bg="#a2d2ff")
    global username_varify
    global password_varify
    Label(root2, text="",bg="#8a83e5").pack()
    Label(root2, text="",bg="#8a83e5").pack()
    Label(root2, text="",bg="#8a83e5").pack()
    Label(root2, text="Log-In Portal", bg="white", fg="black", font=("bold", 30),width=10).pack()
    username_varify = StringVar()
    password_varify = StringVar()
    
 
    Label(root2, text="",bg='#020546').pack()
    Label(root2, text="",bg='#020546').pack()
    Label(root2, text="",bg='#020546').pack()
    Label(root2, text="",bg='#020546').pack()

    Label(root2, text="",bg='#020546').pack()
    
    Label(root2, text="Username :", font="Arial 20 bold",fg="white",bg='#020546').pack()
    Entry(root2,width= 30, textvariable=username_varify).pack()
    Label(root2, text="",bg='#020546').pack()
    Label(root2, text="",bg='#020546').pack()
    Label(root2, text="Password :", font="Arial 20 bold",fg="white",bg='#020546').pack()
    Entry(root2,width= 30, textvariable=password_varify, show="*").pack()
    Label(root2, text="",bg='#020546').pack()
    
    Button(root2, text="\nLog-In\n",width=15,fg="white",font="Arial 10 bold",bg='navy blue',command=login_varify).pack()
    Label(root2, text="")



def fail_destroy():
    fail.destroy()

def logged():
    open_py_file()
def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x100")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()


def login_varify():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    sql = "select * from login where loginid = %s and password = %s"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            logged()
            break
    if user_varify=='HOD':
        if pas_varify=='1234':
            hod()
    else:
        failed()
def hod():
    call(["python","roomallocation.py"])


def main_screen():
    global root
    login()
   
   


main_screen()
root2.mainloop()
