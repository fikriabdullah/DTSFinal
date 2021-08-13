import tkinter
from tkinter import ttk
from PIL import ImageTk, Image

root = tkinter.Tk()
root.geometry("500x500")

background_utama = ImageTk.PhotoImage(file='Background2.jpg')
bckgrd_image = tkinter.Label(root, image=background_utama)
bckgrd_image.place(x=0,y=0,relwidth=1,relheight=1)

def event_btn1():
        lbl1=tkinter.Label(root, text="Yes, Berhasil", font=("Montserrat", 27))
        lbl1.place(x=200, y=200)

btn1 = tkinter.Button(root, text="cek tombol", command=event_btn1)
btn1.place(x=100, y=100)

root.mainloop()