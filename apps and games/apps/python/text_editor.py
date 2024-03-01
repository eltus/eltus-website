import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import pyperclip

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.file_path = None
        self.changes_saved = True  # Flag to track changes

        self.textarea = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.textarea.pack(expand=True, fill='both')

        self.create_menu()

        # Bind close event to handle closing the program
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_menu(self):
        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As", command=self.save_as_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.on_closing)  # Changed to call on_closing
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.textarea.edit_undo)
        editmenu.add_command(label="Redo", command=self.textarea.edit_redo)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.cut_text)
        editmenu.add_command(label="Copy", command=self.copy_text)
        editmenu.add_command(label="Paste", command=self.paste_text)
        editmenu.add_command(label="Copy to Clipboard", command=self.copy_to_clipboard)
        menubar.add_cascade(label="Edit", menu=editmenu)

        self.root.config(menu=menubar)

    def new_file(self):
        self.textarea.delete(1.0, tk.END)
        self.file_path = None  # Reset file_path
        self.changes_saved = True  # Reset flag

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.textarea.delete(1.0, tk.END)
                    self.textarea.insert(tk.END, file.read())
                    self.root.title(os.path.basename(file_path) + " - Text Editor")
                    self.file_path = file_path  # Update file_path
                    self.changes_saved = True  # Reset flag
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def save_file(self):
        if self.file_path:
            try:
                with open(self.file_path, "w") as file:
                    file.write(self.textarea.get(1.0, tk.END))
                    self.changes_saved = True  # Update flag
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.textarea.get(1.0, tk.END))
                    self.root.title(os.path.basename(file_path) + " - Text Editor")
                    self.file_path = file_path  # Update file_path
                    self.changes_saved = True  # Update flag
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def on_closing(self):
        if not self.changes_saved:
            save_changes = messagebox.askyesnocancel("Save", "Do you want to save the changes?")
            if save_changes:
                self.save_file()
                self.root.destroy()
            elif save_changes is False:  # If user chooses not to save
                self.root.destroy()
            # If cancel, do nothing
        else:
            self.root.destroy()

    def cut_text(self):
        self.textarea.event_generate("<<Cut>>")

    def copy_text(self):
        self.textarea.event_generate("<<Copy>>")

    def paste_text(self):
        self.textarea.event_generate("<<Paste>>")

    def copy_to_clipboard(self):
        selected_text = self.textarea.get(tk.SEL_FIRST, tk.SEL_LAST)
        if selected_text:
            pyperclip.copy(selected_text)

def main():
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
