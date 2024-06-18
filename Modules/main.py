from tkinter import *
from tkinter import messagebox

#Password Generator
#-----------------------#
#Save Password
#-----------------------#
#UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

lockimg = "../Src/logo.png"
lock_image = Canvas(bg="white", height=200, width=200, highlightthickness=0)
lock = PhotoImage(file=lockimg)
lock_image.create_image(100, 100, image=lock)
lock_image.grid(row=0, column=1)

#Labels
website_label = Label(text="Website: ", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ", bg="white")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=40)
email_entry.insert(0, "varuntheace@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=40)
password_entry.grid(row=3, column=1, columnspan=2)

#Buttons
generate_password = Button(text="Generate Password", width=14)
generate_password.grid(row=3, column=2)

add_password_button = Button(text="Add")
add_password_button.config(width=34)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()