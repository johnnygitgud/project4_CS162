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
    textbox.insert(0, str(i + 1))#This line will insert the values for each text up counting up.
    textbox.pack(pady=10)
    textboxes.append(textbox)#This line will append each textbox to the list of textboxes.

# Create a function to copy text from the text box to the label
# The function will look for the next smallest value and print it to the lablel
# The first value printed to the screen will be 0 and the last one will be 9
def copy_text():
    # These variablese will help us keep track of of the min and max value as well as the index.
    min_value = None
    max_value = None
    min_index = 0
    #Line 43 is a method called tuple unpacking. The variable current_index will hold the index in the list of textboxes and current textbox will hold the each element in the list of textboxes
    for current_index,current_textbox in enumerate(textboxes):
        current_text = current_textbox.get() # Get the values from each textbox and assign them to current_text
        if current_text.lstrip('-').isnumeric():# lstrip will prevent negative numers and isnumeric will for numbers
            num = int(current_text)# convers all values in each textbox to integer data type
        else:
            # print(f"current_text: {current_text}, current_text.isnumeric(): {current_text.isnumeric()}")
            continue
       
        # try:
        #     num = int(current_textbox.get())
        # except ValueError:
        #     continue
        if min_value is None or num < min_value:#condition will always return True because min_value was initially given the value none.
            min_value = num # Since the above condition will always be met min_value is reasssigned the value of num which is the numbers inside the textboxes
            min_index = current_index # This will also execute and be given each index from the list of texboxes
        #Similarly to the previous if statement. 
        # We are using max value and since it was originally assigned the value None that condition will return True. 
        # The or statement will return true even though num > max_value is not a true statement.  
        # Since the condition checks out we can assign the value of num to  max value
        if max_value is None or num > max_value:
            max_value = num
    label.config(text=min_value)# The label whill change to the current min value when the button is clicked.
    #We take current index which is min_index and delete the value inside. We start at 0 because that is the first index and tk.END is used to reference the last value in the textbox
    #Each time button is clicked the function executes and it will delete each value in every textbox starting from top to bottom
    textboxes[min_index].delete(0, tk.END)


# Create a button and the commmand will call the copy_text function
button = tk.Button(root, text="Find Lowest Number", command=copy_text)
button.pack()

# Start the main event loop
root.mainloop()


##Test code sample for tuple unpacking
# list = ['A', 'B', 'C']
# for current_index, current_element in enumerate(list):
#     print(f"Index: {current_index}, Value: {current_element}")