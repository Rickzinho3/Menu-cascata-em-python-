import tkinter as tk
from tkinter import messagebox

def about():
    messagebox.showinfo("Sobre", "Este é um programa de exemplo.")

def quit_app():
    window.quit()

def open_file():
    # Função para abrir um arquivo
    messagebox.showinfo("Abrir", "Abrir arquivo")

def save_file():
    # Função para salvar um arquivo
    messagebox.showinfo("Salvar", "Salvar arquivo")

def save_as_pdf():
    # Função para salvar como PDF
    messagebox.showinfo("Salvar Como PDF", "Salvar como PDF")

def save_as_text():
    # Função para salvar como texto
    messagebox.showinfo("Salvar Como Texto", "Salvar como texto")

def exit_without_saving():
    # Função para sair sem salvar
    messagebox.showinfo("Sair sem Salvar", "Sair sem salvar")

def cut():
    # Função para recortar
    messagebox.showinfo("Recortar", "Recortar")

def copy():
    # Função para copiar
    messagebox.showinfo("Copiar", "Copiar")

def paste():
    # Função para colar
    messagebox.showinfo("Colar", "Colar")

def bold():
    # Função para definir negrito
    messagebox.showinfo("Negrito", "Texto em negrito")

def italic():
    # Função para definir itálico
    messagebox.showinfo("Itálico", "Texto em itálico")

def align_left():
    # Função para alinhar à esquerda
    messagebox.showinfo("Alinhar à Esquerda", "Texto alinhado à esquerda")

def align_center():
    # Função para alinhar ao centro
    messagebox.showinfo("Alinhar ao Centro", "Texto alinhado ao centro")

def align_right():
    # Função para alinhar à direita
    messagebox.showinfo("Alinhar à Direita", "Texto alinhado à direita")

window = tk.Tk()
window.title("Menu de Estilo Cascata")

# Criando a barra de menus
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Criando o menu "Arquivo" com submenus
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Arquivo", menu=file_menu)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Salvar", command=save_file)
file_menu.add_separator()

# Submenu "Salvar Como"
submenu_save = tk.Menu(file_menu, tearoff=False)
file_menu.add_cascade(label="Salvar Como", menu=submenu_save)
submenu_save.add_command(label="Salvar como PDF", command=save_as_pdf)
submenu_save.add_command(label="Salvar como Texto", command=save_as_text)

# Submenu "Sair"
submenu_exit = tk.Menu(file_menu, tearoff=False)
file_menu.add_cascade(label="Sair", menu=submenu_exit)
submenu_exit.add_command(label="Sair do Programa", command=quit_app)
submenu_exit.add_command(label="Sair sem Salvar", command=exit_without_saving)

# Criando o menu "Editar" com submenus
edit_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Editar", menu=edit_menu)
edit_menu.add_command(label="Recortar", command=cut)
edit_menu.add_command(label="Copiar", command=copy)
edit_menu.add_command(label="Colar", command=paste)
edit_menu.add_separator()

# Submenu "Formatar"
submenu_format = tk.Menu(edit_menu, tearoff=False)
edit_menu.add_cascade(label="Formatar", menu=submenu_format)
submenu_format.add_command(label="Negrito", command=bold)
submenu_format.add_command(label="Itálico", command=italic)

# Submenu "Alinhar"
submenu_align = tk.Menu(submenu_format, tearoff=False)
submenu_format.add_cascade(label="Alinhar", menu=submenu_align)
submenu_align.add_command(label="Esquerda", command=align_left)
submenu_align.add_command(label="Centro", command=align_center)
submenu_align.add_command(label="Direita", command=align_right)

# Criando o menu "Ajuda" com submenus
help_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Ajuda", menu=help_menu)
help_menu.add_command(label="Sobre", command=about)

window.mainloop()