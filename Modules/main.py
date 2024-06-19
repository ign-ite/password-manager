import json
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import random
import pyperclip


#Load previously generated key
#------------------------#
def load_key():
    return open("../Data/secret.key", "rb").read()


key = load_key()
fernet = Fernet(key)


def encrypt_message(message):
    return fernet.encrypt(message.encode()).decode()


def decrypt_message(encrypted_message):
    return fernet.decrypt(encrypted_message.encode()).decode()


#Password Generator
#-----------------------#
def password_generate():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = 12
    nr_symbols = 4
    nr_numbers = 5

    lettersInPass = ([random.choice(letters) for i in range(nr_letters)]
                     + [random.choice(symbols) for i in range(nr_symbols)]
                     + [random.choice(numbers) for i in range(nr_numbers)])

    random.shuffle(lettersInPass)

    randomPass = "".join(lettersInPass)

    password_entry.insert(END, randomPass)

    pyperclip.copy(randomPass)


#Save Password
def save_pass():
    password = password_entry.get()

    encrypted_password = encrypt_message(password)
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": encrypted_password,
        }
    }
    okcancel = messagebox.askokcancel(title=website_entry.get(),
                                      message=f"The details you've entered are as follows:\n"
                                              f"Email: {email_entry.get()}\n"
                                              f"Password: {password_entry.get()}")
    to_write = f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}"

    if not okcancel:
        return

    if len(website_entry.get()) == 0 and len(password_entry.get()) == 0:
        messagebox.showinfo(title="Error: Empty Field!", message="Do not leave the fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                try:
                    # Reading old data
                    data = json.load(data_file)
                except json.JSONDecodeError:
                    data = {}
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            encrypted_password = data[website]["password"]
            password = decrypt_message(encrypted_password)
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


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
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=39)
email_entry.insert(0, "varuntheace@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

generate_password = Button(text="Generate Password", width=14, command=password_generate)
generate_password.grid(row=3, column=2)

add_password_button = Button(text="Add", command=save_pass)
add_password_button.config(width=33)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
