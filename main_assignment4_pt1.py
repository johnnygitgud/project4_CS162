#Line used to import class from assignment4_pt1.py
import assignment4_pt1

#Test function. Will not be seen in GUI
#Funciton will be called to test Lambda
def print_string(output_string):
    print(output_string)

#This function will be our main function to call our class defined in the other file.
def main():
    #Calls our GUI class and creates the GUI object
    gui = assignment4_pt1.TextBox_Gui()
    #Calls our GUI create label method and creates the label
    gui.create_label()
    #Calls our GUI create text box method and creates the textbox
    gui.text_box()
    
    #This function will make use of the empty button dictionary.
    # The function not only creates buttons but will make the name for the button that appears in the GUI be the key in the dictionary.
    # The value for button will its numbered order in the dictionary. The value is not important to the user as of this version
    def set_label_with_text_from_my_button_name(button_name):
        gui.label.config(text=gui.buttons[button_name].cget("text"))

    #gui.copy_text() #If this is called again, it will overide the original label text
    #Lines 26 and 27 dont have anything to do with the GUI. They are there to test lambda in the terminal. 
    lambda_print_string = lambda p1: print_string(p1) #Lambda works like a function. p1 is like a parameter. We can call the lambdaprintstring variable and pass a string using our function from line 6.
    lambda_print_string("calling the lambda function with this text as the parameter")
    
    # This creates our first button and will appear on screen as button1
    gui.create_button("button1")
    # button8 has not been created yet. The string "button8" is assigned to a variable
    button2_name = "button8"

    #The second button our screen is created. But we lambda to call our function and pass the string from line 32 to create the keys for our button dictionary
    gui.create_button(button2_name, lambda: set_label_with_text_from_my_button_name(button2_name))

    #These lines test our dictionary in the terminal. They have no effect in the GUI. These are meant to show that we have dictionary of buttons.
    print(f"gui.buttons: {gui.buttons}")
    print(f'gui.buttons["button1"]: {gui.buttons["button1"]}')
    print(f'gui.buttons["{button2_name}"]: {gui.buttons[button2_name]}')
    gui.main_loop()

if __name__ == "__main__":
    main()
