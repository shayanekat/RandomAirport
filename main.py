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
# extract data
myfile = open("data.txt", "rt") 
dta = []
for l in myfile:
    dta.append(l[:-1].split(":"))        
myfile.close()         

def main():
    # pick random line
    n = random.randint(0, len(dta)-1)

    # update display
    name.set(dta[n][2].lower())
    geo.set(dta[n][3].lower()+" "+dta[n][4].lower())
    coord.set(dta[n][-2]+" "+dta[n][-1])
    code.set(dta[n][0])

    root.update()

    # map
    if [dta[n][-1], dta[n][-2]] != ["0.000", "0.000"]:
        img = Image.open("map.png")
        img = np.array(img)
        plt.imshow(img)
        plt.plot(float(dta[n][-1])*(62/36)+410, -float(dta[n][-2])*(30/18)+195, "*", color="#0000FF")
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