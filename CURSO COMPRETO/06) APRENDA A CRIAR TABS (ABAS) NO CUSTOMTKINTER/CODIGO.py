import customtkinter as ctk

janela = ctk.CTk()

#configurando a janela principal
janela.title("App teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=600)
janela.minsize(width=500, height=250)
janela.resizable(width=False, height=False)

#Aula 06 = Tabview (Abas no tkinter)
tabView = ctk.CTkTabview(janela,width=680, height=390, corner_radius=20, border_width=5, border_color="black", fg_color="teal", segmented_button_fg_color="black", segmented_button_selected_color="green", segmented_button_selected_hover_color="darkgreen", segmented_button_unselected_color="blue", segmented_button_unselected_hover_color="darkblue")
tabView.pack()
tabView.add("Nomes")
tabView.add("Idades")
tabView.add("Genero")
tabView.tab("Nomes").grid_columnconfigure(0, weight=1)
tabView.tab("Idades").grid_columnconfigure(0, weight=1)
tabView.tab("Genero").grid_columnconfigure(0, weight=1)

#Adicionando elementos na nossa tab
text = ctk.CTkLabel(tabView.tab("Nomes"), text="Salvador Eduardo\nEugenio Eduardo\nAntonia Tomocene", text_color="white")
text.pack()

idd = ctk.CTkLabel(tabView.tab("Idades"), text="23\n31\n42", text_color="white")
idd.pack()

idd = ctk.CTkLabel(tabView.tab("Genero"), text="Masculino\nMasculino\nFeminino", text_color="white")
idd.pack()

janela.mainloop()