from tkinter import *
import random

root=Tk()
root.title("random password")
root.geometry("500x500")

label1=Label(root, text="Your password is: ")


def password():
    alpha_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alpha_let1=random.randint(0,25)
    alpha_let2=random.randint(0,25)
    alpha_let3=random.randint(0,25)
    alpha_let4=random.randint(0,25)
    alpha_let5=random.randint(0,25)
    
    letter1=alpha_letters[alpha_let1]
    letter2=alpha_letters[alpha_let2]
    letter3=alpha_letters[alpha_let3]
    letter4=alpha_letters[alpha_let4]
    letter5=alpha_letters[alpha_let5]
    label1["text"]="Your password is: " + letter1+letter2+letter3+letter4+letter5
    
btn=Button(root,text="Generate password", command=password)
btn.pack()

label1.pack()



root.mainloop()