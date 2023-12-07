from tkinter import Tk, ttk
from ttkthemes import ThemedStyle

# Criar uma instância da janela principal
janela = Tk()

# Criar uma barra de progresso
barra_progresso = ttk.Progressbar(janela, mode='indeterminate')
barra_progresso.pack(pady=20)

# Aplicar um tema moderno à janela
style = ThemedStyle(janela)
style.set_theme("arc")  # Pode ser "radiance", "clearlooks", etc.

# Iniciar o loop principal
janela.mainloop()
