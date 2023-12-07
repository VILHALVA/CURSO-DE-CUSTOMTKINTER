import customtkinter as ctk

janela = ctk.CTk()
janela.title("App Teste")
janela.geometry("700x400")

ctk.CTkLabel(janela, text="Curso de Customtkinter - Aula 18 (RadioButton)", font=("arial", 20, "bold")).pack(pady=20)

def radio_event():
    genero = radio_var.get()
    if genero == 1:
        print("Masculino")
    elif genero == 2:
        print("Feminino")

radio_var = ctk.IntVar(value=0)

radio1 = ctk.CTkRadioButton(janela, text="Masculino", command=radio_event, variable=radio_var, value=1)
radio1.pack()

radio2 = ctk.CTkRadioButton(janela, text="Feminino", command=radio_event, variable=radio_var, value=2)
radio2.pack(pady=10)

janela.mainloop()