import tkinter
from tkinter import ttk
from tkinter.constants import END
from PIL import ImageTk, Image
from sklearn import tree

#Def generate
def clickgenerate():
           # if entry_tinggi.get()=="20" or entry_berat.get()=="20" or entry_sepatu.get()=="20": #angka link ke ML
            #    lbl1=tkinter.Label(window, text="Hello Brother!", font=("Montserrat", 25), background='#f8f4f4')
             #   lbl1.place(x=485, y=417)
              #  lbl_pria.configure(image=img_pria, background='#f8f4f4')
            #elif entry_tinggi.get()=="10" or entry_berat.get()=="10" or entry_sepatu.get()=="10": #angka link ke ML
             #   lbl2=tkinter.Label(window, text="Hay Sister!", font=("Montserrat", 25), background='#f8f4f4')
              #  lbl2.place(x=500, y=417)

              
               # lbl_wanita.configure(image=img_wanita, background='#f8f4f4')

           data = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
                   [166, 65, 40], [190, 90, 47], [175, 64, 39], [165, 49, 40],
                   [171, 75, 42], [157, 55, 39], [181, 85, 43], ]

           # data gender,berurut sesuai dengan datanya (merujuk variabel data)
           gender = ['pria', 'pria', 'wanita', 'wanita',
                     'wanita', 'pria', 'pria', 'wanita',
                     'pria', 'wanita', 'pria', ]

           # memanggil metode DecisionTreeClassifier() dari onjek tree
           klasifikasi = tree.DecisionTreeClassifier()
           # training data, memanggil metode fit(param), param = data dan gender
           klasifikasi = klasifikasi.fit(data, gender)

           # memasukkan data baru untuk di prediksi
           # memanggil metode predict([data])
           databaru = []
           databaru.append(entry_tinggi.get())
           databaru.append(entry_berat.get())
           databaru.append(entry_sepatu.get())
           prediksi = klasifikasi.predict([databaru])
           # print hasil prediksi
           print(databaru)
           # print(type(data))
           print(prediksi)

           if prediksi == "wanita" :
                lbl1 = tkinter.Label(window, text="Hay Sister!", font=("Montserrat", 25), background='#f8f4f4')
                lbl1.place(x=485, y=417)
                lbl_wanita.configure(image=img_wanita, background='#f8f4f4')
           elif prediksi == "pria" :
               lbl1 = tkinter.Label(window, text="Hello Brother!", font=("Montserrat", 25), background='#f8f4f4')
               lbl1.place(x=485, y=417)
               lbl_pria.configure(image=img_pria, background='#f8f4f4')


#Def Clear
def clickclear():
    entry_tinggi.delete(0, END)
    entry_berat.delete(0, END)
    entry_sepatu.delete(0, END)
    lbl_pria.configure(image='', background='#f8f4f4')
    lbl_wanita.configure(image='', background='#f8f4f4')
    lbl1 = tkinter.Label()
    lbl1['text'] = ""



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


# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split # Import train_test_split function
# from sklearn import tree # decision tree

# #Mengambil dataset
# df = pd.read_csv('Downloads/weight-height.csv')

# # Mengambil feature dan target
# feature_cols = ['Height', 'Weight']
# X = df[feature_cols]
# y = df['Gender']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) # 70% training and 30% test

# # memanggil metode DecisionTreeClassifier() dari onjek tree
# clf = tree.DecisionTreeClassifier(max_depth=3)
# # training data, memanggil metode fit(param), param = data dan gender
# clf = clf.fit(X_train, y_train)

# # memasukkan data baru untuk di prediksi
# # memanggil metode predict([data])

# databaru = [32, 162]
# y_pred = clf.predict([databaru]) #Ditampilkan untuk hasil prediksi




# Update untuk ukuran sepatu

# df = pd.read_csv('prediksi_gender.csv')

# feature_cols = ['tinggi', 'berat', 'ukuran_sepatu']
# X = df[feature_cols]
# y = df['gender']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) # 70% training and 30% test

# plt.figure(figsize=(8, 8))
# tree.plot_tree(clf, filled=True)

# y_train_pred = clf.predict(X_train)
# y_test_pred = clf.predict(X_test)

# print(accuracy_score(y_train, y_train_pred))
# confusion_matrix(y_train, y_train_pred)