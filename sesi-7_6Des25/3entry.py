import tkinter as tk  # import library

window = tk.Tk()
window.title("My Application")
window.geometry("300x250")

def sapa():      # function untuk button
    hasil_nama = entry.get()
    label_output.config(text= f"Halo {hasil_nama}!")
    # print(f"Halo {hasil_nama}")

# Buat Label
label = tk.Label(window, text="Inputkan namamu: ", font=("Helvetica", 20))
label.pack(pady=5)

# Entry
entry = tk.Entry(window, width=20)
entry.pack(pady=5)

# buat button
button = tk.Button(window, text="Sapa Aku", command=sapa)
button.pack()

label_output = tk.Label(window, text="")
label_output.pack()

#jalankan gui
window.mainloop()