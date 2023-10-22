import tkinter as tk


# Create the main window
root = tk.Tk()
root.title("Text Copy App")

# Create a label
label = tk.Label(root, text="Enter some numbers")
label.pack(pady=10)

# Create a text box
textbox = tk.Entry(root)
textbox.pack()

# This for loop creates more textboxes instead of writing them manually.
for textbox in range(0,9):
    textbox = tk.Entry(root)
    textbox.pack(pady=10)

# Create a function to copy text from the text box to the label

# min_value = int(textbox)
# max_value = int(textbox)

def copy_text():
    # for num in range(1, int(textbox)):
    #     if num < min_value:
    #         min_value = num
    #     if num > max_value:
    #         max_value = num
        label.config(text=int(textbox.get()))


# Create a button
button = tk.Button(root, text="Find Lowest Number", command=copy_text)
button.pack()

# Start the main event loop
root.mainloop()
