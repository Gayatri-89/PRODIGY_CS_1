from tkinter import *
from tkinter import messagebox

# Caesar cipher encryption
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Caesar cipher decryption
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def decrypt():
    try:
        shift = int(code.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number as the key.")
        return

    message = text1.get(1.0, END)
    decrypted_text = caesar_decrypt(message.strip(), shift)

    screen2 = Toplevel(screen)
    screen2.title("Decryption")
    screen2.geometry("400x200")
    screen2.configure(bg="#00bd56")

    Label(screen2, text="DECRYPTED TEXT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
    text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text2.place(x=10, y=40, width=380, height=150)
    text2.insert(END, decrypted_text)

def encrypt():
    try:
        shift = int(code.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number as the key.")
        return

    message = text1.get(1.0, END)
    encrypted_text = caesar_encrypt(message.strip(), shift)

    screen1 = Toplevel(screen)
    screen1.title("Encryption")
    screen1.geometry("400x200")
    screen1.configure(bg="#ed3833")

    Label(screen1, text="ENCRYPTED TEXT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
    text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text2.place(x=10, y=40, width=380, height=150)
    text2.insert(END, encrypted_text)

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("Caesar Cipher App")

    try:
        image_icon = PhotoImage(file="C:/Users/gayat/OneDrive/Desktop/Encryption and Decryption/keys.png")
        screen.iconphoto(False, image_icon)
    except:
        pass  # Skip icon if not valid

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter shift value (key)", fg="black", font=("calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25)).place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
