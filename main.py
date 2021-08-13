import tkinter
from PIL import ImageTk, Image

#tampilan atas window
layar1 = tkinter.Tk()
layar1.geometry("800x400")
layar1.resizable(0,0)
layar1.title('Employee Management System')
layar1.iconbitmap('logo_aplikasi.ico')

#background foto
bglayar1 = ImageTk.PhotoImage(file='bg2.jpg')
bglayar1_image= tkinter.Label(layar1, image=bglayar1).place(x=0,y=0,relwidth=1,relheight=1)

#BUTTON INPUT PEGAWAI
input_pegawai = tkinter.PhotoImage(file='btn_input.png')
# img_label = tkinter.Label(image=input_pegawai)
# img_label.place(x=538, y=130)
btn_inptpegawai = tkinter.Button(layar1, image=input_pegawai, bg="#081c4c", activebackground="#081c4c", borderwidth=0)
btn_inptpegawai.place(x=538, y=130)

#BUTTON DAFTAR PEGAWAI
daftar_pegawai = tkinter.PhotoImage(file='btn_daftar.png')
img_label = tkinter.Label(image=input_pegawai, bg="#081c4c")
img_label.place(x=538, y=222)
# btn_dftrpegawai = tkinter.Button(layar1, image=daftar_pegawai, bg="#081c4c", activebackground="#081c4c", borderwidth=0)
# btn_dftrpegawai.place(x=538, y=222)

#BUTTON EXIT PROGRAM
ext_program = tkinter.PhotoImage(file='btn_exit.png')
# img_label = tkinter.Label(image=input_pegawai)
# img_label.place(x=538, y=130)
btn_extprogram = tkinter.Button(layar1, image=ext_program, bg="#081c4c", activebackground="#081c4c", borderwidth=0, command=layar1.quit)
btn_extprogram.place(x=694, y=329)

layar1.mainloop()