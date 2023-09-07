import go as tk
from go import messagebox
from go import filedialog

def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
        text.delete("1.0", tk.END)
        text.insert("1.0", content)

def save_file():
    content = text.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(content)

def copy_text():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def cut_text():
    copy_text()
    text.delete(tk.SEL_FIRST, tk.SEL_LAST)

def paste_text():
    text.insert(tk.INSERT, text.clipboard_get())

def undo_action():
    text.edit_undo()

root = tk.Tk()
root.title("Simple Text Editor")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=undo_action)

text = tk.Text(root, wrap=tk.WORD)
text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()
