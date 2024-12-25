from Crypto.Cipher import DES
import tkinter as tk
from tkinter import ttk, messagebox

# Fungsi untuk padding
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Fungsi untuk enkripsi
def encrypt(plain_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return encrypted_text.hex()

# Fungsi untuk dekripsi
def decrypt(encrypted_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    encrypted_text_bytes = bytes.fromhex(encrypted_text)
    decrypted_text = des.decrypt(encrypted_text_bytes).decode('utf-8').rstrip(' ')
    return decrypted_text

# Fungsi untuk menangani enkripsi dan dekripsi melalui GUI
def process_text():
    text = text_input.get("1.0", tk.END).strip()
    key = entry_key.get().strip()

    if len(key) != 8:
        messagebox.showerror("Error", "Key harus 8 karakter")
        return

    if var.get() == 1:
        result = encrypt(text, key)
    else:
        result = decrypt(text, key)
    
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

# Setup GUI
root = tk.Tk()
root.title("DES Encryption/Decryption")
root.geometry("1200x600")
root.configure(bg="#F0F8FF")  # Warna latar belakang biru muda

# Style configuration
style = {
    "bg": "#F0F8FF",  
    "card_bg": "#FFFFFF",  
    "font": ("Helvetica", 12, "normal"),
    "bold_font": ("Helvetica", 12, "bold"),
    "title_font": ("Helvetica", 24, "bold"),
    "label_font": ("Helvetica", 12, "bold"),
    "btn_bg": "#4682B4",  
    "btn_fg": "#FFFFFF",  
    "entry_bg": "#FFFFFF",  
    "entry_fg": "#2C3E50",  
}

# Main frame
frame_main = tk.Frame(root, bg=style["card_bg"], bd=2, relief="groove", padx=20, pady=20)
frame_main.place(relx=0.5, rely=0.5, anchor="center", width=1150, height=650)

# Title label
label_title = tk.Label(frame_main, text="DES Encryption/Decryption", bg=style["card_bg"], font=style["title_font"], fg=style["btn_bg"])
label_title.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="nsew")

# Adjust grid weight to center the title properly
frame_main.grid_rowconfigure(0, weight=1)
frame_main.grid_columnconfigure(0, weight=1)
frame_main.grid_columnconfigure(1, weight=1)

# Key entry frame
frame_key = tk.Frame(frame_main, bg=style["card_bg"])
frame_key.grid(row=1, column=0, padx=10, pady=10, sticky="w")

label_key = tk.Label(frame_key, text="Key (8 karakter):", bg=style["card_bg"], font=style["label_font"], fg=style["entry_fg"])
label_key.grid(row=0, column=0, padx=(0, 10), sticky="w")

entry_key = tk.Entry(frame_key, width=10, font=style["font"], bd=3, relief="ridge", bg=style["entry_bg"], fg=style["entry_fg"])
entry_key.grid(row=0, column=1, padx=10)

# Input frame
frame_input = tk.Frame(frame_main, bg=style["card_bg"])
frame_input.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

frame_input.grid_rowconfigure(0, weight=0)
frame_input.grid_rowconfigure(1, weight=1)
frame_input.grid_columnconfigure(0, weight=1)

label_input = tk.Label(frame_input, text="Input Text:", bg=style["card_bg"], font=style["label_font"], fg=style["entry_fg"])
label_input.grid(row=0, column=0, padx=(0, 10), pady=(0, 5), sticky="w")

text_input = tk.Text(frame_input, height=7, width=70, font=style["font"], bd=5, relief="ridge", bg=style["entry_bg"], fg=style["entry_fg"], wrap="word")
text_input.grid(row=1, column=0, pady=(5, 10), sticky="ew")

# Buttons frame
frame_buttons = tk.Frame(frame_main, bg=style["card_bg"])
frame_buttons.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

var = tk.IntVar()
var.set(1)

style_round = ttk.Style()
style_round.configure("TRadiobutton", indicatoron=0, padding=5, relief="flat", font=style["bold_font"],
                      background=style["card_bg"], foreground=style["btn_bg"])

frame_buttons.grid_columnconfigure(0, weight=1)
frame_buttons.grid_columnconfigure(1, weight=1)
frame_buttons.grid_columnconfigure(2, weight=1)

radio_encrypt = ttk.Radiobutton(frame_buttons, text="Encrypt", variable=var, value=1, style="TRadiobutton")
radio_encrypt.grid(row=0, column=0, padx=10, pady=5)

radio_decrypt = ttk.Radiobutton(frame_buttons, text="Decrypt", variable=var, value=2, style="TRadiobutton")
radio_decrypt.grid(row=0, column=1, padx=10, pady=5)

button_process = tk.Button(frame_buttons, text="Process Text", command=process_text, font=style["label_font"], bg=style["btn_bg"], fg=style["btn_fg"], bd=0, width=15, height=1, relief="groove")
button_process.grid(row=0, column=2, padx=10, pady=5)

# Output frame
frame_output = tk.Frame(frame_main, bg=style["card_bg"])
frame_output.grid(row=4, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="nsew")

frame_output.grid_rowconfigure(0, weight=0)
frame_output.grid_rowconfigure(1, weight=1)
frame_output.grid_columnconfigure(0, weight=1)

label_output = tk.Label(frame_output, text="Output:", bg=style["card_bg"], font=style["label_font"], fg=style["entry_fg"])
label_output.grid(row=0, column=0, padx=(0, 10), pady=(0, 5), sticky="w")

text_output = tk.Text(frame_output, height=7, width=70, font=style["font"], bd=5, relief="ridge", bg=style["entry_bg"], fg=style["entry_fg"], wrap="word")
text_output.grid(row=1, column=0, pady=(5, 10), sticky="ew")

# Run the main GUI loop
root.mainloop()
