from tkinter import *
from simplecrypt import encrypt, decrypt
from tkinter import filedialog
import os

root = Tk()
root.geometry("400x250")
root.configure(bg="orange")
def decry():
    path = filedialog.askopenfilename(title="Select file",filetypes=[("Text Files", "*.txt")])
    f=open(path,"r")
    byte_str=bytes.fromhex(f.read())
    original=decrypt("AIM",byte_str)
    final_message=original.decode("utf-8")
    print(final_message)
    decryption_text_data.insert(END,final_message)
def startDecryption():
    global file_name_entry
    global decryption_text_data
    root.destroy()
 
    decryption_window = Tk()
    decryption_window.geometry("600x500")
    decryption_window.configure(bg="orange")
    decryption_text_data = Text(decryption_window, height=20, width=72)
    decryption_text_data.place(relx=0.5,rely=0.35, anchor=CENTER)
    
    btn_open_file = Button(decryption_window, text="Choose File..", font = 'arial 13',command=decry,bg="gold")
    btn_open_file.place(relx=0.5,rely=0.8, anchor=CENTER)
    
    decryption_window.mainloop()
    
def create():
    f = open(file_name_entry.get()+".txt", "w")
    ciphercode=encrypt("AIM",encryption_text_data.get(1.0,END))
    hex_string=ciphercode.hex()
    print(hex_string)
    f.write(hex_string)
    f.close()
    print("done")
def startEncryption():
    global file_name_entry
    global encryption_text_data
    root.destroy()
 
    encryption_window = Tk()
    encryption_window.geometry("600x500")
    encryption_window.configure(bg="orange")
    
    file_name_label = Label(encryption_window, text="File Name: " , font = 'arial 13',bg="orange")
    file_name_label.place(relx=0.1,rely=0.15, anchor=CENTER)
    
    file_name_entry = Entry(encryption_window, font = 'arial 15')
    file_name_entry.place(relx=0.38,rely=0.15, anchor=CENTER)
    
    btn_create = Button(encryption_window, text="Create", font = 'arial 13',command=create,bg="gold")
    btn_create.place(relx=0.75,rely=0.15, anchor=CENTER)
    
    encryption_text_data = Text(encryption_window, height=20, width=72)
    encryption_text_data.place(relx=0.5,rely=0.55, anchor=CENTER)
    
    encryption_window.mainloop()
    
    
heading_label = Label(root, text="Encryption & Decryption" , font = 'arial 18 italic',bg="orange")
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

btn_start_encryption = Button(root, text="Start Encryption" , font = 'arial 13' , command=startEncryption,bg="gold")
btn_start_encryption.place(relx=0.3,rely=0.6, anchor=CENTER)

btn_start_decryption = Button(root, text="Start Decryption" , font = 'arial 13' ,  command=startDecryption,bg="gold")
btn_start_decryption.place(relx=0.7,rely=0.6, anchor=CENTER)

root.mainloop()