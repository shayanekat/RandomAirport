"""
Programme principale du projet RandomAirport
"""
from tkinter import *
import random

# TODO (30/07/2020): 
#   show in a world map

# =========================BACKEND=========================
fname = "data.txt"

def main():
    boo = False
    while not boo:

        # pick random idea
        n = random.randint(1, 7698)

        # extract data
        dta = open(fname, 'r', encoding="utf8")
        l = dta.readline()
        if l[0] != str(n):
            for l in dta.readlines():
                if l[0] == str(n):
                    boo = True
                    break
        dta.close()

    # update window
    l = l.split(",")
    name.set(l[1])
    geo.set(l[2]+" "+l[3])
    coord.set(l[6]+" "+l[7])
    code.set(l[5])
        
    root.update()

    # map
    m = Basemap(projection='mill')
    m.drawcoastlines()
    plt.plot(int(l[6]), int(l[7]))
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