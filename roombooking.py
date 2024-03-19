import tkinter as tk
from subprocess import call

def change_color(button):
    # Check the current background color of the button
    current_bg = button.cget("bg")
    if current_bg == "red":
        button.config(bg="white")  # Change the background color to white if it's currently red
    else:
        button.config(bg="red")  # Change the background color to red if it's currently not red

root = tk.Tk()
root.configure(bg='#8B8DE7')
# Create a frame
frame = tk.Frame(root)

frame.pack()
frame.configure(bg='#8B8DE7')
def council():
    call(['python','Council window.py'])

def book():
    call(['python','book.py'])




# Create buttons and add them to the frame in the first row
buttons_row1 = []  # List to hold buttons in the first row
for i in range(15):
    button = tk.Button(frame, text=f"{(i+101)}", command=lambda i=i: change_color(buttons_row1[i]))
    button.grid(row=0, column=i, padx=10, pady=10)  # Use grid layout, add the button to the first row
    buttons_row1.append(button)  # Add the button to the list of buttons in the first row
    
button1 = tk.Button(frame, text="B11", command=lambda: change_color(button1))
button1.grid(row=0, column=16, padx=10, pady=10)
button2 = tk.Button(frame, text="B12", command=lambda: change_color(button2))
button2.grid(row=0, column=17, padx=10, pady=10)  # Add the button to the left of the frame with padding of 10 pixels


# Create buttons and add them to the frame in the second row
buttons_row2 = []  # List to hold buttons in the second row
for i in range(15):
    button = tk.Button(frame, text=f"{(i+201)}", command=lambda i=i: change_color(buttons_row2[i]))
    button.grid(row=1, column=i, padx=10, pady=10)  # Use grid layout, add the button to the second row
    buttons_row2.append(button)  # Add the button to the list of buttons in the second row
button3 = tk.Button(frame, text="B21", command=lambda: change_color(button3))
button3.grid(row=1, column=16, padx=10, pady=10)
button4 = tk.Button(frame, text="B22", command=lambda: change_color(button4))
button4.grid(row=1, column=17, padx=10, pady=10)  # Add the button to the left of the frame with padding of 10 pixels

buttons_row3 = []  # List to hold buttons in the second row
for i in range(15):
    button = tk.Button(frame, text=f"{(i+301)}", command=lambda i=i: change_color(buttons_row3[i]))
    button.grid(row=2, column=i, padx=10, pady=10)  # Use grid layout, add the button to the second row
    buttons_row3.append(button)  # Add the button to the list of buttons in the second row
button5 = tk.Button(frame, text="B31", command=lambda: change_color(button5))
button5.grid(row=2, column=16, padx=10, pady=10)
button6 = tk.Button(frame, text="B32", command=lambda: change_color(button6))
button6.grid(row=2, column=17, padx=10, pady=10)  # Add the button to the left of the frame with padding of 10 pixels

buttons_row4 = []  # List to hold buttons in the second row
for i in range(15):
    button = tk.Button(frame, text=f"{(i+401)}", command=lambda i=i: change_color(buttons_row4[i]))
    button.grid(row=3, column=i, padx=10, pady=10)  # Use grid layout, add the button to the second row
    buttons_row4.append(button)  # Add the button to the list of buttons in the second row
button7 = tk.Button(frame, text="B41", command=lambda: change_color(button7))
button7.grid(row=3, column=16, padx=10, pady=10)
button8 = tk.Button(frame, text="B42", command=lambda: change_color(button8))
button8.grid(row=3, column=17, padx=10, pady=10)  # Add the button to the left of the frame with padding of 10 pixels
button21 = tk.Button(frame, text="412", bg="red")
button21.grid(row=3, column=11, padx=10, pady=10)

buttons_row5 = []  # List to hold buttons in the second row
for i in range(15):
    button = tk.Button(frame, text=f"{(i+501)}", command=lambda i=i: change_color(buttons_row5[i]))
    button.grid(row=4, column=i, padx=10, pady=10)  # Use grid layout, add the button to the second row
    buttons_row5.append(button)  # Add the button to the list of buttons in the second row
button9 = tk.Button(frame, text="B51", command=lambda: change_color(button9))
button9.grid(row=4, column=16, padx=10, pady=10)
button10 = tk.Button(frame, text="B52", bg="red")
button10.grid(row=4, column=17, padx=10, pady=10)  # Add the button to the left of the frame with padding of 10 pixels

home_button = tk.Button(frame, text="Home", bg="lightblue",command=council)
home_button.grid(row=5, column=8, sticky="NE", padx=10, pady=10)

select_button = tk.Button(frame, text="Select",command=book, bg="lightblue")
select_button.grid(row=6, column=8, sticky="NE", padx=10, pady=10)



# Run the tkinter event loop
root.mainloop()
