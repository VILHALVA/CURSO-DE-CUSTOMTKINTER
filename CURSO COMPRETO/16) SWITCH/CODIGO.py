import customtkinter as ctk #Importando a biblioteca

janela = ctk.CTk() #Criar a nossa janela

#Configurando a nossa janela principal
janela.title("App Teste") #Colocando título
janela.geometry("700x400") #Dimensao inicial da janela

ctk.CTkLabel(janela, text="Curso de Customtkinter - Aula 16 (Switch)", font=("arial", 20, "bold")).pack(pady=20, padx=5)

switch_var = ctk.BooleanVar(None)

def event():
    if(switch_var.get()):
        janela._set_appearance_mode("dark")
    else:
        janela._set_appearance_mode("light")

switch = ctk.CTkSwitch(janela, 
                       text=None, 
                       variable=switch_var, 
                       onvalue=True, 
                       offvalue=False, 
                       command=event, 
                       width=30,
                       fg_color="teal",
                       button_length=5)

switch.pack(pady=30)

janela.mainloop() #Rodando a janela
