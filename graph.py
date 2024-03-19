import matplotlib.pyplot as plt
import mysql.connector
db = mysql.connector.connect(host="127.0.0.1",user="root",passwd="Shan@2003",database="miniproject")
mycur = db.cursor()


fig, ax = plt.subplots()
sql = "select roomscol from rooms"
mycur.execute(sql) 
list1 = mycur.fetchall()
a=0
b=0
c=0
d=0
e=0

number = len(list1)
print(list1)
for i in list1:
 if i[0]=='1':
  a=a+1
 elif  i[0]=='2':
  b=b+1
 elif i[0]=='3':
  c=c+1
 elif  i[0]=='4':
  d=d+1
 else:
  e=e+1

fruits = ['1st', '2nd', '3rd', '4th', '5th']
counts = [a, b, c, d, e]
bar_labels = ['red', 'pink', 'blue', 'orange', 'green']
bar_colors = ['tab:red', 'tab:pink', 'tab:blue', 'tab:orange', 'tab:green']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('Frequency')
ax.set_title('Floors')


plt.show()
