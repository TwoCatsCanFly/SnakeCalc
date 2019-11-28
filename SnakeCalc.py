from tkinter import *

root = Tk()
root.title("Snake Calc")

inp_show = Entry(root, width=35, borderwidth=5)
inp_show.grid(row=0,column=0, columnspan=3, padx=10, pady=10)
line_show = [] #for display
number_show = [] #for calculation
wtf_line = [] #for wtf


def button_click(symbol):
    symbol = str(symbol)
    if symbol == "clr": #screen clear+mem clear
        inp_show.delete(0,END)
        line_show.clear()
    elif symbol == "res": #result
        inp_show.delete(0, END)
        le = line_show[len(line_show)-1]
        if le in ["1","2","3","4","5","6","7","8","9","0"]:
            print(True)

        else:
            print(False)
            line_show.pop()
        res = int(eval("".join(line_show)))
        print(res)
        inp_show.insert(-0, res)
        line_show.clear()
        line_show.append(str(res))
    elif symbol in ["+","-","*","/"]:
        return

    else:
        line_show.append(symbol)
        wtf_line.append(symbol)
        print(line_show)
        inp_show.delete(0, END)
        inp_show.insert(-0, ("".join(line_show)))



#Buttons
button_0 = Button(root,text="0",padx=40, pady=20,command=lambda: button_click(0))
button_1 = Button(root,text="1",padx=40, pady=20,command=lambda: button_click(1))
button_2 = Button(root,text="2",padx=40, pady=20,command=lambda: button_click(2))
button_3 = Button(root,text="3",padx=40, pady=20,command=lambda: button_click(3))
button_4 = Button(root,text="4",padx=40, pady=20,command=lambda: button_click(4))
button_5 = Button(root,text="5",padx=40, pady=20,command=lambda: button_click(5))
button_6 = Button(root,text="6",padx=40, pady=20,command=lambda: button_click(6))
button_7 = Button(root,text="7",padx=40, pady=20,command=lambda: button_click(7))
button_8 = Button(root,text="8",padx=40, pady=20,command=lambda: button_click(8))
button_9 = Button(root,text="9",padx=40, pady=20,command=lambda: button_click(9))

button_add = Button(root,text="+",padx=39, pady=20,command=lambda: button_click("+"))
button_equal = Button(root,text="=",padx=91, pady=20,command=lambda: button_click("res"))
button_clear = Button(root,text="Clear",padx=79, pady=20,command=lambda: button_click("clr"))

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

