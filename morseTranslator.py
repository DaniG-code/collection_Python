from tkinter import *
from tkinter import messagebox
import winsound
import time

root = Tk()
root.title('Morse coder')

alphabet = {"A":".-", "B":"-...","C":"-.-.","D":"-..",
            "E":".","F":"..-.","G":"--.","H":"....",
            "I":"..","J":".---","K":"-.-","L":".-..",
            "M":"--","N":"-.","O":"---","P":".--.",
            "Q":"--.-","R":".-.","S":"...","T":"-",
            "U":"..-","V":"...-","W":".--","X":"-..-",
            "Y":"-.--","Z":"--.."}

# Translate to morse code window
def traTo (): 
    global bx_in
    global lbl_morse1
    
    traTo = Toplevel()
    traTo.title('Translate to Morse code')
    traTo.rowconfigure([0,1,2], minsize=30, weight=30)
    traTo.columnconfigure([0,1,2,3], minsize=60, weight=30)

    bx_in = Entry(master=traTo, width = 50 , borderwidth=2, font='arial')
    bx_in.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    lbl_morse1 = Label(master=traTo, text='In morse language', font='arial')
    lbl_morse1.grid(row=1, column=0, columnspan=3, sticky='nsew')

    btn_close = Button(master=traTo, text='Close', command=traTo.destroy, borderwidth=5, font='arial')
    btn_close.grid(row=2, column=0, sticky='nsew,')

    btn_play = Button(master=traTo, text='Play', command=lambda: play(lbl_morse1['text']), borderwidth=5, font='arial')
    btn_play.grid(row=2, column=1, sticky='nsew,')

    btn_translate = Button(master=traTo, text='Translate', command=lambda: trans(bx_in.get(), alphabet), borderwidth=5, font='arial')
    btn_translate.grid(row=2, column=2, columnspan=2, sticky='nsew,')

    root = traTo
    menubar = Menu(master=traTo, font='arial')
    menubar.add_command(label="Quit", command=quit)
    menubar.add_command(label="Morse alphabet", command=dictionary)
    root.config(menu=menubar)

#translate text to morse
def trans(phrase, alphabet):
    trad = ''
    for letter in phrase.upper():
        if '':
            trad += ' '
        if ' ':
            trad += '   '
        for x, y in alphabet.items():
            if letter == x:
                trad += y
    print(trad)
    lbl_morse1['text']=trad

#play the translated text with sound
def play(what):
    for l in str(what):
        if l == '.':
            winsound.Beep(2200, 500)
            time.sleep(0.5)
        if l == '-':
            winsound.Beep(2200, 1500)
            time.sleep(0.5)
        if l == ' ':
            time.sleep(0.5)
            
#Type in morse code window
def typeIn ():
    global lbl_morse2
    global lbl_natural

    typeIn = Toplevel()
    typeIn.title('Type in Morse code')
    typeIn.rowconfigure([0,1,2], minsize=30, weight=30)
    typeIn.columnconfigure([0,1,2,3], minsize=60, weight=30)

    lbl_natural = Label(master=typeIn, text='', font='arial')
    lbl_natural.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=5, pady=5)

    lbl_morse2 = Label(master=typeIn, text='', font='arial')
    lbl_morse2.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=5, pady=5)

    btn_close = Button(master=typeIn, text='Close', command=typeIn.destroy, borderwidth=5, font='arial')
    btn_close.grid(row=2, column=0, sticky='nsew,')

    btn_morse = Button(master=typeIn, text='Morse', borderwidth=5, font='arial')
    btn_morse.grid(row=2, column=2, columnspan=2, sticky='nsew')
    btn_morse.bind("<ButtonPress-1>", start)
    btn_morse.bind("<ButtonRelease-1>", stop)

    btn_play = Button(master=typeIn, text='Play/Translate', command=lambda: play2(lbl_morse2['text'], alphabet), borderwidth=5, font='arial')
    btn_play.grid(row=2, column=1, sticky='nsew,')

    root = typeIn
    menubar = Menu(master=typeIn)
    menubar.add_command(label="Quit", command=quit)
    menubar.add_command(label="Morse alphabet", command=dictionary)
    root.config(menu=menubar)

#type in morse
global spacestart
spacestart=0

def start(event):
    global lbl_morse2
    global start
    global spacestart
    global mo
    
    start = time.time()
    space = start-spacestart
    mo = lbl_morse2['text']
    
    if 1.2 < space and space < 3.0:
        mo += ' '
    if space >= 3.0:
        mo += '   '

    lbl_morse2['text']= mo
    
def stop(event):
    global lbl_morse2
    global start
    global stop
    global spacestart
    global mo
    
    stop = time.time()
    spacestart = time.time()
    tiLe = stop-start  #time lenght
    mo = lbl_morse2['text']

    if tiLe <= 0.5:
        mo += '.'
    if tiLe > 0.5:
        mo += '-'

    lbl_morse2['text']= mo

#play and translate
def play2(phrase, alphabet):
    global lbl_morse2
    global lbl_natural
    
    phrase = lbl_morse2['text']
    trad = ''
    temp = ''
    i = 0
    u = 0
    st = len(phrase)-1
    for s in phrase:
        if s != ' ':
            i = 0
            temp += s
        if u == st:
            for x, y in alphabet.items():
                if str(temp) == y:
                    trad += x
                    temp = '' 
        if s == ' ':
            for x, y in alphabet.items():
                if str(temp) == y:
                    trad += x
                    temp = ''
            i += 1
        if i > 1:
            trad += ' '
        u += 1
                        
                    
    lbl_natural['text']=trad

    play(lbl_morse2['text'])

#info  
def dictionary():
    messagebox.showinfo('Morse Alphabe',""" A = .- \n B = -... \n C = -.-. \n D = -.. \n E = . \n F = ..-. \n G = --. \n H = .... \n I = .. \n J = .--- \n K = -.- \n L = .-.. \n M = -- \n N = -. \n O = ---\n P = .--. \n Q = --.- \n R = .-. \n S = ... \n T = - \n U = ..- \n V = ...- \n W = .-- \n X = -..- \n Y = -.-- \n Z = --.. \n""")
#info
def info():
    messagebox.showinfo("About Morse Coder","Translate text to Morse code, type in Morse code, listen what you typed in. \n Developed by Dani Greco for a Python course project in Centria UAS.")


btn_traTo = Button(master=root, text='Translate to Morse code', command=traTo, borderwidth=10, width = 50, font='arial').pack()    
btn_typeMorse = Button(master=root, text='Type in Morse code', command=typeIn, borderwidth=10, width = 50, font='arial').pack()

menubar = Menu(master=root)
menubar.add_command(label="Quit", command=quit)
menubar.add_command(label="Info", command=info)
root.config(menu=menubar)

root.mainloop() 
