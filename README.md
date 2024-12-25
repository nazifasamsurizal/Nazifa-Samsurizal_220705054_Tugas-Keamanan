Proyek Enkripsi Teks dengan GUI

Deskripsi Singkat
Proyek ini berisi tiga aplikasi GUI yang dikembangkan menggunakan Python dan Tkinter untuk melakukan enkripsi dan dekripsi teks. Aplikasi ini menggunakan tiga jenis cipher berbeda: Caesar Cipher, DES (Data Encryption Standard), dan Enigma Cipher.

Nama Tugas
1. Caesar Cipher GUI
2. DES Encryption/Decryption GUI
3. Enigma Cipher GUI

Isi Tugas
1. Caesar Cipher GUI
Aplikasi ini memungkinkan pengguna untuk mengenkripsi dan mendekripsi teks menggunakan Caesar Cipher. Pengguna dapat memasukkan teks dan menentukan nilai shift untuk proses enkripsi atau dekripsi.

2. DES Encryption/Decryption GUI
Aplikasi ini memungkinkan pengguna untuk mengenkripsi dan mendekripsi teks menggunakan algoritma DES. Pengguna perlu memasukkan teks dan kunci sepanjang 8 karakter untuk proses enkripsi atau dekripsi.

3. Enigma Cipher GUI
Aplikasi ini memungkinkan pengguna untuk mengenkripsi dan mendekripsi teks menggunakan mesin Enigma yang disederhanakan. Pengguna dapat memasukkan teks serta menentukan posisi awal untuk tiga rotor mesin Enigma.

Cara Menjalankan
1. Clone repository ini:
    ```bash
    git clone https://github.com/username/repository.git
    ```
2. Navigasi ke direktori proyek:
    ```bash
    cd repository
    ```
3. Pastikan Anda memiliki Python dan Tkinter terinstal. Jika belum, Anda bisa menginstalnya menggunakan:
    ```bash
    pip install tk
    ```
4. Untuk menjalankan aplikasi Caesar Cipher GUI:
    ```bash
    python ciphergui.py
    ```
    - Buka terminal atau command prompt.
    - Arahkan ke direktori tempat file `ciphergui.py` berada.
    - Jalankan perintah di atas.
    - Jendela GUI akan terbuka, masukkan teks dan nilai shift, lalu pilih opsi enkripsi atau dekripsi.

5. Untuk menjalankan aplikasi DES Encryption/Decryption GUI:
    ```bash
    python desgui.py
    ```
    - Buka terminal atau command prompt.
    - Arahkan ke direktori tempat file `desgui.py` berada.
    - Jalankan perintah di atas.
    - Jendela GUI akan terbuka, masukkan teks dan kunci sepanjang 8 karakter, lalu pilih opsi enkripsi atau dekripsi.

6. Untuk menjalankan aplikasi Enigma Cipher GUI:
    ```bash
    python enigmagui.py
    ```
    - Buka terminal atau command prompt.
    - Arahkan ke direktori tempat file `enigmagui.py` berada.
    - Jalankan perintah di atas.
    - Jendela GUI akan terbuka, masukkan teks dan posisi awal untuk tiga rotor, lalu pilih opsi enkripsi atau dekripsi.

Setiap aplikasi akan membuka jendela GUI di mana Anda dapat memasukkan teks, kunci (untuk DES), atau nilai shift/posisi rotor (untuk Caesar dan Enigma), dan memilih untuk mengenkripsi atau mendekripsi teks tersebut.

