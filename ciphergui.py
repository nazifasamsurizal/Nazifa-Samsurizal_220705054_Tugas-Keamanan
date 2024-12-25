import tkinter as tk
from tkinter import ttk

# Caesar Cipher encryption function
def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

# Caesar Cipher decryption function
def deskripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

# Function to process text based on encryption or decryption
def proses_teks():
    text = text_input.get("1.0", tk.END).strip()
    shift = int(entry_shift.get())
    if var.get() == 1:
        result = enkripsi(text, shift)
    else:
        result = deskripsi(text, shift)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

# Setup GUI
root = tk.Tk()
root.title("Cipher Encryption Machine")
root.geometry("1200x600")
root.configure(bg="#2C3E50")

# Style configuration
style = {
    "bg": "#2C3E50",
    "card_bg": "#ECF0F1",
    "font": ("Helvetica", 12, "normal"),  # Normal weight for standard text
    "bold_font": ("Helvetica", 12, "bold"),  # Slightly bolder font
    "title_font": ("Helvetica", 24, "bold"),
    "label_font": ("Helvetica", 12, "bold"),
    "btn_bg": "#2980B9",
    "btn_fg": "#FFFFFF",
    "entry_bg": "#FFFFFF",
    "entry_fg": "#34495E",
}

# Main frame
frame_main = tk.Frame(root, bg=style["card_bg"], bd=2, relief="groove", padx=20, pady=20)
frame_main.place(relx=0.5, rely=0.5, anchor="center", width=1150, height=650)

# Title label
label_title = tk.Label(frame_main, text="Cipher Encryption Machine", bg=style["card_bg"], font=style["title_font"], fg=style["btn_bg"])
label_title.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="nsew")

# Adjust grid weight to center the title properly
frame_main.grid_rowconfigure(0, weight=1)
frame_main.grid_columnconfigure(0, weight=1)
frame_main.grid_columnconfigure(1, weight=1)

# Shift value frame
frame_shift = tk.Frame(frame_main, bg=style["card_bg"])
frame_shift.grid(row=1, column=0, padx=10, pady=10, sticky="w")

label_shift = tk.Label(frame_shift, text="Set Shift Value:", bg=style["card_bg"], font=style["label_font"], fg=style["entry_fg"])
label_shift.grid(row=0, column=0, padx=(0, 10), sticky="w")

entry_shift = tk.Entry(frame_shift, width=5, font=style["font"], bd=3, relief="ridge", bg=style["entry_bg"], fg=style["entry_fg"])
entry_shift.grid(row=0, column=1, padx=10)

# Input frame (Centered horizontally and vertically)
frame_input = tk.Frame(frame_main, bg=style["card_bg"])
frame_input.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

# Configure grid to center the content inside frame_input
frame_input.grid_rowconfigure(0, weight=0)  # Label row does not need to stretch
frame_input.grid_rowconfigure(1, weight=1)  # Content row (Text box) should stretch

frame_input.grid_columnconfigure(0, weight=1)  # Center the text box

# Label for input text
label_input = tk.Label(frame_input, text="Input Text to Encrypt/Decrypt:", bg=style["card_bg"], font=style["label_font"], fg=style["entry_fg"])
label_input.grid(row=0, column=0, padx=(0, 10), pady=(0, 5), sticky="w")

# Input text box (Centered with slightly thicker border)
text_input = tk.Text(frame_input, height=7, width=70, font=style["font"], bd=5, relief="ridge", bg=style["entry_bg"], fg=style["entry_fg"], wrap="word")
text_input.grid(row=1, column=0, pady=(5, 10), sticky="ew")

# Buttons frame
frame_buttons = tk.Frame(frame_main, bg=style["card_bg"])
frame_buttons.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

var = tk.IntVar()
var.set(1)

# Style for round radio buttons
style_round = ttk.Style()
style_round.configure("TRadiobutton", indicatoron=0, padding=5, relief="flat", font=style["bold_font"],
                      background=style["card_bg"], foreground=style["btn_bg"])

# Center radio buttons and process button
frame_buttons.grid_columnconfigure(0, weight=1)
frame_buttons.grid_columnconfigure(1, weight=1)
frame_buttons.grid_columnconfigure(2, weight=1)

# Circular radio buttons and process button with adjusted style for centering
radio_encrypt = ttk.Radiobutton(frame_buttons, text="Encrypt", variable=var, value=1, style="TRadiobutton")
radio_encrypt.grid(row=0, column=0, padx=10, pady=5)

radio_decrypt = ttk.Radiobutton(frame_buttons, text="Decrypt", variable=var, value=2, style="TRadiobutton")
radio_decrypt.grid(row=0, column=1, padx=10, pady=5)

button_process = tk.Button(frame_buttons, text="Process Text", command=proses_teks, font=style["label_font"], bg=style["btn_bg"], fg=style["btn_fg"], bd=0, width=15, height=1, relief="groove")
button_process.grid(row=0, column=2, padx=10, pady=5)

# Output frame (Centered horizontally)
frame_output = tk.Frame(frame_main, bg=style["card_bg"])
frame_output.grid(row=4, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="nsew")

# Configure grid to center the content inside frame_output
frame_output.grid_rowconfigure(0, weight=0)  # Label row does not need to stretch
frame_output.grid_rowconfigure(1, weight=1)  # Content row (Text box) should stretch

frame_output.grid_columnconfigure(0, weight=1)  # Center the text box

# Label for output text
label_output = tk.Label(frame_output, text="Output:", bg=style["card_bg"], font=style["label_font"], fg=style["entry_fg"])
label_output.grid(row=0, column=0, padx=(0, 10), pady=(0, 5), sticky="w")

# Output text box (slightly smaller size, with thicker border)
text_output = tk.Text(frame_output, height=7, width=70, font=style["font"], bd=5, relief="ridge", bg=style["entry_bg"], fg=style["entry_fg"], wrap="word")
text_output.grid(row=1, column=0, pady=(5, 10), sticky="ew")

# Run the main GUI loop
root.mainloop()
