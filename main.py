import tkinter as tk
import dhooks

root = tk.Tk()
root.title("Discord Webhook Spammer")
root.geometry("500x400")
root.configure(background='black')

# Creating the title label
title = tk.Label(root, text="\n░██████╗░██████╗░██╗░░░██╗███╗░░██╗░██████╗░███████╗\n██╔════╝░██╔══██╗██║░░░██║████╗░██║██╔════╝░██╔════╝\n██║░░██╗░██████╔╝██║░░░██║██╔██╗██║██║░░██╗░█████╗░░\n██║░░╚██╗██╔══██╗██║░░░██║██║╚████║██║░░╚██╗██╔══╝░░\n╚██████╔╝██║░░██║╚██████╔╝██║░╚███║╚██████╔╝███████╗\n░╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝", fg="red", bg="black", font=("Courier", 11))
title.pack()

# Creating the entry box for webhook URL
url_label = tk.Label(root, text="Enter the Webhook URL:", fg="red", bg="black")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Creating the entry box for the message to be sent
message_label = tk.Label(root, text="Enter the message to be sent:", fg="red", bg="black")
message_label.pack()
message_entry = tk.Entry(root, width=50)
message_entry.pack()

# Creating the entry box for the name of the webhook
name_label = tk.Label(root, text="Enter the name of the webhook:", fg="red", bg="black")
name_label.pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

# Creating the entry box for the number of times to send the message
times_label = tk.Label(root, text="Enter the number of times to send the message:", fg="red", bg="black")
times_label.pack()
times_entry = tk.Entry(root, width=50)
times_entry.pack()

# Function to send webhook message
def send_message():
    # Getting the input values from the user
    webhook_url = url_entry.get()
    message = message_entry.get()
    name = name_entry.get()
    times = int(times_entry.get())

    # Creating the Discord hook
    hook = dhooks.Webhook(webhook_url, username=name)

    # Creating the message to be sent
    for i in range(times):
        hook.send(message)

# Creating the button to send webhook message
send_button = tk.Button(root, text="Send Message", command=send_message, bg="red", fg="black", relief="solid", bd=2, highlightthickness=2, highlightcolor="black")
send_button.pack(pady=10)

root.mainloop()
