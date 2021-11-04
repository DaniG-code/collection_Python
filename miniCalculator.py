import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Mini Calculator')
window.configure(bg="lightgrey")
window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=25, weight=25)
window.columnconfigure([0, 1, 2, 3], minsize=50, weight=25)

op = 0
num1 = 0
num3 = 0

def addition():
    global op
    calculate()
    op = 1

def subtraction():
    global op
    calculate()
    op = 2
    
def multiplication():
    global op
    calculate()
    op = 3
    
def division():
    global op
    calculate()
    op = 4
    
def button_clk(number):
    num = display.get()
    display.delete(0, 1000)
    display.insert(0, num+number)

def calculate():
    global op
    global num1
    global num3
    res = 0
    if display.get() == "":
        error()
        delete()
    else:
        if op != 0 or num3 != 0:
            num2 = display.get()
            if num3 != 0:
                num1 = num3
            if op == 1:
                res = float(num1) + float(num2)
            if op == 2:
                res = float(num1) - float(num2)
            if op == 3:
                res = float(num1) * float(num2)
            if op == 4:
                res = float(num1) / float(num2)
            num1 = res
        else:
            num1 = display.get()
        display.delete(0, 1000)
    
def result ():
    global num1
    global num3
    global op
    calculate ()
    display.delete(0, 1000)
    display.insert(0, num1 )
    num3 = float(num1)
    op = 0

def delete():
    global num1
    global num2
    global num3
    global op
    display.delete(0, 1000)
    num1 = 0
    num2 = 0
    num3 = 0
    op = 0

def timesminus():
    global num1
    global num2
    global num3
    global op
    if display.get() == "":
        error()
        delete()
    else:
        if op != 0 or num3 != 0:
            if num3 != 0:
                num3 = num3 * (-1)
        else:
            num = float(display.get())
            num = num * (-1)
            display.delete(0, 1000)
            display.insert(0, num )

def info():
    messagebox.showinfo("About Mini Calculator","Just a normal mini calculator. \n Developed by Dani Greco for a Python course project in Centria UAS.")

def error():
    messagebox.showinfo("ERROR","ERROR! Type number before operator!\n If number is negative type number and then (-)")

display = tk.Entry(master=window,width=40,  bg="lightblue")
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

btn_1 = tk.Button(master=window, text='1', command=lambda: button_clk('1'), borderwidth=5)
btn_1.grid(row=4, column=0, sticky='nsew')

btn_2 = tk.Button(master=window, text='2', command=lambda: button_clk('2'), borderwidth=5)
btn_2.grid(row=4, column=1, sticky='nsew')

btn_3 = tk.Button(master=window, text='3', command=lambda: button_clk('3'), borderwidth=5)
btn_3.grid(row=4, column=2, sticky='nsew')

btn_4 = tk.Button(master=window, text='4', command=lambda: button_clk('4'), borderwidth=5)
btn_4.grid(row=3, column=0, sticky='nsew')

btn_5 = tk.Button(master=window, text='5', command=lambda: button_clk('5'), borderwidth=5)
btn_5.grid(row=3, column=1, sticky='nsew')

btn_6 = tk.Button(master=window, text='6', command=lambda: button_clk('6'), borderwidth=5)
btn_6.grid(row=3, column=2, sticky='nsew')

btn_7 = tk.Button(master=window, text='7', command=lambda: button_clk('7'), borderwidth=5)
btn_7.grid(row=2, column=0, sticky='nsew')

btn_8 = tk.Button(master=window, text='8', command=lambda: button_clk('8'), borderwidth=5)
btn_8.grid(row=2, column=1, sticky='nsew')

btn_9 = tk.Button(master=window, text='9', command=lambda: button_clk('9'), borderwidth=5)
btn_9.grid(row=2, column=2, sticky='nsew')

btn_0 = tk.Button(master=window, text='0', command=lambda: button_clk('0'), borderwidth=5)
btn_0.grid(row=5, column=0, columnspan=2, sticky='nsew')

btn_div = tk.Button(master=window, text='/', command=division, borderwidth=5)
btn_div.grid(row=1, column=2, sticky='nsew')

btn_mul = tk.Button(master=window, text='*', command=multiplication, borderwidth=5)
btn_mul.grid(row=1, column=3, sticky='nsew')

btn_min = tk.Button(master=window, text='-', command=subtraction, borderwidth=5)
btn_min.grid(row=2, column=3, sticky='nsew')

btn_add = tk.Button(master=window, text='+', command=addition, borderwidth=5)
btn_add.grid(row=3, column=3, sticky='nsew')

btn_enter = tk.Button(master=window, text='=', command=result, borderwidth=5)
btn_enter.grid(row=4,rowspan=2, column=3, sticky='nsew')

btn_c = tk.Button(master=window, text='C', command=delete, borderwidth=5)
btn_c.grid(row=1, column=0, sticky='nsew')

btn_dot = tk.Button(master=window, text=',', command=lambda: button_clk('.'), borderwidth=5)
btn_dot.grid(row=5, column=2, sticky='nsew')

btn_timesminus = tk.Button(master=window, text='(-)', command=timesminus , borderwidth=5)
btn_timesminus.grid(row=1, column=1, sticky='nsew')

root = window
menubar = tk.Menu(master=root)
menubar.add_command(label="Quit", command=quit)
menubar.add_command(label="Info", command=info)
root.config(menu=menubar)
window.mainloop()
