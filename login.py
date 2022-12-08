from tkinter import *

# Making main windows of tkinter
root = Tk()

root.geometry("580x300")
root.title('Login Form')

# Creating elements

loginPageLb = Label(root, text='Login Page', font=('Poppins', 18))

usernameLb = Label(root, text='Username:', font=('Poppins', 18))

usernameEt = Entry(root, font=('Poppins', 18))

passwordLb = Label(root, text='Password:', font=('Poppins', 18))

passwordEt = Entry(root, font=('Poppins', 18))



LoginBtn = Button(text='Login', font=('Poppins', 18))



createLb = Label(root, text='Dont have account? Create one here', font=('Poppins', 18))


# showing the elements
loginPageLb.grid(row=0, column=1)

usernameLb.grid(row=2, column=0)
usernameEt.grid(row=2, column=1)

passwordLb.grid(row=3, column=0)
passwordEt.grid(row=3, column=1)

LoginBtn.grid(row=5, column=1)

createLb.grid(row=8, column=1)


# keep running the program until user closes it
root.mainloop()