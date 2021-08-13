import tkinter
from tkinter import ttk
from tkinter.constants import END
from PIL import ImageTk, Image

#Def generate
def clickgenerate():
            if entry_tinggi.get()=="20" or entry_berat.get()=="20" or entry_sepatu.get()=="20": #angka link ke ML
                lbl1=tkinter.Label(window, text="Hello Brother!", font=("Montserrat", 25), background='#f8f4f4')
                lbl1.place(x=485, y=417)
                lbl_pria.configure(image=img_pria, background='#f8f4f4')
            elif entry_tinggi.get()=="10" or entry_berat.get()=="10" or entry_sepatu.get()=="10": #angka link ke ML
                lbl2=tkinter.Label(window, text="Hay Sister!", font=("Montserrat", 25), background='#f8f4f4')
                lbl2.place(x=500, y=417)
                lbl_wanita.configure(image=img_wanita, background='#f8f4f4')

#Def Clear
def clickclear():
    entry_tinggi.delete(0, END)
    entry_berat.delete(0, END)
    entry_sepatu.delete(0, END)

#Main Window
window = tkinter.Tk()
window.geometry("1200x500")
window.resizable(0,0)
window.title('Gender Guess Machine')
window.iconbitmap('logogender.ico')

#Image.Tk (pop up image)
logo_pria = "logopria.png"
img_pria = ImageTk.PhotoImage(Image.open(logo_pria))

logo_wanita = "logowanita.png"
img_wanita = ImageTk.PhotoImage(Image.open(logo_wanita))

#Background Utama
background_utama = ImageTk.PhotoImage(file='background3.jpg')
bckgrd_image = tkinter.Label(window, image=background_utama)
bckgrd_image.place(x=0,y=0,relwidth=1,relheight=1)

#Entry Tinggi
entry_tinggi = tkinter.Entry(window, font=('Josefin Sans', 17), bg="#ebe8eb", borderwidth=0)
entry_tinggi.place(x=85, y=205, width=312, height=48)

#Entry Berat
entry_berat = tkinter.Entry(window, font=('Josefin Sans', 17), bg="#ebe8eb", borderwidth=0)
entry_berat.place(x=85, y=290, width=312, height=48)

#Entry Ukuran Sepatu
entry_sepatu = tkinter.Entry(window, font=('Josefin Sans', 17), bg="#ebe8eb", borderwidth=0)
entry_sepatu.place(x=85, y=370, width=312, height=48)

#Button Clear
button_clear = tkinter.PhotoImage(file='btn_clear.png')
btn_clear = tkinter.Button(window, image=button_clear, bg="#f8f4f4", activebackground="#f8f4f4", borderwidth=0, command=clickclear)
btn_clear.place(x=106, y=431)

#Button Generate
button_generate = tkinter.PhotoImage(file='btn_generate.png')
btn_generate = tkinter.Button(window, image=button_generate, command=clickgenerate, bg="#f8f4f4", activebackground="#f8f4f4", borderwidth=0)
#lbl ttk (pop up)
lbl_pria = ttk.Label(window)
lbl_wanita = ttk.Label(window)
#Position All Button
btn_generate.place(x=237, y=431)
lbl_pria.place(x=428, y=74)
lbl_wanita.place(x=428, y=64)

#Frame Visualisasi Model
frame_model = tkinter.LabelFrame(window, padx=150, pady=100, background='#ebe8eb', borderwidth=0)
frame_model.place(x=844, y=196)
lbl_test = tkinter.LabelFrame(frame_model) #Dummy Frame
lbl_test.pack() #Dummy Frame

window.mainloop()