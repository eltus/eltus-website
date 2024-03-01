import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import pyperclip

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        self.textarea = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.textarea.pack(expand=True, fill='both')

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As", command=self.save_as_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit_editor)
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

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.textarea.delete(1.0, tk.END)
                    self.textarea.insert(tk.END, file.read())
                    self.root.title(os.path.basename(file_path) + " - Text Editor")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def save_file(self):
        if self.root.title() == "Text Editor":
            self.save_as_file()
        else:
            try:
                file_path = self.root.title().replace(" - Text Editor", "")
                with open(file_path, "w") as file:
                    file.write(self.textarea.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.textarea.get(1.0, tk.END))
                    self.root.title(os.path.basename(file_path) + " - Text Editor")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def exit_editor(self):
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
