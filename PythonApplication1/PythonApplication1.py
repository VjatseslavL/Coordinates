import matplotlib.pyplot as plt
import numpy as np
import tkinter
import math

colors1 = "white"
colors2 = "white"
colors3 = "white"
d = -1
def coordinates():
          if d == 0:
                    plt.style.use("seaborn-whitegrid")
                    x = np.linspace(-x3, x3)
                    y =  x ** 2
                    plt.plot(x, y)
                    plt.show()
          
          elif d  >  0:
                    if vr11 < 0:
                              plt.style.use("seaborn-whitegrid")
                              x = np.linspace(-x1, x1)
                              y =  -x ** 2
                              plt.plot(x, y)
                              plt.show()
                    else:
                              plt.style.use("seaborn-whitegrid")
                              x = np.linspace(-x1, x1)
                              y =  x ** 2
                              plt.plot(x, y)
                              plt.show()    

def result():
    global x1, x2, x3, d
    global label6
    global vr11, vr22, vr33

    try:
        vr11 = vr1.get()
    except:
        colors1 = "red"
        text1.config(bg=colors1)
        text2.config(bg="white")
        text3.config(bg="white")
        return colors1
    text1.config(bg="white")


    try:
        vr22 = vr2.get()
    except:
        colors2 = "red"
        text1.config(bg="white")
        text2.config(bg="red")
        text3.config(bg="white")
        return colors2
    text2.config(bg="white")

    try:
        vr33 = vr3.get()
    except:
        colors3 = "red"
        text1.config(bg="white")
        text2.config(bg="white")
        text3.config(bg="red")
        return colors3

    text3.config(bg="white")
    d = (vr22 ** 2) - (4 * vr11 * vr33)

    if d > 0:

        x1 = (-vr22 + math.sqrt(d)) / (2 * vr11)
        x2 = (-vr22 - math.sqrt(d)) / (2 * vr11)

        label6.config(text=f"x1 = {x1}\nx2 = {x2}")

    elif d == 0:
        x3 = -vr22 / (2 * vr11)
        label6.config(text=f"x = {x3}")

    elif d < 0:
        label6.config(text=f" d < 0 ")


n = 0
tk = tkinter.Tk()


tk.title("Решение квадратного уравнения")

tk.geometry("900x200")
vr1 = tkinter.IntVar(tk, 1)
vr2 = tkinter.IntVar(tk, 6)
vr3 = tkinter.IntVar(tk, 8)

nupp = tkinter.Button(tk, text="Vajuta \nsiia", height=2, width=5, bg="#FFFFF0", fg="green",
                      font="Arial 14", command=result)  # .pack(side=TOP) command=vajutamine()
nupp1 =  tkinter.Button(tk, text="Граф", height=2, width=5, bg="#FFFFF0", fg="green",
                      font="Arial 14", command=coordinates)  # .pack(side=TOP) command=vajutamine()

label1 = tkinter.Label(text="Решение квадратного уравнения", height=2, width=30, bg="white", font="Arial 22")
label2 = tkinter.Label(text=" x**2 + ", font="Arial 15")
label3 = tkinter.Label(text=" x + ", font="Arial 15")
label4 = tkinter.Label(text=" = 0 ", font="Arial 15")
label5 = tkinter.Label(width=41)
label6 = tkinter.Label(text="Result", font="Arial 15", height=2, width=84, bg="#F0FFFF")

text1 = tkinter.Entry(width=2, font="Arial 30", textvariable=vr1, bg=colors1)
text2 = tkinter.Entry(width=2, font="Arial 30", textvariable=vr2, bg=colors2)
text3 = tkinter.Entry(width=2, font="Arial 30", textvariable=vr3, bg=colors3)

label1.pack()
label6.pack(side="bottom")
label5.pack(side="left")
text1.pack(side="left")
label2.pack(side="left")
text2.pack(side="left")
label3.pack(side="left")
label2.pack(side="left")
text3.pack(side="left")
label4.pack(side="left")
nupp.pack(side="left")
nupp1.pack(side="left")
tk.mainloop()






