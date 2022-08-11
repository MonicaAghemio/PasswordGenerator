from tkinter import *
from random import randint

root = Tk()
root.title('Password generator')
# root.iconbitmap('Python/passW-generator/password.ico')
root.geometry("500x300")

my_password = chr(randint(33, 126))


def new_rand():
    # clear entry box
    pw_entry.delete(0, END)
    # convert pw length and convert to int
    pw_length = int(my_entry.get())

    # creates a variable to hold password
    my_password = ''

    # loop through password length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    # password on the screen
    pw_entry.insert(0, my_password)

# copy to clipboard


def clipper():
    # clear clipboard
    root.clipboard_clear()
    # copy to clipboard
    root.clipboard_append(pw_entry.get())


# Label Frame
lF = LabelFrame(root, text="How many characters password? ")
lF.pack(pady=20)

# Entry box for number of characters
my_entry = Entry(lF, font=("Arial", 24))
my_entry.pack(pady=20, padx=20)

# entry box for returned password
pw_entry = Entry(root, text='', font=('Arial', 24),
                 bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

# frame for buttons
my_frame = Frame(root)
my_frame. pack(pady=20)

# buttons
my_button = Button(my_frame, text="Generate password", command=new_rand)
my_button.grid(row=0, column=0,  padx=10)


clip_button = Button(my_frame, text="Copy to clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)


root.mainloop()
