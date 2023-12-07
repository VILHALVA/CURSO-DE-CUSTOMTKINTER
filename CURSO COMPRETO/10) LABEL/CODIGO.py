import customtkinter as ctk #Importando a biblioteca

janela = ctk.CTk() #Criar a nossa janela

#Configurando a nossa janela principal
janela.title("App Teste") #Colocando título
janela.geometry("700x400") #Dimensao inicial da janela

ctk.CTkLabel(janela, text="Curso de Customtkinter - Aula 10 (Label)", font=("arial", 20, "bold")).pack(pady=20)
ctk.CTkLabel(janela, text="Este texto é estático de um Label").pack()

#Trabalhando com label de forma dinamica
#1 forma introduzindo texto por input
"""
text_var = ctk.StringVar(value=input("Digite o seu nome completo: "))
lab = ctk.CTkLabel(janela, textvariable=text_var, width=200, height=25, text_color="red", font=("arial", 16, "bold"))
lab.pack(pady=10)
"""
#Introduzindo texto por entry (forma mais prática)
def modificar():
    lab.configure(text=entry.get())

lab = ctk.CTkLabel(janela, text="", text_color="red", font=("arial", 16, "bold"), fg_color="teal", corner_radius=10)
lab.pack(pady=10)

entry = ctk.CTkEntry(janela, width=200)
entry.pack()

ctk.CTkButton(janela, width=200, text="enviar", command=modificar).pack(pady=10)

janela.mainloop() #Rodando a janela