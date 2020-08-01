"""
Programme principale du projet RandomAirport
"""
from tkinter import *
import random
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# TODO (30/07/2020): 
#   show in a world map

# =========================BACKEND=========================
fname = "data.txt"
myfile = open("data2.txt", "rt") 
dta = []
for l in myfile:
    dta.append(l[:-1].split(":"))        
myfile.close()         

def main():
    # boo = False
    # while not boo:

        # pick random idea
    #     n = random.randint(1, 7698)

    #     # extract data
    #     dta = open(fname, 'r', encoding="utf8")
    #     l = dta.readline()
    #     if l[0] != str(n):
    #         for l in dta.readlines():
    #             if l[0] == str(n):
    #                 boo = True
    #                 break
    #     dta.close()

    # # update window
    # l = l.split(",")
    # name.set(l[1])
    # geo.set(l[2]+" "+l[3])
    # coord.set(l[6]+" "+l[7])
    # code.set(l[5])  

        n = random.randint(0, len(dta)-1)

    root.update()

    # map
    img = Image.open("map.png")
    img = np.array(img)
    plt.imshow(img)
    # plt.plot(float(l[7])*(62/36)+410, -float(l[6])*(30/18)+195, "*")
    plt.show()

# =========================FRONTEND=========================
root = Tk()
root.title('RandomAirport')


lname = Label(root, text="Name of Airport : ")
lname.grid(row=0, column=0, padx=5, pady=5)

name = StringVar()
vname = Label(root, textvariable=name)
vname.grid(row=0, column=1, padx=5, pady=5)


lgeo = Label(root, text="Geographical position : ")
lgeo.grid(row=1, column=0, padx=5, pady=5)

geo = StringVar()
vgeo = Label(root, textvariable=geo)
vgeo.grid(row=1, column=1, padx=5, pady=5)


lcoord = Label(root, text="Coordinates : ")
lcoord.grid(row=2, column=0, padx=5, pady=5)

coord = StringVar()
vcoord = Label(root, textvariable=coord)
vcoord.grid(row=2, column=1, padx=5, pady=5)


lcode = Label(root, text="Airport ICAO Code : ")
lcode.grid(row=3, column=0, padx=5, pady=5)

code = StringVar()
vcode = Label(root, textvariable=code)
vcode.grid(row=3, column=1, padx=5, pady=5)


b = Button(root, text="Pick Random", command=main)
b.grid(row=4, column=1, padx=5, pady=5)


root.mainloop()