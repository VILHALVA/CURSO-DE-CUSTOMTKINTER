import customtkinter as ctk #Importando a biblioteca

janela = ctk.CTk() #Criar a nossa janela

#Configurando a nossa janela principal
janela.title("App Teste") #Colocando título
janela.geometry("700x400") #Dimensao inicial da janela

ctk.CTkLabel(janela, text="Curso de Customtkinter - Aula 11 (Entry)", font=("arial", 20, "bold")).pack(pady=20, padx=5)

entry = ctk.CTkEntry(janela, width=300, placeholder_text="Digite o seu nome completo...", placeholder_text_color="green", fg_color="transparent", text_color="teal", font=("arial", 16, "bold"), border_width=2, border_color="#fff", state="normal", corner_radius=20)
entry.pack(pady=20)

def pegar():
    print(entry.get())
    entry.delete("0", "end") 

ctk.CTkButton(janela, width=300, text="Pegar texto", command=pegar).pack()

janela.mainloop() #Rodando a janela