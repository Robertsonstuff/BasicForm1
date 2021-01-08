
try:
    from Tkinter import Label
    from ttk import Style
    from tkFont import Font, nametofont
except ImportError:
    from tkinter import Label
    from tkinter.ttk import Style
    from tkinter.font import Font, nametofont

def get_background_of_widget(widget):
    try:
        # We assume first tk widget
        background = widget.cget("background")
    except:
        # Otherwise this is a ttk widget
        style = widget.cget("style")

        if style == "":
            # if there is not style configuration option, default style is the same than widget class
            style = widget.winfo_class()

        background = Style().lookup(style, 'background')
    
    return background

class Link_Button(Label, object):
    def __init__(self, master, text, background=None, font=None, familiy=None, size=None, underline=True, visited_fg = "#551A8B", normal_fg = "#0000EE", visited=False, action=None):
        self._visited_fg = visited_fg
        self._normal_fg = normal_fg
        
        if visited:
            fg = self._visited_fg
        else:
            fg = self._normal_fg

        if font is None:
            default_font = nametofont("TkDefaultFont")
            family = default_font.cget("family")

            if size is None:
                size = default_font.cget("size")

            font = Font(family=family, size=size, underline=underline)

        Label.__init__(self, master, text=text, fg=fg, cursor="hand2", font=font)

        if background is None:
            background = get_background_of_widget(master)

        self.configure(background=background)

        self._visited = visited
        self._action = action

        self.bind("<Button-1>", self._on_click)

    @property
    def visited(self):
        return self._visited
        
    @visited.setter
    def visited(self, is_visited):
        if is_visited:
            self.configure(fg=self._visited_fg)
            self._visited = True
        else:
            self.configure(fg=self._normal_fg)
            self._visited = False

    def _on_click(self, event):
        if not self._visited:
            self.configure(fg=self._visited_fg)

        self._visited = True

        if self._action:
            self._action()

if __name__ == "__main__":
    import webbrowser

    try:
        from Tkinter import *
    except ImportError:
        from tkinter import *    

    def save_info():
        #print("hello Luke")
        firstname_info = firstname.get()
        lastname_info = lastname.get()
        age_info = age.get()
        print(firstname_info, lastname_info, age_info)
    
        file = open("user.txt", "a+")
        file.write(firstname_info + " ")
        file.write(lastname_info + " ")
        file.write(age_info + "\n")
        print(" User ", firstname_info, "registered successfully")
        file.close

    def callback():
        webbrowser.open_new(r"mailto:lukerobertsonblogger@gmail.com")
        
        


        firstname_entry.delete(0, END)
        lastname_entry.delete(0, END)
        age_entry.delete(0, END)



    root = Tk()
    root.geometry("500x500")
    root.title("Luke's Basic Form")
    heading = Label(root,
    text = "*", bg = "white", fg = "black", width = "500", height = "3")
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
    age = StringVar()

    firstname_entry = Entry(textvariable = firstname, width = "30")
    lastname_entry = Entry(textvariable = lastname, width = "30")
    age_entry = Entry(textvariable = age, width = "15")

    firstname_entry.place(x = 15, y = 100)
    lastname_entry.place(x = 15, y = 170)
    age_entry.place(x = 15, y = 240)

    register = Button(root,text = "Register", width = "30", height = "2", command = save_info, bg = "grey")
    register.place(x = 15, y = 290)

    link = Link_Button(heading, text="My Email", action=callback)
    link.pack(padx=10, pady=10)
    root.mainloop()
 
