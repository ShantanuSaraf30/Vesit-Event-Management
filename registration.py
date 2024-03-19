import tkinter as tk
import mysql.connector
from tkinter import messagebox
import os
import time
import re
from subprocess import call
#connecting to the database
db = mysql.connector.connect(host="127.0.0.1",user="root",passwd="Shan@2003",database="miniproject")
mycur = db.cursor()
# Create the main window
root = tk.Tk()
root.title("Registration Page")
root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.configure(bg="powder blue")


# Create the labels and entry fields for the form
label_title = tk.Label(root, text="Registration Page", font="impack 20 bold", fg='black', bg='powder blue')


logo_img = tk.PhotoImage(file="reg.png")
logo_widget = tk.Label(root, image=logo_img, bg=root.cget("bg"), bd=0)
logo_widget.image = logo_img
logo_widget.place(x=0, y=0, relwidth=1, relheight=1)
label_event_name = tk.Label(root, text="",fg='black',bg='#020546').pack()
label_event_name = tk.Label(root, text="",fg='black',bg='#020546').pack()
label_event_name = tk.Label(root, text="",fg='black',bg='#020546').pack()
label_event_name = tk.Label(root, text="",fg='black',bg='#020546').pack()
label_event_name = tk.Label(root, text="",fg='black',bg='#020546').pack()
label_event_name = tk.Label(root, text="",fg='black',bg='#020546').pack()
 
label_event_name = tk.Label(root, text="Event Name",font=('arial',16,'bold'),fg='white',bg='#020546')
entry_event_name = tk.Entry(root)
label_username = tk.Label(root, text="Name",font=('arial',16,'bold'),fg='white',bg='#020546')
entry_username = tk.Entry(root)
label_div = tk.Label(root, text="Class",font=('arial',16,'bold'),fg='white',bg='#020546')
entry_div = tk.Entry(root)
label_roll = tk.Label(root, text="Roll No.",font=('arial',16,'bold'),fg='white',bg='#020546')
entry_roll = tk.Entry(root)
label_phone = tk.Label(root, text="Phone No.",font=('arial',16,'bold'),fg='white',bg='#020546')
entry_phone = tk.Entry(root)
label_email = tk.Label(root, text="Email ID",font=('arial',16,'bold'),fg='white',bg='#020546')
entry_email = tk.Entry(root)


# Pack the labels and entry fields vertically with padding
label_title.pack(pady=10)
label_event_name.pack(pady=10)
entry_event_name.pack()
label_username.pack(pady=10)
entry_username.pack()
label_div.pack(pady=10)
entry_div.pack()
label_roll.pack(pady=10)
entry_roll.pack()
label_phone.pack(pady=10)
entry_phone.pack()
label_email.pack(pady=10)
entry_email.pack()

# Define a function to submit the form
def fail_destroy():
    fail.destroy()
def validate_email(email):  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return True  
    return False  
def submit_form():

    event_name = entry_event_name.get()
    username = entry_username.get()
    div = entry_div.get()
    roll = entry_roll.get()
    phone = entry_phone.get()
    email = entry_email.get()
    r=re.fullmatch('[6-9][0-9]{9}',phone) 
    if r!=None:
        if validate_email(email):
            sql = "insert into registration values(%s,%s,%s,%s,%s,%s)"
            t = (event_name,username,div,roll,phone,email)
            mycur.execute(sql, t)
            db.commit()
            success()
        else:
            global fail
            fail=tk.Tk()
            fail.title("Invalid")
            fail.geometry("200x100")
            a=tk.Label(fail, text="Invalid Email...", fg="red", font="bold").pack()
            a=tk.Label(fail, text="").pack()
            Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()
    else:
       
        fail=tk.Tk()
        fail.title("Invalid")
        fail.geometry("200x100")
        a=tk.Label(fail, text="Invalid Phone NO...", fg="red", font="bold").pack()
        a=tk.Label(fail, text="").pack()
        Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()
        
def success():
    global succ
    succ=tk.Tk()
    succ.title("Success")
    
    succ.geometry("1800x1800")
    h1=tk.Label(succ, text="Registration successful...", fg="green", font="bold")
    h1.pack()
    my_button1 = tk.Button(succ, text="Home",command=home)
    my_button1.config(width=20, height=3, bg="#caf0f8")
    my_button1.pack(side='top',pady=10)
def home():
    call(["python","homefinal.py"])

    

# Create a submit button
button_submit = tk.Button(root, text="Submit",font=('arial',16,'bold'), command=submit_form,fg='white',width=20,bg='navy blue')
button_submit.pack(pady=20)

# Start the main event loop
root.mainloop()
