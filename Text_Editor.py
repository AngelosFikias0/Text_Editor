from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import font as tkFont, colorchooser
from tkinter.messagebox import showinfo

# Functions for the editor
def open_file():
    file = filedialog.askopenfilename(defaultextension='.txt',
                                      filetypes=[
                                          ("Text files", "*.txt"),
                                          ("HTML files", "*.html"),
                                          ("All files", "*.*")
                                      ])
    if file:
        window.title(f"Text Editor - {file}")
        text.delete(1.0, END)
        with open(file, "r") as f:
            text.insert(1.0, f.read())
        status_bar.config(text="Opened file: " + file)

def save_file():
    file = filedialog.asksaveasfilename(defaultextension='.txt',
                                        filetypes=[
                                            ("Text files", "*.txt"),
                                            ("HTML files", "*.html"),
                                            ("All files", "*.*")
                                        ])
    if file:
        filetext = str(text.get(1.0, END))
        with open(file, "w") as f:
            f.write(filetext)
        window.title(f"Text Editor - {file}")
        status_bar.config(text="Saved file: " + file)

def save_as():
    save_file()

def delete_text():
    response = messagebox.askyesno("Delete", "Do you want to clear the text?")
    if response:
        text.delete(1.0, END)
        status_bar.config(text="Text deleted")

def exit_editor():
    response = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if response:
        window.quit()

def col_change():
    color = colorchooser.askcolor(title="Pick a text color")
    text.config(fg=color[1])

def bg_change():
    color = colorchooser.askcolor(title="Pick a background color")
    text.config(bg=color[1])

def font_change(font_family):
    font_text.config(family=font_family)

def size_change(font_size):
    font_text.config(size=font_size)

def about():
    showinfo("About this program:","This program is written by Angelos Fikias, thank you!")

# Main window setup
window = Tk()
window.title("Text Editor")
window.geometry("1000x560")
window.config(bg="#2c3e50")

# Fonts and styling
font_text = tkFont.Font(family="Helvetica", size=12)
font_menu = tkFont.Font(family="Arial", size=10)
bg_color = "#ecf0f1"
text_fg_color = "#2c3e50"
button_color = "#3498db"
button_hover_color = "#2980b9"
status_bg = "#34495e"
status_fg = "#ecf0f1"

# Available fonts and sizes
available_fonts = list(tkFont.families())
default_font = "Helvetica"
default_size = 12

# Menu bar setup
menu_bar = Menu(window, font=font_menu, bg=bg_color, fg=text_fg_color)
window.config(menu=menu_bar)

# File menu
file_menu = Menu(menu_bar, tearoff=0, bg=bg_color, fg=text_fg_color)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Delete", command=delete_text, accelerator="Ctrl+D")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

# Edit menu
edit_menu = Menu(menu_bar, tearoff=0, bg=bg_color, fg=text_fg_color)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Change color of text", command=col_change)
edit_menu.add_separator()
edit_menu.add_command(label="Change color of background", command=bg_change)

# Font submenu
font_submenu = Menu(menu_bar, tearoff=0, bg=bg_color, fg=text_fg_color)
menu_bar.add_cascade(label="Format", menu=font_submenu)

# Font selection submenu
font_selection = Menu(font_submenu, tearoff=0, bg=bg_color, fg=text_fg_color)
for font in available_fonts:
    font_selection.add_command(label=font, command=lambda f=font: font_change(f))
font_submenu.add_cascade(label="Font", menu=font_selection)
font_submenu.add_separator()

# Font size submenu
size_selection = Menu(font_submenu, tearoff=0, bg=bg_color, fg=text_fg_color)
for size in range(8, 73, 2):
    size_selection.add_command(label=str(size), command=lambda s=size: size_change(s))
font_submenu.add_cascade(label="Size", menu=size_selection)

# Help menu
help_menu = Menu(menu_bar, tearoff=0, bg=bg_color, fg=text_fg_color)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Text widget
text = Text(window, wrap='word', font=font_text, bg=bg_color, fg=text_fg_color, undo=True, padx=10, pady=10, insertbackground="black")
text.pack(expand=YES, fill=BOTH, padx=10, pady=10)

# Status bar
status_bar = Label(window, text="Welcome to my Text Editor, by Angelos Fikias", anchor=W, bg=status_bg, fg=status_fg, padx=5, pady=5)
status_bar.pack(side=BOTTOM, fill=X)

# Keyboard shortcuts
window.bind("<Control-s>", lambda event: save_file())
window.bind("<Control-o>", lambda event: open_file())
window.bind("<Control-d>", lambda event: delete_text())

window.mainloop()