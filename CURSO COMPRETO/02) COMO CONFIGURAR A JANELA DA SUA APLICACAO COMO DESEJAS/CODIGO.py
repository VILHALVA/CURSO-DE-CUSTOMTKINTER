import customtkinter as ctk #Importante a biblioteca

janela = ctk.CTk() #Criar a nossa janela

#Configurando a janela principal
janela.title("App Teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=500)
janela.minsize(width=500, height=300)
janela.resizable(width=False,height=False)
janela.iconify()
janela.deiconify()

janela.mainloop()