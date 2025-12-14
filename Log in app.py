# Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Login App')
root.geometry('400x400')

# Create a frame to organize elements better
frame = Frame(master=root, height=200, width=360, bg="#d0efff")

# Add widgets
# Add Label
lbl1 = Label(frame, text="Full Name", bg="#3895D3", fg='white', width=12)
lbl2 = Label(frame, text="Email Id", bg="#3895D3", fg='white', width=12)
lbl3 = Label(frame, text="Enter Password", bg="#3895D3", fg='white', width=12)
# Use Entry Widget to create a text box for user to enter details
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

# Function to display message
def display():
    name = name_entry.get()

