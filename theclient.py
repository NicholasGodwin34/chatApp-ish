import socket as sc
import threading as tr 
import tkinter as tk 
import ssl 
from tkinter import simpledialog as sd


HOST = '127.0.0.1'
PORT = 12897

# create ssl context and wrap the client socket 
ssl_context = ssl.create_default_context()
    #if using self signed certificates, disable verification(only for testing)
    #ssl_context.check_hostname = false
    #ssl_context.verify_mode = ssl.CERT_NONE


# setting up the client
raw_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
c_socket = ssl_context.wrap_socket(raw_socket, server_hostname=HOST)
c_socket.connect((HOST , PORT))



# Function to  receive messages from the server
def receive_msg():
    while True : 
        try: 
            msg = c_socket.recv(1024).decode('utf-8')
            if msg: 
                chat_box.config(state='normal') # allow editing temporarily
                chat_box.insert(tk.END, msg + '\n') # add message at the end 
                chat_box.config(state='disabled') # disable editing again 
                chat_box.see(tk.END) # Automatically scroll to the newest message
        except: 
            print("Connection to server lost.")
            break 

# Function to send messages to the server 
def send_msg(event=None): 
    msg=msg_entry.get()
    if msg: 
        #prefix the message with the username 
        full_msg = f"{username}: {msg}"
        c_socket.send(msg.encode('utf-8')) # send to server
        # display the message with the username
        chat_box.config(state='normal')
        chat_box.insert(tk.END, full_msg   + '\n') # Add username
        chat_box.config(state='disabled')
        chat_box.see(tk.END)
        msg_entry.delete(0, tk.END) # clear the input field 

#Function to prompt for username using GUI 
def ask_username(): 
    global username 
    user_prompt = tk.Toplevel(root) # create a popup window
    user_prompt.title("Enter Your username")

    tk.Label(user_prompt, text="Please enter your username: ").pack(pady=10)
    user_entry=tk.Entry(user_prompt)
    user_entry.pack(pady=10)

    def submit_username(): 
        nonlocal user_entry
        username = user_entry.get()
        if username: 
            user_prompt.destroy() # close the popup 
            start_chat(username) # start the chat application
        else : 
            tk.Label(user_prompt, text="Username cannot be empty! ", fg="red").pack()

    tk.Button(user_prompt, text="submit", command=submit_username).pack(pady=10)
    user_prompt.protocol("WM_DELETE_WINDOW", root.destroy)  # close app if user exits popup


# function to initialize the chat after username is set 
def start_chat(user): 
    global username 
    username=user # save the username globally 

    #create chat interface 
    chat_box.pack()
    msg_entry.pack()
    send_button.pack()
    
    # start thread to receive messages
    tr.Thread(target=receive_msg, daemon=True ).start()
    # Bind the "Enter" key to send messages
    root.bind("<Return>", send_msg)


# Create the GUI 
root = tk.Tk()
root.title("Chat Application")

chat_box = tk.Text(root, height=20, width=50, state='disabled') # chat display
chat_box.pack()

msg_entry = tk.Entry(root, width=50) # input field
msg_entry.pack()

send_button = tk.Button(root, text="send", command=send_msg) # send button
send_button.pack()

# Start with a username prompt
ask_username()

# Run the tkinter event loop 
root.mainloop()


