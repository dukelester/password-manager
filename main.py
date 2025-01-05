from tkinter import *
from tkinter import messagebox
import json
from password_generator import password_generator
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    my_password = password_generator()
    password_entry.delete(0, END)
    password_entry.insert(0, my_password)
    pyperclip.copy(my_password)


def search():
    website = website_entry.get().strip()
    if website is None or website == '':
        messagebox.showerror(title="Error", message="Search word cannot be empty!")
        return
    print(website)
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            print(data)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror(title="Error", message="No data file found!")
        return
    if website in data:
        email = data[website]['email']
        my_password = data[website]['password']
        messagebox.showinfo(title=website, message=f'Email: {email} \n Password: {my_password}')
        pyperclip.copy(my_password)
    else:
        messagebox.showerror(title="Error", message=f"No details found for: {website}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    my_password = password_entry.get().strip()

    if not website or not email or not my_password:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")
        return

    new_data = {
        website: {
            "email": email,
            "password": my_password
        }
    }

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            print(data)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data.update(new_data)

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    messagebox.showinfo(title="Success", message="Details saved successfully!")
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='white')

# Canvas
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_image = PhotoImage(file='assests/logo.png')
canvas.create_image(100, 115, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.insert(0, "duke@lester.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)
search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
