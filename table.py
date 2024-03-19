import tkinter as tk

root = tk.Tk()
root.configure(bg="#a2d2ff")
root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))

# Create table headings
tk.Label(root, borderwidth=2, relief="solid",bg="#050347").grid(row=0, column=0, sticky="nsew")
tk.Label(root, text="1st Year", borderwidth=2, relief="solid", font="bold",bg="#050347",fg='white').grid(row=0, column=1, sticky="nsew")
tk.Label(root, text="2nd Year", borderwidth=2, relief="solid", font=("bold"),bg="#050347",fg='white').grid(row=0, column=2, sticky="nsew")
tk.Label(root, text="3rd Year", borderwidth=2, relief="solid", font="bold",bg="#050347",fg='white').grid(row=0, column=3, sticky="nsew")
tk.Label(root, text="4th Year", borderwidth=2, relief="solid", font="bold",bg="#050347",fg='white').grid(row=0, column=4, sticky="nsew")

# Add data to the table
for i in range(1, 13):
 tk.Label(root, text="January", borderwidth=1, relief="solid", font="bold",bg="#050347",fg='white').grid(row=1, column=0, sticky="nsew")
 tk.Label(root, text="February", borderwidth=1, relief="solid", font="bold",bg="#050347",fg='white').grid(row=2, column=0, sticky="nsew")
 tk.Label(root, text="March", borderwidth=1, relief="solid", font="bold",bg="#050347",fg='white').grid(row=3, column=0, sticky="nsew")
 tk.Label(root, text="April", borderwidth=1, relief="solid", font="bold",bg="#050347",fg='white').grid(row=4, column=0, sticky="nsew")
 tk.Label(root, text="May", borderwidth=1, relief="solid", font="bold",bg="#050347",fg='white').grid(row=5, column=0, sticky="nsew")
 tk.Label(root, text="June", borderwidth=1, relief="solid", font="bold",bg="#050347",fg='white').grid(row=6, column=0, sticky="nsew")
 tk.Label(root, text="July", borderwidth=1, relief="solid", font="bold",bg="#050347",fg='white').grid(row=7, column=0, sticky="nsew")
 tk.Label(root, text="August", borderwidth=1, relief="solid", font="bold",bg="#050347",fg='white').grid(row=8, column=0, sticky="nsew")
 tk.Label(root, text="September", borderwidth=1, relief="solid", font="bold",bg="#050347",fg='white').grid(row=9, column=0, sticky="nsew")
 tk.Label(root, text="October", borderwidth=1, relief="solid",font="bold",bg="#050347",fg='white').grid(row=10, column=0, sticky="nsew")
 tk.Label(root, text="October", borderwidth=1, relief="solid",font="bold",bg="#050347",fg='white').grid(row=10, column=0, sticky="nsew")
 tk.Label(root, text="November", borderwidth=1, relief="solid",font="bold",bg="#050347",fg='white').grid(row=11, column=0, sticky="nsew")
 tk.Label(root, text="December", borderwidth=1, relief="solid",font="bold",bg="#050347",fg='white').grid(row=12, column=0, sticky="nsew")
 tk.Label(root, text="Prarambh\n Illusions\nVPL", borderwidth=1, relief="solid",bg='#FFB7B1').grid(row=1, column=1, sticky="nsew")
 tk.Label(root, text="Blood Donation Drive\nBeach Cleanup Drive\nBliss", borderwidth=1, relief="solid",bg='#FFB7B1').grid(row=2, column=1, sticky="nsew")
 tk.Label(root, text="Umeed\nUtsav\nSphurti\nPraxis\nOctaves", borderwidth=1, relief="solid",bg='#FFB7B1').grid(row=3, column=1, sticky="nsew")
 tk.Label(root, text="None", borderwidth=1, relief="solid",bg='#FFB7B1').grid(row=4, column=1, sticky="nsew")
 tk.Label(root, text="None", borderwidth=1, relief="solid",bg='#FFB7B1').grid(row=5, column=1, sticky="nsew")
 tk.Label(root, text="None", borderwidth=1, relief="solid",bg='#FFB7B1').grid(row=6, column=1, sticky="nsew")
 tk.Label(root, text="None", borderwidth=1, relief="solid",bg='#FFB7B1').grid(row=7, column=1, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#FFB7B1').grid(row=8, column=1, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#FFB7B1').grid(row=9, column=1, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#FFB7B1').grid(row=10, column=1, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#FFB7B1').grid(row=11, column=1, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#FFB7B1').grid(row=12, column=1, sticky="nsew")
 tk.Label(root, text="Illusions\nVPL", borderwidth=1, relief="solid",bg='#FFDAC1').grid(row=1, column=2, sticky="nsew")
 tk.Label(root, text="Blood Donation Drive\nBeach Cleanup Drive\nBliss\nInvictus", borderwidth=1, relief="solid",bg='#FFDAC1').grid(row=2, column=2, sticky="nsew")
 tk.Label(root, text="Umeed\nUtsav\nSphurti\nPraxis\nOctaves", borderwidth=1, relief="solid",bg='#FFDAC1').grid(row=3, column=2, sticky="nsew")
 tk.Label(root, text="Symposium", borderwidth=1, relief="solid",bg='#FFDAC1').grid(row=4, column=2, sticky="nsew")
 tk.Label(root, text="None", borderwidth=1, relief="solid",bg='#FFDAC1').grid(row=5, column=2, sticky="nsew")
 tk.Label(root, text="None", borderwidth=1, relief="solid",bg='#FFDAC1').grid(row=6, column=2, sticky="nsew")
 tk.Label(root, text="None", borderwidth=1, relief="solid",bg='#FFDAC1').grid(row=7, column=2, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#FFDAC1').grid(row=8, column=2, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#FFDAC1').grid(row=9, column=2, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#FFDAC1').grid(row=10, column=2, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#FFDAC1').grid(row=11, column=2, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#FFDAC1').grid(row=12, column=2, sticky="nsew")
 tk.Label(root, text="Illusions\nVPL", borderwidth=1, relief="solid",bg='#B5EAD6').grid(row=1, column=3, sticky="nsew")
 tk.Label(root, text="Blood Donation Drive\nBeach Cleanup Drive\nBliss\nInvictus", borderwidth=1, relief="solid",bg='#B5EAD6').grid(row=2, column=3, sticky="nsew")
 tk.Label(root, text="Umeed\nUtsav\nSphurti\nPraxis\nOctaves", borderwidth=1, relief="solid",bg='#B5EAD6').grid(row=3, column=3, sticky="nsew")
 tk.Label(root, text="Symposium", borderwidth=1, relief="solid",bg='#B5EAD6').grid(row=4, column=3, sticky="nsew")
 tk.Label(root, text="None", borderwidth=1, relief="solid",bg='#B5EAD6').grid(row=5, column=3, sticky="nsew")
 tk.Label(root, text="None", borderwidth=1, relief="solid",bg='#B5EAD6').grid(row=6, column=3, sticky="nsew")
 tk.Label(root, text="None", borderwidth=1, relief="solid",bg='#B5EAD6').grid(row=7, column=3, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#B5EAD6').grid(row=8, column=3, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#B5EAD6').grid(row=9, column=3, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#B5EAD6').grid(row=10, column=3, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#B5EAD6').grid(row=11, column=3, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#B5EAD6').grid(row=12, column=3, sticky="nsew")
 tk.Label(root, text="Illusions\nVPL", borderwidth=1, relief="solid",bg='#C6CEEA').grid(row=1, column=4, sticky="nsew")
 tk.Label(root, text="Blood Donation Drive\nBeach Cleanup Drive\nBliss\nInvictus", borderwidth=1, relief="solid",bg='#C6CEEA').grid(row=2, column=4, sticky="nsew")
 tk.Label(root, text="Umeed\nUtsav\nSphurti\nPraxis\nOctaves", borderwidth=1, relief="solid",bg='#C6CEEA').grid(row=3, column=4, sticky="nsew")
 tk.Label(root, text="Symposium", borderwidth=1, relief="solid",bg='#C6CEEA').grid(row=4, column=4, sticky="nsew")
 tk.Label(root, text="None", borderwidth=1, relief="solid",bg='#C6CEEA').grid(row=5, column=4, sticky="nsew")
 tk.Label(root, text="None", borderwidth=1, relief="solid",bg='#C6CEEA').grid(row=6, column=4, sticky="nsew")
 tk.Label(root, text="None", borderwidth=1, relief="solid",bg='#C6CEEA').grid(row=7, column=4, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#C6CEEA').grid(row=8, column=4, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#C6CEEA').grid(row=9, column=4, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#C6CEEA').grid(row=10, column=4, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#C6CEEA').grid(row=11, column=4, sticky="nsew")
 tk.Label(root, text="To be updated", borderwidth=1, relief="solid",bg='#C6CEEA').grid(row=12, column=4, sticky="nsew")
 

# Configure column and row resizing
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.rowconfigure(0, weight=1)
for i in range(1, 13):
    root.rowconfigure(i, weight=1)

root.mainloop()

