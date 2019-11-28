from tkinter import *

root = Tk()
root.title("Snake Calc")

inp_show = Entry(root, width=35, borderwidth=5)
inp_show.grid(row=0,column=0, columnspan=3, padx=10, pady=10)
# line_show = [] #for display
# number_show = [] #for calculation
# wtf_line = [] #for wtf

# def button_click(symbol):
#     symbol = str(symbol)
#     if symbol == "clr": #screen clear+mem clear
#         inp_show.delete(0,END)
#         line_show.clear()
#         number_show.clear()
#         wtf_line.clear()
#     elif symbol == "res": #result
#         inp_show.delete(0, END)
#         le = number_show[len(number_show)-1]
#         wtf_1 = "".join(wtf_line)
#         number_show.append(wtf_1)
#         print(wtf_1,"wtf_1")
#         wtf_line.clear()
#         print(number_show)
#         print(le,"last in number_show")
#         if le not in ["+","-","*","/"]:
#             print(True, "line is fine")
#         else:
#             print(False,"EOF cached!")
#             number_show.pop()
#         res = int(eval("".join(number_show)))
#         print(res)
#         inp_show.insert(-0, res)
#         line_show.clear()
#         line_show.append(str(res))
#         number_show.append(str(res))
#     elif symbol in ["+","-","*","/"]:
#         wtf = "".join(wtf_line)
#         print(wtf,"wtf")
#         number_show.append(wtf)
#         number_show.append(symbol)
#         line_show.append(symbol)
#         inp_show.delete(0, END)
#         inp_show.insert(-0, ("".join(line_show)))
#         wtf_line.clear()
#         print(line_show," = line_show")
#         print(number_show," = number_show")
#     else:
#         line_show.append(symbol)
#         wtf_line.append(symbol)
#         print(line_show)
#         inp_show.delete(0, END)
#         inp_show.insert(-0, ("".join(line_show)))



#Buttons

display = []
number = []
calculation = []

def calc():
    r = eval("".join(calculation))
    print(r)

def disp(a):
    c = len(display)+1
    if a == "clr":
        inp_show.delete(0,END)
        display.clear()
    elif a == "res":
        return
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
        calculation.append(j)
        if sym != "res":
            calculation.append(sym)
        if sym == "res":
            calc()
        disp(sym)
    else:
        number.append(sym)
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
button_equal = Button(root,text="=",padx=91, pady=20,command=lambda: btn_click("res"))
button_clear = Button(root,text="Clear",padx=79, pady=20,command=lambda: btn_click("clr"))

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

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)


root.mainloop()

