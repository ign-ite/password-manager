from tkinter import *
from tkinter import messagebox

#Password Generator
#-----------------------#
#Save Password
def save_pass():
    okcancel = messagebox.askokcancel(title=website_entry.get(),
                                      message=f"The details you've entered are as follows:\n"
                                              f"Email: {email_entry.get()}\n"
                                              f"Password: {password_entry.get()}")
    to_write = f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}"
    src = open('data.json', 'r')
    line = src.readlines()
    is_empty = False
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        is_empty = True
    is_dup = False
    for i in line:
        if i[:len(i) - 1] == to_write:
            is_dup = True
    src.close()
    if not is_dup and okcancel and not is_empty:
        with open('data.txt', 'a') as data:
            data.write(f"{to_write}")
            data.write("\n")
        messagebox.showinfo("Password Saved", "Password Saved Successfully!")
    elif not okcancel:
        messagebox.showinfo("Save Cancelled.", "Password Save Cancelled!")
    elif is_dup:
        print("Password already saved!")
        messagebox.showinfo("Error: Saved!", "Password already saved!")
    elif is_empty:
        messagebox.showinfo("Error: Empty Submission", "Do not leave the fields empty!")
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()
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