import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

class ImageToPdfConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.pdf_input_name = tk.StringVar(value="output.pdf")
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.initialize_ui()
        
    def initialize_ui(self):
        title_label = tk.Label(self.root, text="Image to PDF Converter", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)
        
        # Listbox packen
        self.selected_images_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        # Buttons
        select_button = tk.Button(self.root, text="Select Images", command=self.select_images)
        select_button.pack(pady=5)

        name_frame = tk.Frame(self.root)
        name_frame.pack(pady=5)
        tk.Label(name_frame, text="PDF Name:").pack(side=tk.LEFT)
        tk.Entry(name_frame, textvariable=self.pdf_input_name).pack(side=tk.LEFT)

        convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_to_pdf)
        convert_button.pack(pady=10)

    def select_images(self):
        paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if paths:
            self.image_paths.extend(paths)
            self.update_listbox()

    def update_listbox(self):
        self.selected_images_listbox.delete(0, tk.END)
        for path in self.image_paths:
            self.selected_images_listbox.insert(tk.END, os.path.basename(path))

    def convert_to_pdf(self):
        if not self.image_paths:
            messagebox.showerror("Error", "No images selected!")
            return

        images = []
        for path in self.image_paths:
            img = Image.open(path).convert('RGB')  # Alle Bilder in RGB konvertieren
            images.append(img)

        pdf_name = self.pdf_input_name.get().strip()
        if not pdf_name.lower().endswith(".pdf"):
            pdf_name += ".pdf"

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=pdf_name)
        if save_path:
            images[0].save(save_path, save_all=True, append_images=images[1:])
            messagebox.showinfo("Success", f"PDF saved as {os.path.basename(save_path)}")

def main():
    root = tk.Tk()
    root.title("Image to PDF")
    root.geometry("450x500")
    app = ImageToPdfConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
