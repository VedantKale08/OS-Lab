import os
from tkinter import *
import getpass
import socket

def execute_command():

    input = command.get()
    
    output_text.insert(END, f' {input}\n')

    if input.lower() == "exit":
        root.destroy()
        return

   
    try:
        if(input == "history"):
            output = os.popen("cat /home/vedant/.bash_history").read()  
        elif(input == "top"):
            output = os.popen("ps aux").read()  
        else:
            output = os.popen(input).read()
        output_text.insert(END, output)
    except Exception as e:
        output_text.insert(END, f"Error executing command: {e}\n")

    command.delete(0,END)
    output_text.insert(END, f"{username}@{hostname} ~ ")


if __name__ == "__main__":

    root = Tk()
    root.title("Terminal")
    root.configure(bg="#000")
    root.resizable(False,False)

    username = getpass.getuser()
    hostname = socket.gethostname()

    output_text = Text(root, wrap=WORD, width=80, height=30, bg="#000", fg="#fff")
    output_text.grid(row=0, column=0, padx=10, pady=10)

    scrollbar = Scrollbar(root, command=output_text.yview)
    scrollbar.grid(row=0, column=1, sticky='nsew')
    output_text.config(yscrollcommand=scrollbar.set)

    output_text.insert(END, f"{username}@{hostname} ~")

    command = Entry(root, width=80 , bg="#000", fg="#fff", insertbackground="#fff")
    command.grid(row=1, column=0, padx=10, pady=10, ipady=5)

    # Create a button to execute the command
    execute_button = Button(root, text="Execute", command=execute_command,bg="#000", fg="#fff")
    execute_button.grid(row=2, column=0, pady=10, padx=10, sticky=W)

    root.mainloop()

