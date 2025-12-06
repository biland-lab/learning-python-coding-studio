import tkinter as tk  # import library

#membuat jendela/ window
window = tk.Tk()
# judul dari window
window.title("My Application")
# ukuran dari window
window.geometry("300x250") # dalam pixel

# function untuk button
def klik():
    print("Button di klik user ...")

# Buat Label
label = tk.Label(window, text="Belajar Membuat Button", font=("Calibry",20))
label.pack(pady=5)

# buat button
button = tk.Button(window, text="Klik Saya", command=klik)
button.pack()

#jalankan gui
window.mainloop()
