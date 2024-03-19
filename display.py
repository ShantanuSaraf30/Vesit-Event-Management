import mysql.connector
import tkinter  as tk 
from tkinter import * 
frame1 = tk.Tk()
frame1.geometry("1800x1800")
frame1.config(bg='#8B8DE7')
db = mysql.connector.connect(
  host="127.0.0.1",
  user="root", 
  passwd="Shan@2003",
  database="miniproject"
)

mycur = db.cursor()

a=tk.Label(frame1,text='Event Name',font = 'time 12 bold',fg="black",bg='#8B8DE7')
a.grid(row='1',column='0')
q=tk.Label(frame1,text='Name',font = 'time 12 bold',fg="black",bg='#8B8DE7')
q.grid(row='1',column='1')
a=tk.Label(frame1,text='class',font = 'time 12 bold',fg="black",bg='#8B8DE7')
a.grid(row='1',column='2')
a=tk.Label(frame1,text='Roll No.',font = 'time 12 bold',fg="black",bg='#8B8DE7')
a.grid(row='1',column='3')
a=tk.Label(frame1,text='Phone No.',font = 'time 12 bold',fg="black",bg='#8B8DE7')
a.grid(row='1',column='4')
a=tk.Label(frame1,text='Email',font = 'time 12 bold',fg="black",bg='#8B8DE7')
a.grid(row='1',column='5')

####### end of connection ####
mycur = db.cursor()
sql = "select * from registration where ename='utsav'"
mycur.execute(sql) 
myresult = mycur.fetchall()
i=2
for a in myresult:
    for j in range(len(a)):
        h = Entry(frame1,width=30,font = 'time 10 bold',fg="blue")
        
        h.grid(row=i,column=j,pady=5)
        h.insert(END,a[j])


    i=i+1
   
frame1.mainloop()
