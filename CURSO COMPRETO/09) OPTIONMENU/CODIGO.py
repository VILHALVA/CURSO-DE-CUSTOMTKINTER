import customtkinter as ctk # Importando a biblioteca

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste") # Colocando título
janela.geometry("700x400") # Dimensao inicial da janela

ctk.CTkLabel(janela, text="Menu de Opcoes. Aula - 09", font=("arial", 20, "bold")).pack(pady=20, padx=5)

ctk.CTkLabel(janela, text="Escolha o seu mes de nascimento:", font=("arial", 14, "bold")).pack()

mes_var = ctk.StringVar(value="Escolha o mes")

def mes_nascimento(escolha):
    print(f"O seu mes de nascimento e: {escolha}")

mes = ctk.CTkOptionMenu(janela, values=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"], command=mes_nascimento, variable=mes_var, width=250, height=50, corner_radius=20, fg_color="red", button_color="green", button_hover_color="teal", dropdown_fg_color="teal", dropdown_text_color="red", dropdown_font=("arial", 15, "bold"), dropdown_hover_color="white", font=("Arial", 18, "bold"))

mes.pack(pady=10)

janela.mainloop() # Rodando a janela