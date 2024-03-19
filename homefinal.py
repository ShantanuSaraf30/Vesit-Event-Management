import tkinter as tk

from PIL import Image, ImageTk
import mysql.connector
import os
import time
from subprocess import call
from tkinter import *  



#connecting to the database
db = mysql.connector.connect(host="127.0.0.1",user="root",passwd="Shan@2003",database="miniproject")
mycur = db.cursor()
def pyfile():
        call(["python","test.py"])

class MyApp(tk.Tk):
    
    def __init__(self):
        super().__init__()

        # Set the title of the window
        self.title("VESIT Event Management")

        # Set the size of the window
        self.geometry("1800x1800")
        
          
        # Set the background color of the window
        self.configure(bg="#a2d2ff")
        

        # Create a sidebar frame
        self.sidebar = tk.Frame(self, bg="#9f99ef", width=200)
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

        button5 = tk.Button(self.sidebar, text=" Chat with Me ", command=self.chatbot)
        button5.pack(pady=10)

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
        self.scroll_y=tk.Scrollbar(frame1,orient=VERTICAL)
        
        self.scroll_y.pack(side=RIGHT,fill=Y)
  
       
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

        label=tk.Label(frame1,text="UPCOMING EVENTS",font='times 22 bold' ,fg='black',bg="#8b88e4")
        label.pack(padx=10,pady=30)

        mycur = db.cursor()
        sql = "select * from events where status='UPCOMING' "
        mycur.execute(sql) 
        myresult = mycur.fetchall()

        for i in myresult:
            h = tk.Label(frame1,font = 'times 17 bold',text =f"{i[1]}",fg="white",bg="navy blue")
            h.pack(side ="top",pady=5)
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
           
            my_button1 = tk.Button(frame1, text="Registration",font='times 10',command=self.reg)
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
            h.pack(side ="top")
            name = tk.Label(frame6,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#C0D1F4")
            name.pack(side ="top")
            time = tk.Label(frame6,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#C0D1F4")
            time.pack(side ="top")
            date = tk.Label(frame6,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#C0D1F4")
            date.pack(side ="top",)
            venue=tk.Label(frame6,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#C0D1F4")
            venue.pack(side ="top")
            desc=tk.Label(frame6,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#C0D1F4")
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
            h.pack(side ="top")
            name = tk.Label(frame7,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#F7C59F")
            name.pack(side ="top")
            time = tk.Label(frame7,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#F7C59F")
            time.pack(side ="top")
            date = tk.Label(frame7,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#F7C59F")
            date.pack(side ="top",)
            venue=tk.Label(frame7,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#F7C59F")
            venue.pack(side ="top")
            desc=tk.Label(frame7,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#F7C59F")
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
            h.pack(side ="top")
            name = tk.Label(frame8,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#F6AEAE")
            name.pack(side ="top")
            time = tk.Label(frame8,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#F6AEAE")
            time.pack(side ="top")
            date = tk.Label(frame8,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#F6AEAE")
            date.pack(side ="top",)
            venue=tk.Label(frame8,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#F6AEAE")
            venue.pack(side ="top")
            desc=tk.Label(frame8,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#F6AEAE")
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
            h.pack(side ="top")
            name = tk.Label(frame9,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#AFC8FF")
            name.pack(side ="top")
            time = tk.Label(frame9,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#AFC8FF")
            time.pack(side ="top")
            date = tk.Label(frame9,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#AFC8FF")
            date.pack(side ="top",)
            venue=tk.Label(frame9,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#AFC8FF")
            venue.pack(side ="top")
            desc=tk.Label(frame9,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#AFC8FF")
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
            name = tk.Label(frame11,font = 'time 12 bold',text =f"Hosted by :{i[0]}",fg="black",bg="#F6AEAE")
            name.pack(side ="top")
            time = tk.Label(frame11,font = 'time 12 bold',text =f"Time: {i[2]}",fg="black",bg="#F6AEAE")
            time.pack(side ="top")
            date = tk.Label(frame11,font = 'time 12 bold',text =f"Date: {i[3]}",fg="black",bg="#F6AEAE")
            date.pack(side ="top",)
            venue=tk.Label(frame11,font = 'time 12 bold',text =f"Venue: {i[4]}",fg="black",bg="#F6AEAE")
            venue.pack(side ="top")
            desc=tk.Label(frame11,font = 'time 12 bold',text =f"Description: {i[5]}",fg="black",bg="#F6AEAE")
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
    def pyfile(self):
        call(["python","test.py"])
    def reg(self):
        call(["python","registration.py"])
    def chatbot(self):
            call(["python","chatbot.py"])
    def table(self):
            call(['python','table.py'])
if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
