import requests
from tkinter import *

window = Tk()
window.geometry('550x450')
window.title('Scor32k | Name to Image')


def fetch():
    file = f"https://source.unsplash.com/{val5.get()}x{val6.get()}/?{val1.get()},{val2.get()}"
    out = requests.get(file)
    wrte = open(f"{val3.get()}.png", 'wb')
    wrte.write(out.content)


Label(window, text="Search Key Words").grid(row=0, column=6)

val1 = StringVar()
val2 = StringVar()
val3 = StringVar()
val5 = IntVar()
val6 = IntVar()

Label(window, text="Enter the image type 1: ").grid(row=1, column=0)
e1 = Entry(window, textvariable=val1).grid(row=1, column=2)

Label(window, text="Enter the image type 2: ").grid(row=2, column=0)
e2 = Entry(window, textvariable=val2).grid(row=2, column=2)

Label(window, text="Image Name To be Saved: ").grid(row=3, column=0)
Entry(window, textvariable=val3).grid(row=3, column=2)


Label(window, text="width: ").grid(row=4, column=0)
Entry(window, textvariable=val5).grid(row=4, column=2)

Label(window, text="Height:").grid(row=5, column=0)
Entry(window, textvariable=val6).grid(row=5, column=2)


btn = Button(window, text="Fetch!", command=fetch).grid(row=8, column=4)

window.mainloop()
