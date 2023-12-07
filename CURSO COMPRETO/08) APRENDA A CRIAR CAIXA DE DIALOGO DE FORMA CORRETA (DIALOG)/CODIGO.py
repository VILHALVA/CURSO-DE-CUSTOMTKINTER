import customtkinter as ctk

janela = ctk.CTk()

#configurando a janela principal
janela.title("App teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=600)
janela.minsize(width=500, height=250)
janela.resizable(width=False, height=False)

#Aula 08 - Caixa de Diálogo (dialog)

def abrir():
    dialog = ctk.CTkInputDialog(title="Caixa de Dialogo",text="Digite o seu numero de Celular")
    print("Numero de Celular buscado:", dialog.get_input())

btn = ctk.CTkButton(janela, text="Abrir caixa de Dialogo", command=abrir)
btn.pack()

janela.mainloop()