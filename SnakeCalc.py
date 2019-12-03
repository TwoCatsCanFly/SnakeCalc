from tkinter import *
root = Tk()

root.title("Snake Calc")
inp_show = Entry(root, width=35, borderwidth=5)
inp_show.grid(row=0,column=0, columnspan=3, padx=10, pady=10)
display = []
number = []
calculation = []

def calc():
    f = len(calculation)
    g = calculation[f-1]
    if g in ["+","-","*","/"]:
        calculation.pop()
    try:
        r = eval("".join(calculation))
    except:
        r = "Error"
    return r
def disp(a):
    c = len(display)+1
    if a == "clr":
        inp_show.delete(0,END)
        display.clear()
    elif a == "res":
        r = str(calc())
        inp_show.delete(0, END)
        inp_show.insert(0, r)
        calculation.clear()
        if r != "Error":
            calculation.append(r)
    else :
        display.append(a)
        inp_show.insert(c,a)
def btn_click(sym):
    if sym == "clr":
        disp(sym)
        number.clear()
        calculation.clear()
    elif sym in ["+","-","*","/","res"]:
        j = ("".join(number))
        number.clear()
        if j != '':
            calculation.append(j)
        if sym != "res":
            calculation.append(sym)
        if sym == "res":
            calc()
        disp(sym)
    else:
        if sym != "0":
            number.append(sym)
        elif sym == "0" and number:
            number.append(sym)
        elif sym == "0" and not number:
            return
        disp(sym)

button_0 = Button(root,text="0",padx=40, pady=20,command=lambda: btn_click("0"))
button_1 = Button(root,text="1",padx=40, pady=20,command=lambda: btn_click("1"))
button_2 = Button(root,text="2",padx=40, pady=20,command=lambda: btn_click("2"))
button_3 = Button(root,text="3",padx=40, pady=20,command=lambda: btn_click("3"))
button_4 = Button(root,text="4",padx=40, pady=20,command=lambda: btn_click("4"))
button_5 = Button(root,text="5",padx=40, pady=20,command=lambda: btn_click("5"))
button_6 = Button(root,text="6",padx=40, pady=20,command=lambda: btn_click("6"))
button_7 = Button(root,text="7",padx=40, pady=20,command=lambda: btn_click("7"))
button_8 = Button(root,text="8",padx=40, pady=20,command=lambda: btn_click("8"))
button_9 = Button(root,text="9",padx=40, pady=20,command=lambda: btn_click("9"))
button_add = Button(root,text="+",padx=39, pady=20,command=lambda: btn_click("+"))
button_dot = Button(root,text=".",padx=41, pady=20,command=lambda: btn_click("."))
button_sub = Button(root,text="-",padx=40, pady=20,command=lambda: btn_click("-"))
button_mil = Button(root,text="*",padx=41, pady=20,command=lambda: btn_click("*"))
button_diy = Button(root,text="/",padx=41, pady=20,command=lambda: btn_click("/"))
button_equal = Button(root,text="=",padx=135, pady=20,command=lambda: btn_click("res"))
button_clear = Button(root,text="Clear",padx=125, pady=20,command=lambda: btn_click("clr"))
#displaying buttons
button_0.grid(row=4,column=0)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_add.grid(row=4,column=2)
button_dot.grid(row=4,column=1)
button_sub.grid(row=5,column=0)
button_mil.grid(row=5,column=1)
button_diy.grid(row=5,column=2)
button_equal.grid(row=6,column=0,columnspan=3)
button_clear.grid(row=7,column=0,columnspan=3)
root.mainloop()

