import customtkinter as ctk #Importando a biblioteca

janela = ctk.CTk() #Criar a nossa janela

#Configurando a nossa janela principal
janela.title("App Teste") #Colocando título
janela.geometry("700x400") #Dimensao inicial da janela

ctk.CTkLabel(janela, text="Curso de Customtkinter - Aula 15 (Segmented Button)", font=("arial", 20, "bold")).pack(pady=20, padx=5)

def btn(value):
    print("Está no segmento de: " + value)

segment = ctk.CTkSegmentedButton(janela,   
                                 values=["TKinter", "Django", "Flask"], 
                                 command=btn,
                                 fg_color="teal",
                                 selected_color="red",
                                 selected_hover_color="green",
                                 border_width=5,
                                 width=10,
                                 corner_radius=30,
                                 unselected_color="blue",
                                 unselected_hover_color="yellow")

segment.pack(pady=20)
segment.set("Django")

janela.mainloop() #Rodando a janela
