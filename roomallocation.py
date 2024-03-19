import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import os
import time
from subprocess import call
from tkinter import *  
import pdb
global events

#connecting to the database
db = mysql.connector.connect(host="127.0.0.1",user="root",passwd="Shan@2003",database="miniproject")
mycur = db.cursor()
def pyfile():
        call(["python","test.py"])

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the title of the window
        self.title("Council Page")

        # Set the size of the window
        self.geometry("1800x1800")

        # Set the background color of the window
        self.configure(bg="#a2d2ff")

        # Create a sidebar frame
        self.sidebar = tk.Frame(self, bg="#613dc1", width=200)
        self.sidebar.pack(side="left", fill="y")

        # Create buttons inside the sidebar frame
        button1 = tk.Button(self.sidebar, text="  Home  ", command=self.show_frame1)
        button1.pack(pady=10)
        
        button2 = tk.Button(self.sidebar, text="Councils", command=self.show_frame2)
        button2.pack(pady=10)

       
        button3 = tk.Button(self.sidebar, text="Societies", command=self.show_frame3)
        button3.pack(pady=10)

        button4 = tk.Button(self.sidebar, text="  Clubs  ", command=self.show_frame4)
        button4.pack(pady=10)
        

        #button5 = tk.Button(self.sidebar, text=" Chat with Me ", command=self.show_frame5)
        #button5.pack(pady=10)

        button6 = tk.Button(self.sidebar, text=" Room Allocation", command=self.show_frame14)
        button6.pack(pady=10)
        button10 = tk.Button(self.sidebar, text="Room Booking", command=self.booking)  
        button10.pack(pady=10)
        button11 = tk.Button(self.sidebar, text="Floor Graph", command=self.graph)  
        button11.pack(pady=10)

        #button7 = tk.Button(self.sidebar, text="Create New Events ", command=self.show_frame15)  
        #button7.pack(pady=10)

        #button8 = tk.Button(self.sidebar, text="Modify Events ", command=self.show_frame16)  
        #button8.pack(pady=10)

        # Create a container frame to hold all the pages
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        # Create dictionary to hold all the pages
        self.pages = {}

        # Create the Frame 1 page and add it to the pages dictionary
        frame1 = tk.Frame(self.container, bg="#a2d2ff")
        logo_img = ImageTk.PhotoImage(file="home.png")
        logo_widget = tk.Label(frame1, image=logo_img, bg=frame1.cget("bg"), bd=0)
        logo_widget.image = logo_img
        logo_widget.place(x=0, y=0, relwidth=1, relheight=1)
       
        frame1_label = tk.Label(frame1, text="VESIT Council Management            ", font="Arial 20 bold",bg="#8b88e4")
        frame1_label.pack(pady=20)
        self.pages["Frame1"] = frame1

        
        my_button = tk.Button(frame1, text="Login",command=self.pyfile)
        my_button.config(width=20, height=3, bg="#f6aeae")
        my_button.pack(pady=10, padx=10, anchor="ne")
        
        my_button = tk.Button(frame1, text="Grid View",command=self.table)
        my_button.config(width=21, height=3, bg="#f6aeae")
        my_button.pack(side="right", anchor="ne")
        
        #connecting to the database
        #Fech All

        label=tk.Label(frame1,text="UPCOMING EVENTS",font='time 20 ',fg='black',bg="#8b88e4")
        label.pack(padx=10,pady=30)

        mycur = db.cursor()
        sql = "select * from events where status='UPCOMING' "
        mycur.execute(sql) 
        myresult = mycur.fetchall()

        for i in myresult:
            h = tk.Label(frame1,font = 'time 20 bold',text =f"{i[1]}",fg="white",bg="navy blue")
            h.pack(side ="top")
            name = tk.Label(frame1,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#8a83e5")
            name.pack(side ="top",pady=10)
            time = tk.Label(frame1,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#8a83e5")
            time.pack(side ="top")
            date = tk.Label(frame1,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#8a83e5")
            date.pack(side ="top")
            venue=tk.Label(frame1,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#8a83e5")
            venue.pack(side ="top")
            desc=tk.Label(frame1,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#8a83e5")
            desc.pack(side ="top")
           
            my_button1 = tk.Button(frame1, text="Registration",command=self.reg)
            my_button1.config(width=20, height=3, bg="#caf0f8")
            my_button1.pack(side='top',pady=20)
       

       

        
         # Create the Frame 2 page and add it to the pages dictionary
        frame2 = tk.Frame(self.container, bg="#a2d2ff")
        logo_img = ImageTk.PhotoImage(file="frame2.png")
        logo_widget = tk.Label(frame2, image=logo_img, bg=frame2.cget("bg"), bd=0)
        logo_widget.image = logo_img
        logo_widget.place(x=0, y=0, relwidth=1, relheight=1)
        frame2_label = tk.Label(frame2, text="Councils", font=("Arial", 20))
        frame2_label.pack(pady=20)
        self.pages["Frame2"] = frame2

        my_button = tk.Button(frame2, text="SoRT",command=self.show_frame10)
        my_button.config(width=10, height=3, bg="#caf0f8")
        my_button.place(x=150, y=85)

        my_button = tk.Button(frame2, text="Cultural",command=self.show_frame11)  
        my_button.config(width=10, height=3, bg="#caf0f8")
        my_button.place(x=150, y=185)

        my_button = tk.Button(frame2, text="Sports", command=self.show_frame12)    
        my_button.config(width=10, height=3, bg="#caf0f8")
        my_button.place(x=150, y=285)

        my_button = tk.Button(frame2, text="Music", command=self.show_frame13)
        my_button.config(width=10, height=3, bg="#caf0f8")
        my_button.place(x=150, y=385)
               
        # Create the Frame 3 page and add it to the pages dictionary
        frame3 = tk.Frame(self.container, bg="#a2d2ff")
        logo_img = ImageTk.PhotoImage(file="tech.png")
        logo_widget = tk.Label(frame3, image=logo_img, bg=frame3.cget("bg"), bd=0)
        logo_widget.image = logo_img
        logo_widget.place(x=0, y=0, relwidth=1, relheight=1)
        frame3_label = tk.Label(frame3, text="Societies", font=("Arial", 20))
        frame3_label.pack(pady=20)
        self.pages["Frame3"] = frame3

        my_button = tk.Button(frame3, text="ISA-Vesit",command=self.show_frame6)
        my_button.config(width=10, height=3, bg="#caf0f8")
        my_button.place(x=150, y=85)

        button6= tk.Button(frame3, text="CSI-Vesit ",command=self.show_frame7)  
        button6.config(width=10, height=3, bg="#caf0f8")
        button6.place(x=150, y=185)

        my_button = tk.Button(frame3, text="ISTE-Vesit",command=self.show_frame8)   
        my_button.config(width=10, height=3, bg="#caf0f8")
        my_button.place(x=150, y=285)

        my_button = tk.Button(frame3, text="IEEE-Vesit",command=self.show_frame9)
        my_button.config(width=10, height=3, bg="#caf0f8")
        my_button.place(x=150, y=385)

        # Create the Frame 4 page and add it to the pages dictionary
        frame4 = tk.Frame(self.container, bg="#a2d2ff")
        frame4_label = tk.Label(frame4, text="Clubs", font=("Arial", 20))
        frame4_label.pack(pady=20)
        self.pages["Frame4"] = frame4


        # Create the Frame 5 page and add it to the pages dictionary
        frame5 = tk.Frame(self.container, bg="#a2d2ff")
        frame5_label = tk.Label(frame5, text="Circles", font=("Arial", 20))
        frame5_label.pack(pady=20)
        self.pages["Frame5"] = frame5


        # Create the Frame 6 page and add it to the pages dictionary
        frame6 = tk.Frame(self.container, bg="#a2d2ff")
        frame6_label = tk.Label(frame6, text="ISA-Vesit", font=("Arial", 20))
        frame6_label.pack(pady=20)
        self.pages["Frame6"] = frame6
        #connecting to the database
        #Fech All

        label=tk.Label(frame1,text="Upcoming Events",font='time 30 bold',bg="#a2d2ff")
        label.pack(padx=10,pady=30)

        logo_img = ImageTk.PhotoImage(file="isa.png")
        logo_widget = tk.Label(frame6, image=logo_img, bg=frame6.cget("bg"), bd=0)
        logo_widget.image = logo_img
        logo_widget.place(x=0, y=0, relwidth=1, relheight=1)

        mycur = db.cursor()
        sql = "select * from events where councilname ='ISA-VESIT' "
        mycur.execute(sql) 
        myresult = mycur.fetchall()

        for i in myresult:
            h = tk.Label(frame6,font = 'time 20 bold',text =f"{i[1]}",fg="white",bg="navy blue")
            h.pack(side ="top",fill='x')
            name = tk.Label(frame6,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#a2d2ff")
            name.pack(side ="top")
            time = tk.Label(frame6,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#a2d2ff")
            time.pack(side ="top")
            date = tk.Label(frame6,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#a2d2ff")
            date.pack(side ="top",)
            venue=tk.Label(frame6,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#a2d2ff")
            venue.pack(side ="top")
            desc=tk.Label(frame6,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#a2d2ff")
            desc.pack(side ="top")
            my_button1 = tk.Button(frame6, text="Registration",command=self.reg)
            my_button1.config(width=20, height=3, bg="#caf0f8")
            my_button1.pack(side='top',pady=10)
            desc1=tk.Label(frame1,font = 'time 12 bold',text ="  ",fg="black",bg="#a2d2ff")
            desc1.pack(side ="top",fill='x')
         
        #create the frame 7 page and add it to the pages dictionary
        frame7 = tk.Frame(self.container, bg="#a2d2ff")

        logo_img = ImageTk.PhotoImage(file="csi.png")
        logo_widget = tk.Label(frame7, image=logo_img, bg=frame7.cget("bg"), bd=0)
        logo_widget.image = logo_img
        logo_widget.place(x=0, y=0, relwidth=1, relheight=1)
        frame7_label = tk.Label(frame7, text="CSI-Vesit", font=("Arial", 20))
        frame7_label.pack(pady=20)
        self.pages["Frame7"] = frame7
        #connecting to the database
        #Fech All

        label=tk.Label(frame1,text="Upcoming Events",font='time 30 bold',bg="#a2d2ff")
        label.pack(padx=10,pady=30)

        mycur = db.cursor()
        sql = "select * from events where councilname ='CSI-VESIT' "
        mycur.execute(sql) 
        myresult = mycur.fetchall()

        for i in myresult:
            h = tk.Label(frame7,font = 'time 20 bold',text =f"{i[1]}",fg="white",bg="navy blue")
            h.pack(side ="top",fill='x')
            name = tk.Label(frame7,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#a2d2ff")
            name.pack(side ="top")
            time = tk.Label(frame7,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#a2d2ff")
            time.pack(side ="top")
            date = tk.Label(frame7,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#a2d2ff")
            date.pack(side ="top",)
            venue=tk.Label(frame7,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#a2d2ff")
            venue.pack(side ="top")
            desc=tk.Label(frame7,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#a2d2ff")
            desc.pack(side ="top")
            my_button1 = tk.Button(frame7, text="Registration",command=self.reg)
            my_button1.config(width=20, height=3, bg="#caf0f8")
            my_button1.pack(side='top',pady=10)
            desc1=tk.Label(frame1,font = 'time 12 bold',text ="  ",fg="black",bg="#a2d2ff")
            desc1.pack(side ="top",fill='x')
            
        # Create the Frame 8 page and add it to the pages dictionary
        frame8 = tk.Frame(self.container, bg="#a2d2ff")
        logo_img = ImageTk.PhotoImage(file="iste.png")
        logo_widget = tk.Label(frame8, image=logo_img, bg=frame8.cget("bg"), bd=0)
        logo_widget.image = logo_img
        logo_widget.place(x=0, y=0, relwidth=1, relheight=1)
        frame8_label = tk.Label(frame8, text="ISTE-Vesit", font=("Arial", 20))
        frame8_label.pack(pady=20)
        self.pages["Frame8"] = frame8
        #connecting to the database
        #Fech All

        label=tk.Label(frame1,text="Upcoming Events",font='time 30 bold',bg="#a2d2ff")
        label.pack(padx=10,pady=30)

        mycur = db.cursor()
        sql = "select * from events where councilname ='ISTE-VESIT' "
        mycur.execute(sql) 
        myresult = mycur.fetchall()

        for i in myresult:
            h = tk.Label(frame8,font = 'time 20 bold',text =f"{i[1]}",fg="white",bg="navy blue")
            h.pack(side ="top",fill='x')
            name = tk.Label(frame8,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#a2d2ff")
            name.pack(side ="top")
            time = tk.Label(frame8,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#a2d2ff")
            time.pack(side ="top")
            date = tk.Label(frame8,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#a2d2ff")
            date.pack(side ="top",)
            venue=tk.Label(frame8,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#a2d2ff")
            venue.pack(side ="top")
            desc=tk.Label(frame8,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#a2d2ff")
            desc.pack(side ="top")
            my_button1 = tk.Button(frame8, text="Registration",command=self.reg)
            my_button1.config(width=20, height=3, bg="#caf0f8")
            my_button1.pack(side='top',pady=10)
            desc1=tk.Label(frame1,font = 'time 12 bold',text ="  ",fg="black",bg="#a2d2ff")
            desc1.pack(side ="top",fill='x')

        #create the frame 9 page and add it to the pages dictionary
        frame9 = tk.Frame(self.container, bg="#a2d2ff")
        logo_img = ImageTk.PhotoImage(file="ieee.png")
        logo_widget = tk.Label(frame9, image=logo_img, bg=frame9.cget("bg"), bd=0)
        logo_widget.image = logo_img
        logo_widget.place(x=0, y=0, relwidth=1, relheight=1)
        frame9_label = tk.Label(frame9, text="IEEE-Vesit", font=("Arial", 20))
        frame9_label.pack(pady=20)
        self.pages["Frame9"] = frame9
        #connecting to the database
        #Fech All

        label=tk.Label(frame1,text="Upcoming Events",font='time 30 bold',bg="#a2d2ff")
        label.pack(padx=10,pady=30)

        mycur = db.cursor()
        sql = "select * from events where councilname ='IEEE-VESIT' "
        mycur.execute(sql) 
        myresult = mycur.fetchall()

        for i in myresult:
            h = tk.Label(frame9,font = 'time 20 bold',text =f"{i[1]}",fg="white",bg="navy blue")
            h.pack(side ="top",fill='x')
            name = tk.Label(frame9,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#a2d2ff")
            name.pack(side ="top")
            time = tk.Label(frame9,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#a2d2ff")
            time.pack(side ="top")
            date = tk.Label(frame9,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#a2d2ff")
            date.pack(side ="top",)
            venue=tk.Label(frame9,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#a2d2ff")
            venue.pack(side ="top")
            desc=tk.Label(frame9,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#a2d2ff")
            desc.pack(side ="top")
            my_button1 = tk.Button(frame9, text="Registration",command=self.reg)
            my_button1.config(width=20, height=3, bg="#caf0f8")
            my_button1.pack(side='top',pady=10)
            desc1=tk.Label(frame1,font = 'time 12 bold',text ="  ",fg="black",bg="#a2d2ff")
            desc1.pack(side ="top",fill='x')


        # Create the Frame 10 page and add it to the pages dictionary
        frame10 = tk.Frame(self.container, bg="#a2d2ff")
        logo_img = ImageTk.PhotoImage(file="sort.png")
        logo_widget = tk.Label(frame10, image=logo_img, bg=frame10.cget("bg"), bd=0)
        logo_widget.image = logo_img
        logo_widget.place(x=0, y=0, relwidth=1, relheight=1)
        frame10_label = tk.Label(frame10, text="SoRT", font=("Arial", 20))
        frame10_label.pack(pady=20)
        self.pages["Frame10"] = frame10
        #connecting to the database
        #Fech All

        label=tk.Label(frame1,text="Upcoming Events",font='time 30 bold',bg="#a2d2ff")
        label.pack(padx=10,pady=30)

        mycur = db.cursor()
        sql = "select * from events where councilname ='Sort' "
        mycur.execute(sql) 
        myresult = mycur.fetchall()

        for i in myresult:
            h = tk.Label(frame10,font = 'time 20 bold',text =f"{i[1]}",fg="white",bg="navy blue")
            h.pack(side ="top")
            name = tk.Label(frame10,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#F7C59F")
            name.pack(side ="top")
            time = tk.Label(frame10,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#F7C59F")
            time.pack(side ="top")
            date = tk.Label(frame10,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#F7C59F")
            date.pack(side ="top",)
            venue=tk.Label(frame10,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#F7C59F")
            venue.pack(side ="top")
            desc=tk.Label(frame10,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#F7C59F")
            desc.pack(side ="top")
            my_button1 = tk.Button(frame10, text="Registration",command=self.reg)
            my_button1.config(width=20, height=3, bg="#caf0f8")
            my_button1.pack(side='top',pady=10)
            desc1=tk.Label(frame1,font = 'time 12 bold',text ="  ",fg="black",bg="#a2d2ff")
            desc1.pack(side ="top",fill='x')

        # Create the Frame 11 page and add it to the pages dictionary
        frame11 = tk.Frame(self.container, bg="#a2d2ff")

        logo_img = ImageTk.PhotoImage(file="cultural.png")
        logo_widget = tk.Label(frame11, image=logo_img, bg=frame11.cget("bg"), bd=0)
        logo_widget.image = logo_img
        logo_widget.place(x=0, y=0, relwidth=1, relheight=1)
        frame11_label = tk.Label(frame11, text="Cultural", font=("Arial", 20))
        frame11_label.pack(pady=20)
        self.pages["Frame11"] = frame11
        #connecting to the database
        #Fech All

        label=tk.Label(frame1,text="Upcoming Events",font='time 30 bold',bg="#a2d2ff")
        label.pack(padx=10,pady=30)

        mycur = db.cursor()
        sql = "select * from events where councilname ='Cultural' "
        mycur.execute(sql) 
        myresult = mycur.fetchall()

        for i in myresult:
            h = tk.Label(frame11,font = 'time 20 bold',text =f"{i[1]}",fg="white",bg="navy blue")
            h.pack(side ="top")
            name = tk.Label(frame11,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#8a83e5")
            name.pack(side ="top")
            time = tk.Label(frame11,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#8a83e5")
            time.pack(side ="top")
            date = tk.Label(frame11,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#8a83e5")
            date.pack(side ="top",)
            venue=tk.Label(frame11,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#8a83e5")
            venue.pack(side ="top")
            desc=tk.Label(frame11,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#8a83e5")
            desc.pack(side ="top")
            my_button1 = tk.Button(frame11, text="Registration",command=self.reg)
            my_button1.config(width=20, height=3, bg="#caf0f8")
            my_button1.pack(side='top',pady=10)
            desc1=tk.Label(frame1,font = 'time 12 bold',text ="  ",fg="black",bg="#a2d2ff")
            desc1.pack(side ="top",fill='x')
        # Create the Frame 12 page and add it to the pages dictionary
        frame12 = tk.Frame(self.container, bg="#a2d2ff")
        logo_img = ImageTk.PhotoImage(file="sports.jpg")
        logo_widget = tk.Label(frame12, image=logo_img, bg=frame12.cget("bg"), bd=0)
        logo_widget.image = logo_img
        logo_widget.place(x=0, y=0, relwidth=1, relheight=1)
        frame12_label = tk.Label(frame12, text="Sports", font=("Arial", 20))
        frame12_label.pack(pady=20)
        self.pages["Frame12"] = frame12
        #connecting to the database
        #Fech All

        label=tk.Label(frame1,text="Upcoming Events",font='time 30 bold',bg="#a2d2ff")
        label.pack(padx=10,pady=30)

        mycur = db.cursor()
        sql = "select * from events where councilname ='Sports' "
        mycur.execute(sql) 
        myresult = mycur.fetchall()

        for i in myresult:
            h = tk.Label(frame12,font = 'time 20 bold',text =f"{i[1]}",fg="white",bg="navy blue")
            h.pack(side ="top")
            name = tk.Label(frame12,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#AFC8FF")
            name.pack(side ="top")
            time = tk.Label(frame12,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#AFC8FF")
            time.pack(side ="top")
            date = tk.Label(frame12,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#AFC8FF")
            date.pack(side ="top",)
            venue=tk.Label(frame12,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#AFC8FF")
            venue.pack(side ="top")
            desc=tk.Label(frame12,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#AFC8FF")
            desc.pack(side ="top")
            my_button1 = tk.Button(frame12, text="Registration",command=self.reg)
            my_button1.config(width=20, height=3, bg="#caf0f8")
            my_button1.pack(side='top',pady=10)
            desc1=tk.Label(frame1,font = 'time 12 bold',text ="  ",fg="black",bg="#a2d2ff")
            desc1.pack(side ="top",fill='x')

        # Create the Frame 13 page and add it to the pages dictionary
        frame13 = tk.Frame(self.container, bg="#a2d2ff")
        logo_img = ImageTk.PhotoImage(file="music.jpg")
        logo_widget = tk.Label(frame13, image=logo_img, bg=frame13.cget("bg"), bd=0)
        logo_widget.image = logo_img
        logo_widget.place(x=0, y=0, relwidth=1, relheight=1)
        frame13_label = tk.Label(frame13, text="Music", font=("Arial", 20))
        frame13_label.pack(pady=20)
        self.pages["Frame13"] = frame13
        #connecting to the database
        #Fech All

        label=tk.Label(frame1,text="Upcoming Events",font='time 30 bold',bg="#a2d2ff")
        label.pack(padx=10,pady=30)

        mycur = db.cursor()
        sql = "select * from events where councilname ='Music' "
        mycur.execute(sql) 
        myresult = mycur.fetchall()

        for i in myresult:
            h = tk.Label(frame13,font = 'time 20 bold',text =f"{i[1]}",fg="white",bg="navy blue")
            h.pack(side ="top")
            name = tk.Label(frame13,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#C0D1F4")
            name.pack(side ="top")
            time = tk.Label(frame13,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#C0D1F4")
            time.pack(side ="top")
            date = tk.Label(frame13,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#C0D1F4")
            date.pack(side ="top",)
            venue=tk.Label(frame13,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#C0D1F4")
            venue.pack(side ="top")
            desc=tk.Label(frame13,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#C0D1F4")
            desc.pack(side ="top")
            my_button1 = tk.Button(frame13, text="Registration",command=self.reg)
            my_button1.config(width=20, height=3, bg="#caf0f8")
            my_button1.pack(side='top',pady=10)
            desc1=tk.Label(frame1,font = 'time 12 bold',text ="  ",fg="black",bg="#a2d2ff")
            desc1.pack(side ="top",fill='x')
        # Create the Frame 14 page and add it to the pages dictionary
       
        frame14 = tk.Frame(self.container, bg="#a2d2ff")
        frame14_label = tk.Label(frame14, text="Room Allocation", font=("Arial", 20))
        frame14_label.pack(pady=20)
        self.pages["Frame14"] = frame14
        
        label=tk.Label(frame14,text="ROOM REQUEST",font='time 30 bold',bg="#a2d2ff")
        label.pack(padx=10,pady=30)

        mycur = db.cursor()
        sql = "select * from rooms"
        mycur.execute(sql) 
        myresult = mycur.fetchall()

        for g in myresult:
            h = tk.Label(frame14,font = 'time 20 bold',text =f"Council name:{g[0]}",fg="white",bg="navy blue")
            h.pack(side ="top",fill='x')
            name = tk.Label(frame14,font = 'time 12 bold',text =f"Room NO. :{g[1]}",fg="black",bg="#a2d2ff")
            name.pack(side ="top",fill='x')
            time = tk.Label(frame14,font = 'time 12 bold',text =f"Event Name: {g[2]}",fg="black",bg="#a2d2ff")
            time.pack(side ="top",fill='x')
            date = tk.Label(frame14,font = 'time 12 bold',text =f"Date: {g[3]}",fg="black",bg="#a2d2ff")
            date.pack(side ="top",fill='x')
            venue=tk.Label(frame14,font = 'time 12 bold',text =f"Time: {g[4]}",fg="black",bg="#a2d2ff")
            venue.pack(side ="top",fill='x')
            desc=tk.Label(frame14,font = 'time 12 bold',text =f"Reason: {g[5]}",fg="black",bg="#a2d2ff")
            desc.pack(side ="top",fill='x')
            desc1=tk.Label(frame14,font = 'time 12 bold',text ="  ",fg="black",bg="#a2d2ff")
            desc1.pack(side ="top",fill='x')                       

      
        


# Create the Frame 15 page and add it to the pages dictionary delete event
        frame15 = tk.Frame(self.container, bg="#a2d2ff")
        frame15_label = tk.Label(frame15, text="New Event", font=("Arial", 20))
        frame15_label.pack(pady=20)
        self.pages["Frame15"] = frame15

        label_coun = tk.Label(frame15, text="Council name",font=('arial',16,'bold'),fg='black',bg='powder blue')
        entry_coun = tk.Entry(frame15,)
        
        label_event_name = tk.Label(frame15, text="Name of the event",font=('arial',16,'bold'),fg='black',bg='powder blue')
        entry_event_name = tk.Entry(frame15)
        label_time = tk.Label(frame15, text="Time",font=('arial',16,'bold'),fg='black',bg='powder blue')
        entry_time = tk.Entry(frame15)
        label_date = tk.Label(frame15, text="Date",font=('arial',16,'bold'),fg='black',bg='powder blue')
        entry_date = tk.Entry(frame15)
        label_ven = tk.Label(frame15, text="Venue",font=('arial',16,'bold'),fg='black',bg='powder blue')
        entry_ven = tk.Entry(frame15)
        label_des = tk.Label(frame15, text="Event description",font=('arial',16,'bold'),fg='black',bg='powder blue')
        entry_des = tk.Entry(frame15)
        label_stat = tk.Label(frame15, text="Status of the event",font=('arial',16,'bold'),fg='black',bg='powder blue')
        entry_stat = tk.Entry(frame15)


        # Pack the labels and entry fields vertically with padding
        label_coun.pack(pady=10)
        entry_coun.pack()
        label_event_name.pack(pady=10)
        entry_event_name.pack()
        label_time.pack(pady=10)
        entry_time.pack()
        label_date.pack(pady=10)
        entry_date.pack()
        label_ven.pack(pady=10)
        entry_ven.pack()
        label_des.pack(pady=10)
        entry_des.pack()
        label_stat.pack(pady=10)
        entry_stat.pack()
# Define a function to submit the form
        def submit_form():
            coun = entry_coun.get()
            event_name = entry_event_name.get()
            time = entry_time.get()
            date = entry_date.get()
            ven = entry_ven.get()
            des = entry_des.get()
            stat=entry_stat.get()
            sql = "insert into events values(%s,%s,%s,%s,%s,%s,%s)"
            t = (coun,event_name,time,date,ven,des,stat)
            mycur.execute(sql, t)
            db.commit()
            success1()
        def success1():
            global succ
            succ=tk.Tk()
            succ.title("Success")
            succ.geometry("1800x1800")
            h1=tk.Label(succ, text="EVENT ADDED SUCCESSFULLY", fg="green", font="bold")
            h1.pack()
            my_button1 = tk.Button(succ, text="Home",command=home)
            my_button1.config(width=20, height=3, bg="#caf0f8")
            my_button1.pack(side='top',pady=10)
        def home():
            call(["python","Council window.py"])
        # Create a submit button
        button_submit = tk.Button(frame15, text="Submit",font=('arial',16,'bold'),command=submit_form,fg='white',width=20,bg='navy blue')
        button_submit.pack(pady=20)

# Create the Frame 16 page and add it to the pages dictionary delete event
        frame16 = tk.Frame(self.container, bg="#a2d2ff")
        frame16_label = tk.Label(frame16, text="Modify Event", font=("Arial", 20))
        frame16_label.pack(pady=20)
        self.pages["Frame16"] = frame16
        

        label=tk.Label(frame16,text="Events",font='time 30 bold',bg="#a2d2ff")
        label.pack(padx=10,pady=30)
        
        mycur = db.cursor()
        sql = "select * from events"
        mycur.execute(sql) 
        myresult = mycur.fetchall()
     
        def createbutton(value):
                button = tk.Button(frame16, text=value, command=lambda v=value:button_click(v),fg='white',width=20,bg='navy blue',font=('arial',16,'bold'))
                button.pack(pady=20)     
        for i in myresult:
            createbutton(i[1])
        def button_click(v):
                frame17 = tk.Frame(self.container, bg="#a2d2ff")
                frame17_label = tk.Label(frame17, text=v, font=("Arial", 20))
                frame17_label.pack(pady=20)
               
                mycur1 = db.cursor()
                sql = 'select * from events where ename=?'
                mycur1.execute(sql,(v)) 
                myresult = mycur1.fetchall()
                for i in myresult:
                        label_coun = tk.Label(frame17, text="Council name",font=('arial',16,'bold'),fg='black',bg='powder blue')
                        entry_coun = tk.Entry(frame17,)
                        entry_coun.insert(END,i[0])
                        label_event_name = tk.Label(frame17, text="Name of the event",font=('arial',16,'bold'),fg='black',bg='powder blue')
                        entry_event_name = tk.Entry(frame17)
                        entry_event_name.insert(END,i[1])
                        label_time = tk.Label(frame17, text="Time",font=('arial',16,'bold'),fg='black',bg='powder blue')
                        entry_time = tk.Entry(frame17)
                        entry_time.insert(END,i[2])
                        label_date = tk.Label(frame17, text="Date",font=('arial',16,'bold'),fg='black',bg='powder blue')
                        entry_date = tk.Entry(frame17)
                        entry_date.insert(END,i[3])
                        label_ven = tk.Label(frame17, text="Venue",font=('arial',16,'bold'),fg='black',bg='powder blue')
                        entry_ven = tk.Entry(frame17)
                        entry_ven.insert(END,i[4])
                        label_des = tk.Label(frame17, text="Event description",font=('arial',16,'bold'),fg='black',bg='powder blue')
                        entry_des = tk.Entry(frame17)
                        entry_des.insert(END,i[5])
                        label_stat=tk.Label(frame17,text="Status of Event",font=('arial',16,'bold'),fg='black',bg='powder blue')
                        entry_stat.insert(END,i[6])
                        button_submit()
                label_coun.pack(pady=10)
                entry_coun.pack()
                label_event_name.pack(pady=10)
                entry_event_name.pack()
                label_time.pack(pady=10)
                entry_time.pack()
                label_date.pack(pady=10)
                entry_date.pack()
                label_ven.pack(pady=10)
                entry_ven.pack()
                label_des.pack(pady=10)
                entry_des.pack()
                label_stat.pack(pady=10)
                entry_stat.pack()

                
# Define a function to submit the form
        def submit_form1():
            coun = entry_coun.get()
            event_name = entry_event_name.get()
            time = entry_time.get()
            date = entry_date.get()
            ven = entry_ven.get()
            des = entry_des.get()
            stat=entry_stat.get()
            sql = "update events set councilname=%s,ename=%s,ename=%s,time=%s,date=%s,venue=%s,desc=%s,status=%s where ename=?"
            t = (coun,event_name,time,date,ven,des,stat)
            mycur.execute(sql,(value))
            db.commit()
            success3()
        def success3():
            global succ
            succ=tk.Tk()
            succ.title("Success")
            succ.geometry("1800x1800")
            h1=tk.Label(succ, text="EVENT MODIFIED SUCCESSFULLY", fg="green", font="bold")
            h1.pack()
            my_button1 = tk.Button(succ, text="Home",command=home)
            my_button1.config(width=20, height=3, bg="#caf0f8")
            my_button1.pack(side='top',pady=10)
        def home():
            call(["python","Council window.py"])
        # Create a submit button
        def button_submit():
                button_submit = tk.Button(frame17, text="Submit",font=('arial',16,'bold'), command=submit_form1,fg='white',width=20,bg='navy blue')
                button_submit.pack(pady=20)
        

        
        # Show the Frame 1 page by defalt
        self.current_page = "Frame1"
        self.show_page("Frame1")

    def show_page(self, page_name):
        # Hide the current page
        current_page = self.pages[self.current_page]
        current_page.pack_forget()

        # Show the new page
        new_page = self.pages[page_name]
        new_page.pack(side="left", fill="both", expand=True)

        # Set the current page to the new page
        self.current_page = page_name

    def show_frame1(self):
        self.show_page("Frame1")

    def show_frame2(self):
        self.show_page("Frame2")

    def show_frame3(self):
        self.show_page("Frame3")

    def show_frame4(self):
        self.show_page("Frame4")

    def show_frame5(self):
        self.show_page("Frame5")
    
    def show_frame6(self):
        self.show_page("Frame6")

    def show_frame7(self):
        self.show_page("Frame7")

    def show_frame8(self):
        self.show_page("Frame8")

    def show_frame9(self):
        self.show_page("Frame9")            
    
    def show_frame10(self):
        self.show_page("Frame10")

    def show_frame11(self):
        self.show_page("Frame11")

    def show_frame12(self):
        self.show_page("Frame12")

    def show_frame13(self):
        self.show_page("Frame13")

    def show_frame14(self):
        self.show_page("Frame14")
    def show_frame15(self):
        self.show_page("Frame15")
 
    def show_frame16(self):
        self.show_page("Frame16")

    def pyfile(self):
        call(["python","test.py"])
    def reg(self):
        call(["python","registration.py"])
    def table(self):
            call(['python','table.py'])
    def booking(self):
        call(["python","roombooking.py"])
    def graph(self):
        call(["python","graph.py"])             


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
