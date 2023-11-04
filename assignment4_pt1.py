
import tkinter as tk

# Create a function to copy text from the text box to the label

class TextBox_Gui:
    """Create the main window"""
    def __init__(self):
        # root creates the window
        self.root = tk.Tk()
        # sets the size of the window itself
        self.root.minsize(800, 600)
        #gives our window a title
        self.root.title("Text Copy App")
        # creates a dictionary of buttons
        self.buttons = {}

    """Create a label"""
    def create_label(self):
        #a sets the lable with its name
        self.label = tk.Label(self.root, text="This is label")
        #Using pack as supposed to grind to set size of widget
        self.label.pack(pady =50)

    """Create a text box"""
    def text_box(self):
        self.textbox = tk.Entry(self.root)
        self.textbox.pack()
    
    """Take text from text box"""
    def copy_text(self):
        #.config is used to create a setting that can be called to.
        #The text entered will added to our label using textbox.get()
        self.label.config(text=self.textbox.get())

    """Method for creating buttons"""
    def create_button(self, name, action="no action selected"):
        if action == "no action selected":
            button = tk.Button(self.root, text=name, command=self.copy_text)
        else:
            button = tk.Button(self.root, text=name, command=action)
        self.buttons[name] = button
        button.pack()
    
# Start the main event loop
    
    def main_loop(self):
        self.root.mainloop()


"""Below is the original code from chatGPT that i manually created a class and a main file for.
        It has been commented out"""
#
#import tkinter as tk

# # Create a function to copy text from the text box to the label
# def copy_text():
#     label.config(text=textbox.get())

# # Create the main window
# root = tk.Tk()
# root.title("Text Copy App")

# # Create a label
# label = tk.Label(root, text="Label")
# label.pack(pady=10)

# # Create a text box
# textbox = tk.Entry(root)
# textbox.pack()

# # Create a button
# button = tk.Button(root, text="Copy Text", command=copy_text)
# button.pack()

# # Start the main event loop
# root.mainloop()
