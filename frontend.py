from tkinter import *
from tkinter import ttk, messagebox
from backend import UserDatabase
import time


class UserManagementApp:
    def __init__(self, root):
        self.db = UserDatabase()

        # Variables
        self.name_var = StringVar()
        self.phone_var = StringVar()
        self.email_var = StringVar()
        self.address_var = StringVar()
        self.gender_var = StringVar()
        self.dob_var = StringVar()

        # GUI setup
        self.root = root
        self.root.title("User Management System")
        self.root.geometry("900x500")

        self.setup_ui()

    def setup_ui(self):
        # Labels and Entry Widgets
        Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        Entry(self.root, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=10)

        Label(self.root, text="Phone:").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        Entry(self.root, textvariable=self.phone_var).grid(row=1, column=1, padx=10, pady=10)

        Label(self.root, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        Entry(self.root, textvariable=self.email_var).grid(row=2, column=1, padx=10, pady=10)

        Label(self.root, text="Address:").grid(row=3, column=0, padx=10, pady=10, sticky=W)
        Entry(self.root, textvariable=self.address_var).grid(row=3, column=1, padx=10, pady=10)

        Label(self.root, text="Gender:").grid(row=4, column=0, padx=10, pady=10, sticky=W)
        Entry(self.root, textvariable=self.gender_var).grid(row=4, column=1, padx=10, pady=10)

        Label(self.root, text="DOB:").grid(row=5, column=0, padx=10, pady=10, sticky=W)
        Entry(self.root, textvariable=self.dob_var).grid(row=5, column=1, padx=10, pady=10)

        # Buttons
        self.connect_button = Button(self.root, text="Connect to Database", command=self.connect_database)
        self.connect_button.grid(row=6, column=0, padx=10, pady=20)

        self.add_button = Button(self.root, text="Add", command=self.add_user, state=DISABLED)
        self.add_button.grid(row=6, column=1, padx=10, pady=20)

        self.delete_button = Button(self.root, text="Delete", command=self.delete_user, state=DISABLED)
        self.delete_button.grid(row=6, column=2, padx=10, pady=20)

        self.edit_button = Button(self.root, text="Edit", command=self.edit_user, state=DISABLED)
        self.edit_button.grid(row=6, column=3, padx=10, pady=20)

        self.show_users_button = Button(self.root, text="Show List", command=self.show_users, state=DISABLED)
        self.show_users_button.grid(row=6, column=4, padx=10, pady=20)

        # Treeview
        columns = ('ID', 'Name', 'Phone', 'Email', 'Address', 'Gender', 'DOB', 'Date', 'Time')
        self.user_table = ttk.Treeview(self.root, columns=columns, show='headings')
        for col in columns:
            self.user_table.heading(col, text=col)
            self.user_table.column(col, width=100)
        self.user_table.grid(row=7, column=0, columnspan=6, padx=10, pady=10)

    def connect_database(self):
        status, message = self.db.connect()
        messagebox.showinfo(status, message)
        if status == "Success":
            self.enable_buttons()

    def enable_buttons(self):
        self.add_button.config(state=NORMAL)
        self.delete_button.config(state=NORMAL)
        self.edit_button.config(state=NORMAL)
        self.show_users_button.config(state=NORMAL)

    def add_user(self):
        data = (self.name_var.get(), self.phone_var.get(), self.email_var.get(),
                self.address_var.get(), self.gender_var.get(), self.dob_var.get(),
                time.strftime('%d/%m/%Y'), time.strftime('%H:%M:%S'))
        status, message = self.db.add_user(data)
        messagebox.showinfo(status, message)
        if status == "Success":
            self.clear_entries()
            self.show_users()

    def show_users(self):
        status, result = self.db.fetch_users()
        if status == "Error":
            messagebox.showerror(status, result)
        else:
            self.user_table.delete(*self.user_table.get_children())
            for row in result:
                self.user_table.insert('', END, values=row)

    def delete_user(self):
        selected_item = self.user_table.focus()
        if not selected_item:
            messagebox.showerror("Error", "No User Selected")
            return
        user_id = self.user_table.item(selected_item)['values'][0]
        status, message = self.db.delete_user(user_id)
        messagebox.showinfo(status, message)
        if status == "Success":
            self.show_users()

    def edit_user(self):
        # Implementation for editing user details (similar to adding users)
        pass

    def clear_entries(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")
        self.gender_var.set("")
        self.dob_var.set("")


if __name__ == "__main__":
    root = Tk()
    app = UserManagementApp(root)
    root.mainloop()
