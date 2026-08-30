import tkinter as tk

#--Backend code--#
def encryptor(message, shift_number):
    encrypted_result = ""
    for char in message:
        if char == " ":
            encrypted_result = encrypted_result + char
        else:  
            ascii_value = ord(char)
            encryption = chr(ascii_value + shift_number)
            encrypted_result = encrypted_result + encryption
    return encrypted_result

def descrambler(message, shift_number):
    descrambled_result = ""
    for char in message:
        if char == " ":
            descrambled_result = descrambled_result + char
        else:
            ascii_value = ord(char)
            decrypted = chr(ascii_value - shift_number)
            descrambled_result = (descrambled_result + decrypted)
    return descrambled_result



#--GUI--#

def update_result_box(output_text):
    text_result.config(state="normal")
    text_result.delete("1.0", tk.END)
    text_result.insert("1.0", output_text)
    text_result.config(state="disabled")
    



def run_encryption():
    text_encryption = user_text_input.get("1.0", tk.END).strip()

    encryptor_output = encryptor(text_encryption, 3)
    
    update_result_box(encryptor_output)

def run_decryption():
    text_decryption = user_text_input.get("1.0", tk.END).strip()

    decryptor_output = descrambler(text_decryption, 3)

    update_result_box(decryptor_output)

def copy_to_clipboard():
    result_text = text_result.get("1.0", tk.END).strip()
    
    if result_text:
        window.clipboard_clear()
        window.clipboard_append(result_text)





window = tk.Tk()
window.geometry ("420x420")
window.title("Encrypter/Decrypter")

label_title = tk.Label(
    window,
    text="---Simple Encryptor/Decryptor---",
    font=("arial", 16, "bold"),
    fg ="red",
    bg ="black",
    bd = 10,
    relief = "raised"
    )

label_title.grid(row=0, column=0, columnspan=2, ipadx=10, ipady=10, sticky="ew")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

user_text_input = tk.Text(
    window,
    font=("arial", 12),
    bd=2,
    relief="solid",
    height = 5
    )
user_text_input.grid(row=2, column=0, columnspan=2, sticky = "ew", pady = 10)


button_encrypt =tk.Button(
    window,
    text = "Encrypt code",
    font = ("arial", 12, "bold"),
    command=run_encryption
    )

button_encrypt.grid(row=1, column=0, pady=10)




button_decrypt = tk.Button(
    window,
    text="Decrypt code",
    font = ("arial", 12, "bold"),
    command=run_decryption
    )

button_decrypt.grid(row=1,column=1,pady=10)


text_result = tk.Text(
    window,
    font=("arial", 12, "bold"),
    state = "disabled",
    height=5,
    bg = "grey",
    bd = 2,
    relief = "solid"
    )

text_result.grid(row=3, column=0, columnspan=2, sticky="ew")



copy_button = tk.Button(
    window,
    text = "copy to clipboard",
    font =("arial", 12, "bold"),
    fg = "black",
    height = 2,
    command=copy_to_clipboard
    )

copy_button.grid(row=4, column=0, columnspan=2, pady=10, padx=5, sticky = "e")
    

window.mainloop()
