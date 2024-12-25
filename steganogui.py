import tkinter as tk
from tkinter import filedialog
from stegano import lsb
import os

def browse_image():
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg")])
    if img_path:
        img_path_entry.delete(0, tk.END)
        img_path_entry.insert(0, img_path)

def browse_save_path():
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG Files", "*.png")])
    if save_path:
        save_path_entry.delete(0, tk.END)
        save_path_entry.insert(0, save_path)

def hide_message():
    img_path = img_path_entry.get().strip()
    message = message_entry.get().strip()
    save_path = save_path_entry.get().strip()

    if not img_path or not os.path.exists(img_path):
        result_label.config(text="Error: Path gambar tidak valid.", fg="red")
        return

    if not message:
        result_label.config(text="Error: Pesan tidak boleh kosong.", fg="red")
        return

    if not save_path:
        result_label.config(text="Error: Path penyimpanan tidak valid.", fg="red")
        return

    try:
        secret = lsb.hide(img_path, message)
        secret.save(save_path)
        result_label.config(text=f"Pesan berhasil disembunyikan di: {save_path}", fg="green")
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="red")

def show_message():
    img_path = img_path_entry.get().strip()

    if not img_path or not os.path.exists(img_path):
        result_label.config(text="Error: Path gambar tidak valid.", fg="red")
        return

    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
            result_label.config(text=f"Pesan tersembunyi: {clear_message}", fg="green")
        else:
            result_label.config(text="Tidak ada pesan tersembunyi dalam gambar.", fg="orange")
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="red")

# Warna tema ungu pastel
bg_color = "#F3E5F5"  # Light Lavender background
header_color = "#D1C4E9"  # Soft Purple header
button_color = "#B39DDB"  # Light Purple Button
text_color = "#4A148C"  # Dark Purple Text

# Set up root window
root = tk.Tk()
root.title("Steganography Tool")
root.configure(bg=bg_color)
root.geometry("600x400")
root.resizable(True, True)

# Heading
header_label = tk.Label(root, text="Steganography Tool", font=("Arial", 18, "bold"), bg=header_color, fg=text_color, pady=10)
header_label.pack(fill="x")

# Frame untuk input
input_frame = tk.Frame(root, bg=bg_color)
input_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Path gambar
img_path_label = tk.Label(input_frame, text="Path Gambar:", font=("Arial", 12), bg=bg_color, fg=text_color)
img_path_label.grid(row=0, column=0, sticky="w", pady=5)
img_path_entry = tk.Entry(input_frame, font=("Arial", 12))
img_path_entry.grid(row=0, column=1, sticky="ew", pady=5, padx=5)
browse_img_button = tk.Button(input_frame, text="Browse", command=browse_image, bg=button_color, font=("Arial", 10))
browse_img_button.grid(row=0, column=2, padx=5)

# Pesan tersembunyi
message_label = tk.Label(input_frame, text="Pesan:", font=("Arial", 12), bg=bg_color, fg=text_color)
message_label.grid(row=1, column=0, sticky="w", pady=5)
message_entry = tk.Entry(input_frame, font=("Arial", 12))
message_entry.grid(row=1, column=1, sticky="ew", pady=5, padx=5)

# Path penyimpanan
save_path_label = tk.Label(input_frame, text="Simpan ke:", font=("Arial", 12), bg=bg_color, fg=text_color)
save_path_label.grid(row=2, column=0, sticky="w", pady=5)
save_path_entry = tk.Entry(input_frame, font=("Arial", 12))
save_path_entry.grid(row=2, column=1, sticky="ew", pady=5, padx=5)
browse_save_button = tk.Button(input_frame, text="Browse", command=browse_save_path, bg=button_color, font=("Arial", 10))
browse_save_button.grid(row=2, column=2, padx=5)

# Atur grid weight untuk responsivitas
input_frame.columnconfigure(1, weight=1)

# Frame untuk tombol aksi
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=10)

hide_button = tk.Button(button_frame, text="Sembunyikan Pesan", command=hide_message, bg=button_color, font=("Arial", 12))
hide_button.grid(row=0, column=0, padx=10)
show_button = tk.Button(button_frame, text="Tampilkan Pesan", command=show_message, bg=button_color, font=("Arial", 12))
show_button.grid(row=0, column=1, padx=10)

# Frame untuk output
output_frame = tk.Frame(root, bg=bg_color)
output_frame.pack(pady=10, fill="both")

result_label = tk.Label(output_frame, text="", font=("Arial", 12), bg=bg_color, fg=text_color)
result_label.pack()

root.mainloop()
