import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def register():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    event = event_var.get()

    if not name or not email or not phone or event == "Select Event":
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    # Here you could also write the data to a file or database
    messagebox.showinfo("Registration Successful",
                        f"Thank you, {name}!\nYou have registered for the {event}.")

    # Clear form after registration
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    event_var.set("Select Event")

# Create the main window
root = tk.Tk()
root.title("Event Registration Form")
root.geometry("400x400")
root.configure(bg="#f4f7fa")

# Heading
tk.Label(root, text="Event Registration", font=("Arial", 18, "bold"), bg="#f4f7fa").pack(pady=10)

# Name
tk.Label(root, text="Full Name:", font=("Arial", 12), bg="#f4f7fa").pack(anchor="w", padx=30)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=30, pady=5)

# Email
tk.Label(root, text="Email:", font=("Arial", 12), bg="#f4f7fa").pack(anchor="w", padx=30)
email_entry = tk.Entry(root, width=40)
email_entry.pack(padx=30, pady=5)

# Phone
tk.Label(root, text="Phone:", font=("Arial", 12), bg="#f4f7fa").pack(anchor="w", padx=30)
phone_entry = tk.Entry(root, width=40)
phone_entry.pack(padx=30, pady=5)

# Event selection
tk.Label(root, text="Select Event:", font=("Arial", 12), bg="#f4f7fa").pack(anchor="w", padx=30)
event_var = tk.StringVar(value="Select Event")
events = ["Tech Talk", "Workshop", "Hackathon"]
event_menu = tk.OptionMenu(root, event_var, *events)
event_menu.pack(padx=30, pady=5)

# Submit button
tk.Button(root, text="Register", command=register, bg="#4CAF50", fg="white",
          font=("Arial", 12, "bold"), width=15).pack(pady=20)

# Run the app
root.mainloop()
