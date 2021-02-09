
from tkinter import *


def save_info():
    #print("hello Luke")
    Status_info = Status.get()
    FriendlyName_info = FriendlyName.get()
    Asset_info = Asset.get()
    CIType_info = CIType.get()
    Model_info = Model.get()
    PrimaryContact_info = PrimaryContact.get()
    BuildingLocation_info = BuildingLocation.get()
    RoomLocation_info = RoomLocation.get()
	
    top = Toplevel()
    top.title('output')
    top.geometry("400x250")
    top.title("Output form")
    T = Text(top, height=15, width=30)
    T.pack()
    T.insert(END, 10*"-" + "\n" + "Status: " + Status_info + "\n")
    T.insert(END, "Friendly Name: " + FriendlyName_info + "\n")
    T.insert(END, "Alt CI ID: " + FriendlyName_info + "\n")
    T.insert(END, "Serial Number: " + FriendlyName_info + "\n")
    T.insert(END, "Asset Number: " + Asset_info + "\n")
    T.insert(END, "CI Type: " + CIType_info + "\n")
    T.insert(END, "Model: " + Model_info + "\n")
    T.insert(END, "Primary Contact: " + PrimaryContact_info + "\n")
    T.insert(END, "Building Location: " + BuildingLocation_info + "\n")
    T.insert(END, "Room Location: " + RoomLocation_info + "\n" + 10*"-" + "\n")

    Status_entry.delete(0, END)
    FriendlyName_entry.delete(0, END)
    Asset_entry.delete(0, END)
    CIType_entry.delete(0, END)
    Model_entry.delete(0, END)
    PrimaryContact_entry.delete(0, END)
    BuildingLocation_entry.delete(0, END)
    RoomLocation_entry.delete(0, END)

    root.quit()
    top.mainloop()
    

root = Tk()
root.geometry("400x700")
root.title("Luke's CI Form")
heading = Label(root, text = "CI Form", bg = "white", fg = "black", width = "500", height = "3")
heading.pack()


# 10 fields being status, friendly name, Alt CI ID, Serial Number, Asset, CI type, Model, Primary Contact, Location Building, Location room.

Status_text = Label(root,
text = "Status * ",)
FriendlyName_text = Label(root,
text = "Friendly Name *, Alt CI ID *, Serial Number * ",)
Asset_text = Label(root,
text = "Asset Number * ",)
CIType_text = Label(root,
text = "CI Type * ",)
Model_text = Label(root,
text = "Model * ",)
PrimaryContact_text = Label(root,
text = "Primary Contact * ",)
BuildingLocation_text = Label(root,
text = "Building Location * ",)
RoomLocation_text = Label(root,
text = "Room Location * ",)

Status_text.place(x = 15, y = 60)
FriendlyName_text.place(x = 15, y = 120)
Asset_text.place(x = 15, y = 180)
CIType_text.place(x = 15, y = 240)
Model_text.place(x = 15, y = 300)
PrimaryContact_text.place(x = 15, y = 360)
BuildingLocation_text.place(x = 15, y = 420)
RoomLocation_text.place(x = 15, y = 480)

Status = StringVar()
FriendlyName = StringVar()
Asset = StringVar()
CIType = StringVar()
Model = StringVar()
PrimaryContact = StringVar()
BuildingLocation = StringVar()
RoomLocation = StringVar()

Status_entry = Entry(textvariable = Status, width = "20")
FriendlyName_entry = Entry(textvariable = FriendlyName, width = "20")
Asset_entry = Entry(textvariable = Asset, width = "20")
CIType_entry = Entry(textvariable = CIType, width = "20")
Model_entry = Entry(textvariable = Model, width = "20")
PrimaryContact_entry = Entry(textvariable = PrimaryContact, width = "35")
BuildingLocation_entry = Entry(textvariable = BuildingLocation, width = "35")
RoomLocation_entry = Entry(textvariable = RoomLocation, width = "20")

Status_entry.place(x = 15, y = 80)
FriendlyName_entry.place(x = 15, y = 140)
Asset_entry.place(x = 15, y = 200)
CIType_entry.place(x = 15, y = 260)
Model_entry.place(x = 15, y = 320)
PrimaryContact_entry.place(x = 15, y = 380)
BuildingLocation_entry.place(x = 15, y = 440)
RoomLocation_entry.place(x = 15, y = 500)

register = Button(root,text = "Register", width = "30", height = "2", command = save_info, bg = "grey")
register.place(x = 15, y = 600)


root.mainloop()

