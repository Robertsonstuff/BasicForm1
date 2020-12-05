
from tkinter import *

def save_info():
    #print("hello Luke")
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()
    age_info = str(age_info)
    print(firstname_info, lastname_info, age_info)

    file = open("user.txt", "a+")
    file.write(firstname_info + " ")
    file.write(lastname_info + " ")
    file.write(age_info + "\n")
    print(" User ", firstname_info, "registered successfully")
    file.close

    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    age_entry.delete(0, END)

root = Tk()
root.geometry("500x500")
root.title("Luke's Basic Form")
heading = Label(root,
text = "Python Form", bg = "white", fg = "black", width = "500", height = "3")
heading.pack()

firstname_text = Label(root,
text = "Firstname * ",)
lastname_text = Label(root,
text = "Lastname * ",)
age_text = Label(root,
text = "Age * ",)
firstname_text.place(x = 15, y = 70)
lastname_text.place(x = 15, y = 140)
age_text.place(x = 15, y = 210)

firstname = StringVar()
lastname = StringVar()
age = IntVar()

firstname_entry = Entry(textvariable = firstname, width = "30")
lastname_entry = Entry(textvariable = lastname, width = "30")
age_entry = Entry(textvariable = age, width = "15")

firstname_entry.place(x = 15, y = 100)
lastname_entry.place(x = 15, y = 170)
age_entry.place(x = 15, y = 240)

register = Button(root,text = "Register", width = "30", height = "2", command = save_info, bg = "grey")
register.place(x = 15, y = 290)

root.mainloop()