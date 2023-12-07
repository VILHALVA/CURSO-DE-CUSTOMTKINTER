#Place
#Pack
#Grid

import customtkinter as ctk

janela = ctk.CTk()
janela.title("App Teste")
janela.geometry("700x400")

btn1 = ctk.CTkButton(janela, text="BOTAO 1")
btn1.place(x=100, y=200)

btn2 = ctk.CTkButton(janela, text="BOTAO 2")
btn2.place(x=70, y=40)

#Posicionando com meia responsividade
btn3 = ctk.CTkButton(janela, text="BOTAO 3")
btn3.place(relx=0.1, rely=0.2)

janela.mainloop()