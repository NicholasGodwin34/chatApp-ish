import socket as sc
import threading as tr 
import tkinter as tk 


HOST = '127.0.0.1'
PORT = 12897
# setting up the client
c_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
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
        c_socket.send(msg.encode('utf-8')) # send to server
        chat_box.config(state='normal')
        chat_box.insert(tk.END, "You: " + msg + '\n') # display  in chat box 
        chat_box.config(state='disabled')
        chat_box.see(tk.END)
        msg_entry.delete(0, tk.END) # clear the input field 

# Create the GUI 
root = tk.Tk()
root.title("Chat Application")

chat_box = tk.Text(root, height=20, width=50)
chat_box.pack()

msg_entry = tk.Entry(root, width=50)
msg_entry.pack()

send_button = tk.Button(root, text="send", command=send_msg)
send_button.pack()

#start thread to receive messages 
root.bind("<Return>", send_msg)

# Run the tkinter event loop 
root.mainloop()


