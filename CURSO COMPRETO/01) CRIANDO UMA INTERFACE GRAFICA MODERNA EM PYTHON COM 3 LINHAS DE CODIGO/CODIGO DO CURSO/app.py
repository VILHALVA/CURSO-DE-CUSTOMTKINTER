import customtkinter as ctk #Importando a biblioteca

janela = ctk.CTk() #Criar a nossa janela

#janela._set_appearance_mode("dark")

btn = ctk.CTkButton(janela, text="Ola")
btn.pack()

janela.mainloop()