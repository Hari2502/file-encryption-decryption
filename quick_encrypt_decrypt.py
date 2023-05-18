from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox

# Functions
def generate_key():
    # Generate a new encryption key
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Load the encryption key from a file
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file():
    # Select file to encrypt
    file_path = filedialog.askopenfilename(filetypes=(("All Files", "*.*"),))
    if file_path:
        key = load_key()
        fernet = Fernet(key)
        try:
            with open(file_path, "rb") as file:
                file_data = file.read()
            encrypted_data = fernet.encrypt(file_data)
            encrypted_file_path = file_path + ".encrypted"
            with open(encrypted_file_path, "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
            messagebox.showinfo("Encryption Successful", f"File encrypted successfully.\nEncrypted file: {encrypted_file_path}")
        except Exception as e:
            messagebox.showerror("Encryption Error", str(e))

def decrypt_file():
    # Select file to decrypt
    file_path = filedialog.askopenfilename(filetypes=(("Encrypted Files", "*.encrypted"),))
    if file_path:
        key = load_key()
        fernet = Fernet(key)
        try:
            with open(file_path, "rb") as file:
                encrypted_data = file.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            decrypted_file_path = file_path[:-10]
            with open(decrypted_file_path, "wb") as decrypted_file:
                decrypted_file.write(decrypted_data)
            messagebox.showinfo("Decryption Successful", f"File decrypted successfully.\nDecrypted file: {decrypted_file_path}")
        except Exception as e:
            messagebox.showerror("Decryption Error", str(e))

# Create GUI
window = tk.Tk()
window.title("File Encryption/Decryption Tool")

# Encryption Section
encryption_frame = tk.LabelFrame(window, text="Encryption")
encryption_frame.pack(fill="both", expand="yes", padx=20, pady=10)

encryption_label = tk.Label(encryption_frame, text="Choose a file to encrypt:")
encryption_label.pack(pady=10)

encrypt_button = tk.Button(encryption_frame, text="Encrypt", command=encrypt_file)
encrypt_button.pack(pady=5)

# Decryption Section
decryption_frame = tk.LabelFrame(window, text="Decryption")
decryption_frame.pack(fill="both", expand="yes", padx=20, pady=10)

decryption_label = tk.Label(decryption_frame, text="Choose an encrypted file to decrypt:")
decryption_label.pack(pady=10)

decrypt_button = tk.Button(decryption_frame, text="Decrypt", command=decrypt_file)
decrypt_button.pack(pady=5)

# Key Generation Section
key_frame = tk.LabelFrame(window, text="Key Generation")
key_frame.pack(fill="both", expand="yes", padx=20, pady=10)

key_button = tk.Button(key_frame, text="Generate Key", command=generate_key)
key_button.pack(pady=10)

# Run GUI
window.mainloop()
