import customtkinter as ctk

janela = ctk.CTk()
janela.title("App Teste")
janela.geometry("700x400")

ctk.CTkLabel(janela, text="Curso de Customtkinter - Aula 17 (CheckBox)", font=("arial", 20, "bold")).pack(pady=20)

def check_event():
    if check_var.get():
        janela._set_appearance_mode("dark")
    else:
        janela._set_appearance_mode("light")

check_var = ctk.BooleanVar(value=False)
checkbox = ctk.CTkCheckBox(janela, text="Altere o tema", variable=check_var, onvalue=True, offvalue=False, command=check_event)
checkbox.pack(pady=10)

janela.mainloop()