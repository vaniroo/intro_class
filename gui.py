from Tkinter import*
root_widget = Tk()
var_label_text = StringVar()    #            # Special Tkinter Variable for label text
   

def main():
                            # creates a widget window which will hold all other widgets.
    root_widget.geometry("300x100")             # sets the size of the window
    root_widget.title("Simple GUI Demo")        # set the title of the window


    var_label_text.set("Display your name here")
  
    Label(root_widget,textvariable= var_label_text ).grid(row=0, sticky=W)#terxtvariable allows updates of this label
    Label(root_widget, text="First").grid(row=1, sticky=W)
    Label(root_widget, text="Last").grid(row=2, sticky=W)

    e1 = Entry(root_widget)
    e2 = Entry(root_widget)

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)                          # show the label

    
    button1 = Button(text='Ok', command=lambda: var_label_text.set(e1.get() + e2.get()))
    #btn_ok = Button(text='Ok', command=set_text)
    button1.grid(row=3, column=1)

    # runs the window in a loop so it continuously detects the button click event
    root_widget.mainloop()

if __name__ == '__main__':
    main()