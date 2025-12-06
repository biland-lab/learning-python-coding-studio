# Python Coding Studio - Dokumentasi Lengkap

Selamat datang di repositori **Learning Python Coding Studio**. Repositori ini berisi materi pembelajaran Python dari berbagai sesi, mulai dari dasar hingga pembuatan GUI dengan Tkinter.

---

## 📁 Struktur Direktori

```
Learning Python Coding Studio/
├── sesi-1_15Nov25/          # Sesi 1: Pengenalan Python
│   ├── Hello.py
│   ├── sesi-1.ipynb
│   ├── test.html
│   └── test1.cpp
├── sesi-2_15Nov25/          # Sesi 2: Materi Lanjutan
│   └── sesi-2.ipynb
├── sesi-3.ipynb_22Nov25/    # Sesi 3: 22 November 2025
│   └── sesi-3.ipynb
├── sesi-4_29Nov25/          # Sesi 4: 29 November 2025
│   └── sesi-4.ipynb
├── sesi-7_6Des25/           # Sesi 7: GUI dengan Tkinter (6 Desember 2025)
│   ├── 1label.py
│   ├── 2button.py
│   ├── 3entry.py
│   ├── 4pack.py
│   ├── 5grid.py
│   ├── 6place.py
│   ├── 7errorhandling.py
│   └── readme.md
├── test.ipynb               # File I/O Testing
├── test.txt                 # File Teks Contoh
└── random.txt               # File Teks Random
```

---

## 📚 Deskripsi File

### **Sesi 1: Pengenalan Python (15 November 2025)**

#### 📄 `Hello.py`
**Deskripsi:** Program dasar yang menampilkan pesan ucapan.
```python
print("Hello World!")
print("Helo teman-teman")
```
**Konsep:** Penggunaan fungsi `print()` untuk menampilkan output di konsol.

#### 📓 `sesi-1.ipynb`
Notebook Jupyter berisi materi dan latihan pembelajaran Python dasar di sesi pertama.

#### 📄 `test.html`
File HTML untuk pembelajaran web dasar (file pendukung).

#### 📄 `test1.cpp`
File C++ untuk pembelajaran bahasa pemrograman lain (file referensi).

---

### **Sesi 2: Materi Lanjutan (15 November 2025)**

#### 📓 `sesi-2.ipynb`
Notebook Jupyter yang melanjutkan materi pembelajaran Python dari sesi 1.

---

### **Sesi 3 (22 November 2025)**

#### 📓 `sesi-3.ipynb`
Notebook Jupyter berisi materi pembelajaran Python di sesi ketiga.

---

### **Sesi 4 (29 November 2025)**

#### 📓 `sesi-4.ipynb`
Notebook Jupyter berisi materi pembelajaran Python di sesi keempat.

---

### **Sesi 7: GUI dengan Tkinter (6 Desember 2025)**

Sesi ini fokus pada pembelajaran membuat **Graphical User Interface (GUI)** menggunakan library `tkinter` di Python.

#### 1️⃣ `1label.py` - Membuat Label
**Deskripsi:** Contoh dasar membuat window dan label menggunakan Tkinter.

**Fitur:**
- Membuat window/jendela aplikasi
- Menambahkan judul window
- Mengatur ukuran window (300x250 pixel)
- Membuat multiple labels dengan teks dan font berbeda
- Menggunakan `.pack()` untuk tata letak

**Kode Utama:**
```python
import tkinter as tk
window = tk.Tk()
window.title("My Application")
window.geometry("300x250")
label = tk.Label(window, text="Kelas Python Coding Studio", font=("Calibry",20))
label.pack(pady=10, padx=10)
window.mainloop()
```

---

#### 2️⃣ `2button.py` - Membuat Button
**Deskripsi:** Contoh membuat button interaktif dengan event handler.

**Fitur:**
- Membuat button dengan teks
- Menambahkan fungsi callback saat button diklik
- Menampilkan pesan di console ketika button diklik
- Menggabungkan label dan button

**Kode Utama:**
```python
def klik():
    print("Button di klik user ...")

button = tk.Button(window, text="Klik Saya", command=klik)
button.pack()
```

**Konsep Penting:** Callback function - fungsi yang dijalankan saat event terjadi.

---

#### 3️⃣ `3entry.py` - Membuat Entry (Input Field)
**Deskripsi:** Contoh membuat input field dan memproses input dari user.

**Fitur:**
- Membuat entry widget untuk input user
- Mengambil nilai input dengan `.get()`
- Update label secara dinamis berdasarkan input
- Integrasi dengan button dan label

**Kode Utama:**
```python
def sapa():
    hasil_nama = entry.get()
    label_output.config(text=f"Halo {hasil_nama}!")

entry = tk.Entry(window, width=20)
entry.pack(pady=5)
button = tk.Button(window, text="Sapa Aku", command=sapa)
button.pack()
```

**Konsep Penting:** User input handling dan string formatting.

---

#### 4️⃣ `4pack.py` - Layout Manager: Pack
**Deskripsi:** Demonstrasi penggunaan `.pack()` untuk mengatur tata letak widget.

**Fitur:**
- Membuat multiple widgets (label dan button)
- Menggunakan `.pack()` untuk stacking vertikal
- Layout manager paling sederhana

**Kode Utama:**
```python
tk.Label(window, text="Label 1").pack()
tk.Button(window, text="Button 2").pack()
tk.Label(window, text="Label 3").pack()
```

**Konsep Penting:** Layout manager `.pack()` - menyusun widget secara otomatis.

---

#### 5️⃣ `5grid.py` - Layout Manager: Grid
**Deskripsi:** Demonstrasi penggunaan `.grid()` untuk membuat layout seperti tabel/grid.

**Fitur:**
- Membuat form input dengan layout grid
- Menggunakan rows dan columns untuk posisi widget
- Layout lebih fleksibel dan terstruktur
- Membuat input form sederhana (Nama dan Email)

**Kode Utama:**
```python
nama = tk.Label(window, text="Nama: ")
nama.grid(row=0, column=0, pady=10, padx=10)

entry_nama = tk.Entry(window, width=20)
entry_nama.grid(row=0, column=1, pady=10, padx=10)
```

**Konsep Penting:** Layout manager `.grid()` - pengaturan widget berdasarkan row dan column.

---

#### 6️⃣ `6place.py` - Layout Manager: Place
**Deskripsi:** Demonstrasi penggunaan `.place()` untuk posisi absolut widget.

**Fitur:**
- Menempatkan widget pada koordinat x, y yang spesifik
- Layout paling fleksibel namun manual
- Kontrol penuh atas posisi widget

**Kode Utama:**
```python
button1 = tk.Button(window, text="Button di posisi (x=30, y=50)")
button1.place(x=30, y=50)

button2 = tk.Button(window, text="Button di posisi (x=150, y=120)")
button2.place(x=150, y=120)
```

**Konsep Penting:** Layout manager `.place()` - posisi absolut dengan koordinat x, y.

---

#### 7️⃣ `7errorhandling.py` - Error Handling & Validasi
**Deskripsi:** Contoh handling error dan validasi input user dengan exception handling.

**Fitur:**
- Input validasi untuk memastikan user memasukkan angka
- Menggunakan `try-except` untuk menangani error
- Menampilkan pesan error melalui messagebox popup
- Mencegah division by zero error
- Menampilkan hasil dengan warna hijau jika berhasil

**Kode Utama:**
```python
def hitung_pembagian():
    try:
        angka1 = float(entry_1.get())
        angka2 = float(entry_2.get())
        hasil = angka1/angka2
        hasil_label.config(text=f"Hasil: {hasil}", foreground="green")
    except ValueError:
        messagebox.showerror("Input Salah", "Harap Masukkan Angka Yang Valid")
    except ZeroDivisionError:
        messagebox.showerror("Kesalahan Matematis", "Tidak bisa membagi dengan nol")
```

**Konsep Penting:** Error handling dengan exception, validasi input, dan messagebox.

---

### **File Pendukung**

#### 📓 `test.ipynb`
Notebook berisi contoh:
- Membaca file dengan `.read()`
- Menulis file dengan `.write()`
- Penggunaan path relative (`./` dan `../`)

#### 📄 `test.txt`
File teks contoh berisi:
```
Helo teman-teman koding studio
sekarang kita akan belajar pyhton
```

#### 📄 `random.txt`
File teks yang dibuat dari script `test.ipynb`:
```
ini hanya teks random
```

---

## 🎯 Pembelajaran Progresif

### Urutan Pembelajaran yang Direkomendasikan:

1. **Sesi 1**: Pengenalan dasar Python
   - Fungsi `print()`
   - Konsep dasar pemrograman

2. **Sesi 2-4**: Materi lanjutan Python
   - Variabel, tipe data, kontrol alur
   - Fungsi dan modul

3. **Sesi 7**: GUI dengan Tkinter (Praktik)
   - `1label.py` → Dasar widget
   - `2button.py` → Interaksi user
   - `3entry.py` → Input handling
   - `4pack.py` → Layout pack
   - `5grid.py` → Layout grid
   - `6place.py` → Layout place
   - `7errorhandling.py` → Error handling

---

## 🚀 Cara Menjalankan Script

### Prerequisites:
- Python 3.x terinstall
- Tkinter (biasanya sudah included dengan Python)

### Menjalankan File Python:

```bash
# Navigasi ke folder
cd "sesi-7_6Des25"

# Jalankan script
python 1label.py
python 2button.py
python 3entry.py
# ... dst
```

### Menjalankan Jupyter Notebook:

```bash
jupyter notebook sesi-1.ipynb
```

---

## 📋 Ringkasan Konsep Tkinter

| File | Konsep Utama | Widget Digunakan |
|------|-------------|-----------------|
| `1label.py` | Widget Label & Window Basics | Tk(), Label |
| `2button.py` | Event Handling & Callback | Button, command |
| `3entry.py` | User Input Processing | Entry, .get(), .config() |
| `4pack.py` | Layout Manager Pack | .pack() |
| `5grid.py` | Layout Manager Grid | .grid() dengan row/column |
| `6place.py` | Layout Manager Place | .place() dengan x/y |
| `7errorhandling.py` | Exception Handling | try-except, messagebox |

---

## 💡 Tips & Best Practices

1. **Window Setup**
   ```python
   window = tk.Tk()
   window.title("Judul Aplikasi")
   window.geometry("300x250")  # width x height
   window.mainloop()  # Jangan lupa!
   ```

2. **Padding & Spacing**
   - `pady` = padding vertikal (atas-bawah)
   - `padx` = padding horizontal (kiri-kanan)

3. **Font Styling**
   ```python
   font=("Nama Font", ukuran, "style")  # style: bold, italic
   ```

4. **Event Binding**
   ```python
   button = tk.Button(window, command=nama_fungsi)  # Tanpa ()!
   ```

5. **Widget Configuration**
   ```python
   widget.config(text="Teks baru", foreground="green")
   ```

---

## 📞 Kontak & Informasi

- **Kelas**: Python Coding Studio
- **Tanggal Mulai**: 15 November 2025
- **Sesi Terakhir**: 6 Desember 2025

---

## 📝 Lisensi

Materi pembelajaran ini dibuat untuk keperluan edukasi.

---

**Selamat Belajar! 🎓**
