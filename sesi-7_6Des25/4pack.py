import tkinter as tk  # import library

window = tk.Tk()
window.title("My Application")

tk.Label(window, text="Label 1").pack()
tk.Button(window, text="Button 2").pack()
tk.Label(window, text="Label 3").pack()

window.mainloop()

"""
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
"""