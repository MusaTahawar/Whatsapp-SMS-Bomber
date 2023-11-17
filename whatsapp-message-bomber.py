import tkinter as tk
from tkinter import messagebox
import pywhatkit

def send_single_message():
    phone_number = phone_number_entry.get()
    message = message_entry.get()
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())
    try:
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
        messagebox.showinfo("Success", "Message sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def sms_bomber():
    phone_number = phone_number_entry.get()
    message = message_entry.get()
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())
    times_to_spam = int(times_to_spam_entry.get())
    try:
        for _ in range(times_to_spam):
            pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
        messagebox.showinfo("Success", f"{times_to_spam} messages sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def clear_entries():
    phone_number_entry.delete(0, tk.END)
    message_entry.delete(0, tk.END)
    hour_entry.delete(0, tk.END)
    minute_entry.delete(0, tk.END)
    times_to_spam_entry.delete(0, tk.END)

root = tk.Tk()
root.title("WhatsApp Message Sender")

# Create a frame to organize the UI elements
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

# Labels
labels = ["Phone Number:", "Message:", "Hour (24-hour format):", "Minute:", "Times to spam (if SMS Bomber):"]
for i, label_text in enumerate(labels):
    tk.Label(main_frame, text=label_text).grid(row=i, column=0, sticky="w", padx=5, pady=5)

# Entry fields
phone_number_entry = tk.Entry(main_frame)
message_entry = tk.Entry(main_frame)
hour_entry = tk.Entry(main_frame)
minute_entry = tk.Entry(main_frame)
times_to_spam_entry = tk.Entry(main_frame)

entry_fields = [phone_number_entry, message_entry, hour_entry, minute_entry, times_to_spam_entry]
for i, entry in enumerate(entry_fields):
    entry.grid(row=i, column=1, padx=5, pady=5)

# Buttons
send_single_message_button = tk.Button(main_frame, text="Send Single Message", command=send_single_message)
send_single_message_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

sms_bomber_button = tk.Button(main_frame, text="SMS Bomber", command=sms_bomber)
sms_bomber_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

clear_entries_button = tk.Button(main_frame, text="Clear Entries", command=clear_entries)
clear_entries_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
