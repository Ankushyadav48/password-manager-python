import tkinter as tk
from tkinter import messagebox

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showwarning("Missing", "Please fill in all fields.")
        return

    with open("passwords.txt", "a") as file:
        file.write(f"{website} | {username} | {password}\n")

    messagebox.showinfo("Saved", "Password saved successfully!")

    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def show_passwords():
    try:
        with open("passwords.txt", "r") as file:
            data = file.read()
    except FileNotFoundError:
        data = "No saved passwords."

    new_window = tk.Toplevel(window)
    new_window.title("Saved Passwords")
    new_window.configure(bg="#fff3cd")  

    text_box = tk.Text(new_window, width=50, height=15, bg="#fff8e1", fg="#6b3e26")
    text_box.insert(tk.END, data)
    text_box.config(state="disabled")
    text_box.pack(padx=10, pady=10)

def delete_all_passwords():
    confirm = messagebox.askyesno("Delete All", "Are you sure you want to delete all saved passwords?")
    if confirm:
        try:
            open("passwords.txt", "w").close()
            messagebox.showinfo("Deleted", "All passwords have been deleted.")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")

def delete_specific_password():
    try:
        with open("passwords.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        messagebox.showinfo("No Data", "No saved passwords to delete.")
        return

    if not lines:
        messagebox.showinfo("Empty", "No saved passwords to delete.")
        return

    # Create window for deletion
    del_window = tk.Toplevel(window)
    del_window.title("Delete a Password")
    del_window.configure(bg="#fff3cd")

    tk.Label(del_window, text="Select a password to delete:", bg="#fff3cd", font=("Helvetica", 10, "bold")).pack(pady=5)

    listbox = tk.Listbox(del_window, width=50, height=10, bg="#fff8e1", fg="#4e342e", selectbackground="#ffe0b2")
    listbox.pack(padx=10, pady=5)

    for line in lines:
        listbox.insert(tk.END, line.strip())

    def delete_selected():
        selected_index = listbox.curselection()
        if not selected_index:
            messagebox.showwarning("No Selection", "Please select a password to delete.")
            return
        index = selected_index[0]

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this password?")
        if confirm:
            lines.pop(index)
            with open("passwords.txt", "w") as file:
                file.writelines(lines)
            messagebox.showinfo("Deleted", "Password deleted successfully.")
            del_window.destroy()

    tk.Button(del_window, text="Delete Selected Password", command=delete_selected, bg="#ff8a65", fg="#4e342e").pack(pady=10)

# GUI Setup
window = tk.Tk()
window.title(" Simple Password Manager ")
window.geometry("380x380")
window.configure(bg="#fff3cd") 
label_font = ("Helvetica", 10, "bold")
entry_width = 40

# Labels and Entries
tk.Label(window, text="Website:", bg="#fff3cd", fg="#8b4513", font=label_font).pack(pady=2)
website_entry = tk.Entry(window, width=entry_width)
website_entry.pack()

tk.Label(window, text="Username/Email:", bg="#fff3cd", fg="#8b4513", font=label_font).pack(pady=2)
username_entry = tk.Entry(window, width=entry_width)
username_entry.pack()

tk.Label(window, text="Password:", bg="#fff3cd", fg="#8b4513", font=label_font).pack(pady=2)
password_entry = tk.Entry(window, width=entry_width, show="*")
password_entry.pack()

# Buttons
tk.Button(window, text=" Save Password", 
          command=save_password, bg="#ffcc80", fg="#4e342e").pack(pady=5)

tk.Button(window, text=" Show Saved Passwords",
          command=show_passwords, bg="#ffb74d", fg="#4e342e").pack(pady=5)

tk.Button(window, text=" Delete All Passwords",
          command=delete_all_passwords, bg="#ff7043", fg="#ffffff").pack(pady=5)

tk.Button(window, text=" Delete a Password",
          command=delete_specific_password, bg="#ff8a65", fg="#4e342e").pack(pady=5)

window.mainloop()
