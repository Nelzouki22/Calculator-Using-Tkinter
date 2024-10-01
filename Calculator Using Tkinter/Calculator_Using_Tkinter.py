import tkinter as tk
from tkinter import *

# Function to update the expression in the text entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the contents of the text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Driver code
if __name__ == "__main__":
    # Create a GUI window
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("400x500")

    expression = ""

    # StringVar() is used to get the instance of input field
    equation = StringVar()

    # Create an entry field
    entry_field = Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
    entry_field.grid(row=0, column=0, columnspan=4)

    # Creating buttons for the calculator
    button1 = Button(root, text=' 1 ', fg='black', bg='white', height=3, width=7, command=lambda: press(1))
    button1.grid(row=1, column=0)

    button2 = Button(root, text=' 2 ', fg='black', bg='white', height=3, width=7, command=lambda: press(2))
    button2.grid(row=1, column=1)

    button3 = Button(root, text=' 3 ', fg='black', bg='white', height=3, width=7, command=lambda: press(3))
    button3.grid(row=1, column=2)

    button4 = Button(root, text=' 4 ', fg='black', bg='white', height=3, width=7, command=lambda: press(4))
    button4.grid(row=2, column=0)

    button5 = Button(root, text=' 5 ', fg='black', bg='white', height=3, width=7, command=lambda: press(5))
    button5.grid(row=2, column=1)

    button6 = Button(root, text=' 6 ', fg='black', bg='white', height=3, width=7, command=lambda: press(6))
    button6.grid(row=2, column=2)

    button7 = Button(root, text=' 7 ', fg='black', bg='white', height=3, width=7, command=lambda: press(7))
    button7.grid(row=3, column=0)

    button8 = Button(root, text=' 8 ', fg='black', bg='white', height=3, width=7, command=lambda: press(8))
    button8.grid(row=3, column=1)

    button9 = Button(root, text=' 9 ', fg='black', bg='white', height=3, width=7, command=lambda: press(9))
    button9.grid(row=3, column=2)

    button0 = Button(root, text=' 0 ', fg='black', bg='white', height=3, width=7, command=lambda: press(0))
    button0.grid(row=4, column=1)

    plus = Button(root, text=' + ', fg='black', bg='light gray', height=3, width=7, command=lambda: press('+'))
    plus.grid(row=1, column=3)

    minus = Button(root, text=' - ', fg='black', bg='light gray', height=3, width=7, command=lambda: press('-'))
    minus.grid(row=2, column=3)

    multiply = Button(root, text=' * ', fg='black', bg='light gray', height=3, width=7, command=lambda: press('*'))
    multiply.grid(row=3, column=3)

    divide = Button(root, text=' / ', fg='black', bg='light gray', height=3, width=7, command=lambda: press('/'))
    divide.grid(row=4, column=3)

    equal = Button(root, text=' = ', fg='black', bg='light green', height=3, width=7, command=equalpress)
    equal.grid(row=4, column=2)

    clear = Button(root, text='Clear', fg='black', bg='red', height=3, width=7, command=clear)
    clear.grid(row=4, column=0)

    # Run the GUI
    root.mainloop()

