import customtkinter as ctk #Importando a biblioteca

janela = ctk.CTk() #Criar a nossa janela principal = Aula02

janela.title("App teste") #Colocando título
janela.geometry("700x400") #Dimensao inicial da janela
janela.maxsize(width=900, height=600)
janela.minsize(width=500, height=250)
janela.resizable(width=False, height=False)

#Customizando tema da nossa aplicacao = Aula 03
janela._set_appearance_mode("light") #Define o tema como claro
janela._set_appearance_mode("dark") #Define o tema como escuro
janela._set_appearance_mode("system") #Define o tema que foi definido no sistema

janela.mainloop()