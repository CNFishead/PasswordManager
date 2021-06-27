from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip
import json

# Password Generator Project


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ------------------------------------------ SAVE PASSWORD ------------------------------------------------- #
def save():
    # Get Values
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password,}}

    # Basic validation checks
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Blank Entries", message="Please make sure to insert both a Website and a Password.")
    else:
        with open("passwords.json", "r") as file:
            # write the text to file {{website: {email, password}}}
            # has to be loaded before it can be wrote to.
            data = json.load(file)
            data.update(new_data)

        with open("passwords.json", "w") as file:
            # Finally write all the data back to the file.
            json.dump(data, file, indent=4)
            # Delete current values
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# def load():
#     try:
#         with open("passwords.json", "r") as file:
#             # pass

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=300, width=300)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=70)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=70)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=51)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
