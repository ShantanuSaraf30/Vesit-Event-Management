import tkinter as tk
from tkinter import ttk
from subprocess import call

# Create the main window
root = tk.Tk()
root.title("Room Request")
root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.configure(bg="powder blue")
# Create the labels and entry fields for the form
label_title = tk.Label(root, text="Room Request", font="impack 20 bold", fg='black', bg='powder blue')
label_title.pack(pady=10)

# create a label for the name
name_label = tk.Label(root, text='Council Name:',font=('arial',16,'bold'),fg='black',bg='powder blue')
name_label.pack(pady=10)

# create a dropdown for the name
name_combo = ttk.Combobox(root, values=('SoRT', 'Cultural', 'Sports','Music','ISTE','CSI','IEEE','ISA'))
name_combo.pack(pady=10)

# create a label for the email
email_label = tk.Label(root, text='Event Name:',font=('arial',16,'bold'),fg='black',bg='powder blue')
email_label.pack(pady=10)
entry_email = tk.Entry(root)
entry_email.pack(pady=10)

def submit_form():

    name = name_combo.get()
    email = entry_email.get()
    print(f"Council name: {name}\nEvent name: {email}")
def select():
    call(['python','roombook1.py'])


# create a button to submit the registration form
submit_button = tk.Button(root, text='Submit',font=('arial',16,'bold'), command=select,fg='white',width=20,bg='navy blue')
submit_button.pack(pady=10)

root.mainloop()

