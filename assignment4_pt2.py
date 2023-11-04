import tkinter as tk


# Create the main window
root = tk.Tk()
root.title("Text Copy App")

# Create a label
label = tk.Label(root, text="Enter some numbers")
label.pack(pady=10)

# Type hinting is used to create an empty list for the variable textboxes. Note. Check ChatGPT conversation for a more in depth explanation
# Annotations are used in type hints. The original code I sent you was a type hint. 
# The variable is my code was textboxes. The type hint annotation was list[tk.Entry].  
# The value is an empty list. However, list in list[tk.Entry] is class that is part of pythons type hinting system. It is not a special keyword
textboxes: list[tk.Entry] = []


# Create a text box and append it to the empty list called textboxes
textbox = tk.Entry(root)
textbox.insert(0, "0")
textbox.pack()
textboxes.append(textbox)

# This for loop creates more textboxes instead of writing them manually.
# It will also include values to each textbox.
#There will be 10 textboxes total and the first box will have the default value 0 and each textbox will go up to 9
for i in range(0,9):
    textbox = tk.Entry(root)
    textbox.insert(0, str(i + 1))
    textbox.pack(pady=10)
    textboxes.append(textbox)

# Create a function to copy text from the text box to the label
# The function will look for the next smallest value and print it to the lablel
# The first value printed to the screen will be 0 and the last one will be 9
def copy_text():
    min_value = None
    max_value = None
    min_index = 0 # Maybe we should follow our None default value and do a None type check when needed...
    for current_index,current_textbox in enumerate(textboxes):
        current_text = current_textbox.get()
        if current_text.lstrip('-').isnumeric():
            num = int(current_text)
        else:
            # print(f"current_text: {current_text}, current_text.isnumeric(): {current_text.isnumeric()}")
            continue
       
        # try:
        #     num = int(current_textbox.get())
        # except ValueError:
        #     continue
        if min_value is None or num < min_value:
            min_value = num
            min_index = current_index
        if max_value is None or num > max_value:
            max_value = num
    label.config(text=min_value)
    textboxes[min_index].delete(0, tk.END)


# Create a button
button = tk.Button(root, text="Find Lowest Number", command=copy_text)
button.pack()

# Start the main event loop
root.mainloop()
