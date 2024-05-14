import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone: 
        new_contact = Contact(name, phone, email, address)
        contacts.append(new_contact)
        clear_entries()
        messagebox.showinfo("Success", "Contact added successfully.")
    else:
        messagebox.showerror("Error", "Name and Phone number are required.")


def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

def view_contact_list():
    update_contact_list()


def delete_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        selected_contact_index = selected_contact[0]
        del contacts[selected_contact_index]
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact deleted successfully.")
    else:
        messagebox.showerror("Error", "Select a contact to delete.")


def search_contact():
    query = search_entry.get()
    contact_listbox.delete(0, tk.END)
    found = False
    for contact in contacts:
        if query.lower() in contact.name.lower() or query in contact.phone:
            contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")
            found = True
    if not found:
        contact_listbox.insert(tk.END, "No contacts found.")

def update_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        selected_contact_index = selected_contact[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        if name and phone: 
            contacts[selected_contact_index].name = name
            contacts[selected_contact_index].phone = phone
            contacts[selected_contact_index].email = email
            contacts[selected_contact_index].address = address
            update_contact_list()
            clear_entries()
            messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            messagebox.showerror("Error", "Name and Phone number are required.")
    else:
        messagebox.showerror("Error", "Select a contact to update.")       


root = tk.Tk()
root.title("Contact Management System")

root.configure(bg="#7B68EE")


tk.Label(root, text="Name:",font=("Times New Roman", 13),bg="#87CEFA").grid(row=0, column=0)
name_entry = tk.Entry(root,width=50,font=("Verdana",10),bg="#CCCCFF")
name_entry.grid(row=0, column=1,padx=30,pady=10)

tk.Label(root, text="Phone:",font=("Times New Roman", 13),bg="#87CEFA").grid(row=1, column=0)
phone_entry = tk.Entry(root,width=50,font=("Verdana",10),bg="#CCCCFF")
phone_entry.grid(row=1, column=1,pady=10)

tk.Label(root, text="Email:",font=("Times New Roman", 13),bg="#87CEFA").grid(row=2, column=0)
email_entry = tk.Entry(root,width=50,font=("Verdana",10),bg="#CCCCFF")
email_entry.grid(row=2, column=1,pady=10)

tk.Label(root, text="Address:",font=("Times New Roman", 13),bg="#87CEFA").grid(row=3, column=0)
address_entry = tk.Entry(root,width=50,font=("Verdana",10),bg="#CCCCFF")
address_entry.grid(row=3, column=1,pady=10)

add_button = tk.Button(root, text="Add Contact", command=add_contact,font=("Georgia",12),bg="#32CD32")
add_button.grid(row=4, column=0, columnspan=2)


delete_button = tk.Button(root, text="Delete Contact", command=delete_contact,font=("Georgia",11),bg="#FF4500",fg="black")
delete_button.grid(row=9, column=2,sticky=tk.W,padx=10,pady=10)

tk.Label(root, text="Search :",font=("Georgia",10),bg="#87CEFA").grid(row=5, column=1, sticky=tk.W)
search_entry = tk.Entry(root,width=40,bg="#CCCCFF",font=("Verdana",10))
search_entry.grid(row=5, column=1,pady=20)

search_button = tk.Button(root, text="Search",padx=10, command=search_contact,font=("Georgia",10),bg="#32CD32")
search_button.grid(row=6, column=1)

update_button = tk.Button(root, text="Update Contact", command=update_contact,font=("Georgia",11),bg="#32CD32")
update_button.grid(row=9,column=1,pady=10)


view_button = tk.Button(root, text="View Contact", command=view_contact_list,font=("Georgia",11),bg="#32CD32")
view_button.grid(row=9, column=0,sticky=tk.W,padx=30,pady=10)

contact_listbox = tk.Listbox(root, width=100, height=10,bg="#AFEEEE",font=("Verdana",10))
contact_listbox.grid(row=7, column=0, columnspan=3,pady=10,padx=5)

root.mainloop()
