from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Encryption key
KEY = 123


def encrypt_image():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.bmp"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    try:
        image = Image.open(file_path).convert("RGB")
        pixels = image.load()

        width, height = image.size

        # Manipulate every pixel
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]

                # Basic mathematical pixel operation
                r = (r + KEY) % 256
                g = (g + KEY) % 256
                b = (b + KEY) % 256

                pixels[x, y] = (r, g, b)

        # Save encrypted image
        folder = os.path.dirname(file_path)
        name = os.path.splitext(os.path.basename(file_path))[0]

        output_path = os.path.join(
            folder,
            name + "_encrypted.png"
        )

        image.save(output_path)

        messagebox.showinfo(
            "Success",
            "Image encrypted successfully!\n\nSaved as:\n" + output_path
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


def decrypt_image():
    file_path = filedialog.askopenfilename(
        title="Select Encrypted Image",
        filetypes=[
            ("PNG Files", "*.png"),
            ("Image Files", "*.png *.jpg *.jpeg *.bmp"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    try:
        image = Image.open(file_path).convert("RGB")
        pixels = image.load()

        width, height = image.size

        # Reverse the encryption operation
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]

                r = (r - KEY) % 256
                g = (g - KEY) % 256
                b = (b - KEY) % 256

                pixels[x, y] = (r, g, b)

        # Save decrypted image
        folder = os.path.dirname(file_path)
        name = os.path.splitext(os.path.basename(file_path))[0]

        output_path = os.path.join(
            folder,
            name + "_decrypted.png"
        )

        image.save(output_path)

        messagebox.showinfo(
            "Success",
            "Image decrypted successfully!\n\nSaved as:\n" + output_path
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create application window
root = tk.Tk()
root.title("Pixel Manipulation Image Encryption")
root.geometry("500x350")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Pixel Manipulation for Image Encryption",
    font=("Arial", 18, "bold")
)
title.pack(pady=30)

info = tk.Label(
    root,
    text="Encrypt or decrypt an image using pixel manipulation.",
    font=("Arial", 11)
)
info.pack(pady=10)

encrypt_button = tk.Button(
    root,
    text="Encrypt Image",
    command=encrypt_image,
    font=("Arial", 13, "bold"),
    width=20,
    height=2
)
encrypt_button.pack(pady=15)

decrypt_button = tk.Button(
    root,
    text="Decrypt Image",
    command=decrypt_image,
    font=("Arial", 13, "bold"),
    width=20,
    height=2
)
decrypt_button.pack(pady=15)

exit_button = tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    font=("Arial", 11),
    width=10
)
exit_button.pack(pady=15)

root.mainloop()