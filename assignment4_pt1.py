
import tkinter as tk

# Create a function to copy text from the text box to the label

class TextBox_Gui:
# Create the main window
    def __init__(self):
        self.root = tk.Tk()
        self.root.minsize(800, 600)
        self.root.title("Text Copy App")

# Create a label
    def label(self):
        self.label = tk.Label(self.root, text = "This is label")
        self.label.pack(pady =10)

# Create a text box
    def text_box(self):
        self.textbox = tk.Entry(self.root)
        self.textbox.pack()
    def copy_text(self):
        self.label(text=self.textbox.get())

# Create a button
    def button(self):
        self.button = tk.Button(self.root, text="Copy Text", command= self.copy_text)
        self.button.pack()
    
# Start the main event loop
    
    def main_loop(self):
        self.root.mainloop()


"""Below is the original code from chatGPT that i manually created a class and a main file for.
        It has been commented out"""

# import tkinter as tk

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
