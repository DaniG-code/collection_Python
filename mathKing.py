import tkinter as tk
from tkinter import messagebox
import random
import winsound

window = tk.Tk()
window.title('Math King')



def operation ():
    op = ['+','-']
    i = random.randint(0,1)
    return op[i]

def newGame():
    num1 = random.randint(0,10)
    lbl_num1['text']= num1
    
    num2 = random.randint(0,10)
    lbl_num2['text']= num2
    
    op = ['+','-']
    i = random.randint(0,1)
    lbl_operation['text']= op[i]

    btn_submit['state']='normal'
    btn_new['state']='disabled'
    txtbx_user_solution.delete(0, 14) #clean txtbx_user_solution


def submit():
    positive = ['Correct!','Fantastic!','Nice job!','Well done!']
    negative = ['Ups!','Not exactly','Take your time', 'Wrong']
    
    if lbl_operation['text'] == '+':
        res = int(lbl_num1['text']+ lbl_num2['text'])
    else:
        res = int(lbl_num1['text']- lbl_num2['text'])

    user_res = txtbx_user_solution.get() ## .get info

    if str(res) == user_res:
        lbl_solution['bg'] = 'green'
        lbl_solution['fg'] = 'white'
        txtbx_user_solution['bg'] = 'green'
        lbl_solution['text']=res
        i = random.randint(0, (len(positive)-1))
        lbl_message['text']= positive[i]
        lbl_message['bg'] = 'green'
        lbl_num1['text']= ''
        lbl_num2['text']= ''
        score = int(lbl_score['text'])+1
        lbl_score['text']=score
        winsound.Beep(2200, 200)
        winsound.Beep(2400, 300)
    else:
        lbl_solution['bg'] = 'yellow'
        lbl_solution['fg'] = 'red'
        txtbx_user_solution['bg'] = 'red'
        lbl_solution['text']=res
        i = random.randint(0, (len(negative)-1))
        lbl_message['text']= negative[i]
        lbl_message['bg'] = 'yellow'

        max_score = int(lbl_max_score['text'])
        now_score = int(lbl_score['text'])
        winsound.Beep(2200, 200)
        winsound.Beep(2000, 400)
        if now_score > max_score:
            lbl_max_score['text']=now_score

        lbl_score['text']='0'

    btn_submit['state']='disabled'
    btn_new['state']='normal'

def handle_keypress(event):
    if btn_submit['state']=='normal':
        submit()
    elif btn_new['state']=='normal':
        newGame()
    
    

def info():
    messagebox.showinfo('How do I play?!?!','Click on "New"(Or press Enter); type your solution;\n click on "Submit"(Or press Enter) and check your answer, then click on "New"(Or press Enter).\n Your score is updated and the best score is saved.\n \n Developed by Dani Greco for a Python course project in Centria UAS.\n \n Enjoy!')
    
    


window.configure(bg="lightblue")
window.rowconfigure(6, minsize=100, weight=1)
window.columnconfigure([0, 1, 2, 3, 4], minsize=80, weight=1)
window.bind("<Return>", handle_keypress)


lbl_num1 = tk.Label(master=window, text="", bg="lightblue")
lbl_num1.grid(row=1, column=1)

lbl_operation = tk.Label(master=window, text="", bg="lightblue")
lbl_operation.grid(row=1, column=2)

lbl_num2 = tk.Label(master=window, text="", bg="lightblue")
lbl_num2.grid(row=1, column=3)

lbl_message = tk.Label(master=window, text="" , width=10, bg="lightblue")
lbl_message.grid(row=3, column=2)


lbl_solution = tk.Label(master=window, width=10, text="", bg="lightblue")
lbl_solution.grid(row=3, column=1)

lbl_score_message = tk.Label(master=window, text="Your score", bg="lightblue")
lbl_score_message.grid(row=5, column=1)

lbl_score = tk.Label(master=window, text="0", bg="lightblue")
lbl_score.grid(row=5, column=2)

lbl_max_score_message = tk.Label(master=window, text="Best score", bg="lightblue")
lbl_max_score_message.grid(row=6, column=1)

lbl_max_score = tk.Label(master=window, text="0", bg="lightblue")
lbl_max_score.grid(row=6, column=2)

lbl_info_message = tk.Label(master=window, text="", bg="lightblue")
lbl_info_message.grid(row=7, column=1)

txtbx_user_solution = tk.Entry(master = window, fg="white", bg="grey", width=10, borderwidth=2)
txtbx_user_solution.grid(row=3, column=3, sticky="nsew")
txtbx_user_solution.insert(0, 'Type solution')

btn_new = tk.Button(master=window, text='New',state=tk.NORMAL, command=newGame, padx=25, pady=25, borderwidth=5) 
btn_new.grid(row=4, column=1, sticky='nsew')

btn_submit = tk.Button(master=window, text='Submit', state=tk.DISABLED, command=submit, padx=25, pady=25, borderwidth=5)
btn_submit.grid(row=4, column=3, sticky='nsew')

root = window
menubar = tk.Menu(master=root)
menubar.add_command(label="Quit", command=quit)
menubar.add_command(label="Info", command=info)
root.config(menu=menubar)
window.mainloop()
