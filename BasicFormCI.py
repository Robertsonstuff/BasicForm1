
from tkinter import *


def save_info():
    #print("hello Luke")
    Status_info = Status.get()
    FriendlyName_info = FriendlyName.get()
    AltCI_info = AltCI.get()
    Serial_info = Serial.get()
    Asset_info = Asset.get()
    CIType_info = CIType.get()
    Model_info = Model.get()
    PrimaryContact_info = PrimaryContact.get()
    BuildingLocation_info = BuildingLocation.get()
    RoomLocation_info = RoomLocation.get()

    file = open("user.txt", "a+")
    file.write(10*"-" + "\n" + "Status: " + Status_info + "\n")
    file.write("Friendly Name: " + FriendlyName_info + "\n")
    file.write("Alt CI ID: " + AltCI_info + "\n")
    file.write("Serial Number: " + Serial_info + "\n")
    file.write("Asset Number: " + Asset_info + "\n")
    file.write("CI Type: " + CIType_info + "\n")
    file.write("Model: " + Model_info + "\n")
    file.write("Primary Contact: " + PrimaryContact_info + "\n")
    file.write("Building Location: " + BuildingLocation_info + "\n")
    file.write("Room Location: " + RoomLocation_info + "\n" + 10*"-" + "\n")
    print(" This Item ", FriendlyName_info, "was registered successfully")
    file.close

    Status_entry.delete(0, END)
    FriendlyName_entry.delete(0, END)
    AltCI_entry.delete(0, END)
    Serial_entry.delete(0, END)
    Asset_entry.delete(0, END)
    CIType_entry.delete(0, END)
    Model_entry.delete(0, END)
    PrimaryContact_entry.delete(0, END)
    BuildingLocation_entry.delete(0, END)
    RoomLocation_entry.delete(0, END)

root = Tk()
root.geometry("400x800")
root.title("Luke's CI Form")
heading = Label(root,
text = "CI Form", bg = "white", fg = "black", width = "500", height = "3")
heading.pack()
# 9 fields being status, friendly name, Alt CI ID, Serial Number, Asset, CI type, Model, Primary Contact, Location Building, Location room.

Status_text = Label(root,
text = "Status * ",)
FriendlyName_text = Label(root,
text = "Friendly Name * ",)
AltCI_text = Label(root,
text = "Alt CI ID * ",)
Serial_text = Label(root,
text = "Serial Number * ",)
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
AltCI_text.place(x = 15, y = 180)
Serial_text.place(x = 15, y = 240)
Asset_text.place(x = 15, y = 300)
CIType_text.place(x = 15, y = 360)
Model_text.place(x = 15, y = 420)
PrimaryContact_text.place(x = 15, y = 480)
BuildingLocation_text.place(x = 15, y = 540)
RoomLocation_text.place(x = 15, y = 600)

Status = StringVar()
FriendlyName = StringVar()
AltCI = StringVar()
Serial = StringVar()
Asset = StringVar()
CIType = StringVar()
Model = StringVar()
PrimaryContact = StringVar()
BuildingLocation = StringVar()
RoomLocation = StringVar()

Status_entry = Entry(textvariable = Status, width = "20")
FriendlyName_entry = Entry(textvariable = FriendlyName, width = "20")
AltCI_entry = Entry(textvariable = AltCI, width = "20")
Serial_entry = Entry(textvariable = Serial, width = "20")
Asset_entry = Entry(textvariable = Asset, width = "20")
CIType_entry = Entry(textvariable = CIType, width = "20")
Model_entry = Entry(textvariable = Model, width = "20")
PrimaryContact_entry = Entry(textvariable = PrimaryContact, width = "35")
BuildingLocation_entry = Entry(textvariable = BuildingLocation, width = "35")
RoomLocation_entry = Entry(textvariable = RoomLocation, width = "20")

Status_entry.place(x = 15, y = 80)
FriendlyName_entry.place(x = 15, y = 140)
AltCI_entry.place(x = 15, y = 200)
Serial_entry.place(x = 15, y = 260)
Asset_entry.place(x = 15, y = 320)
CIType_entry.place(x = 15, y = 380)
Model_entry.place(x = 15, y = 440)
PrimaryContact_entry.place(x = 15, y = 500)
BuildingLocation_entry.place(x = 15, y = 560)
RoomLocation_entry.place(x = 15, y = 620)

register = Button(root,text = "Register", width = "30", height = "2", command = save_info, bg = "grey")
register.place(x = 15, y = 700)

root.mainloop()