import customtkinter as ctk

def button_event():
    print("Usuario: " + entry_username.get())
    print("Senha: " + entry_password.get())
    print("-"*30)

janela = ctk.CTk()
janela.title("Sistema de Login")
janela.geometry("400x300")

ctk.CTkLabel(janela, text="Faça Login", font=("arial", 40, "bold")).pack(pady=20)

entry_username = ctk.CTkEntry(janela, placeholder_text="Useraneme...", width=250, height=45)
entry_username.pack(pady=5)

entry_password = ctk.CTkEntry(janela, placeholder_text="Password...", width=250, height=45, show='●')
entry_password.pack(pady=5)

ctk.CTkButton(janela, text="LOGAR", width=250, height=45, command=button_event).pack(pady=20)

janela.mainloop()