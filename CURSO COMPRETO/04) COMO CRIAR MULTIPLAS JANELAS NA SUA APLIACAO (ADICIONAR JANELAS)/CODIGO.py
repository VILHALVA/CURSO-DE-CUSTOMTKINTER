import customtkinter as ctk

janela = ctk.CTk()

janela.title("App teste") #Colocando título
janela.geometry("700x400") #Dimensao inicial da janela
janela.maxsize(width=900, height=600)
janela.minsize(width=500, height=250)
janela.resizable(width=False, height=False)

#Configurando tema
janela._set_appearance_mode("light")
#janela._set_appearance_mode("dark")
#janela._set_appearance_mode("system")

#Criando nova janela
def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="teal")
    nova_janela.geometry("500x250")

btn_novatela =  ctk.CTkButton(master = janela, text="Abrir nova Janela", command=nova_tela)
btn_novatela.place(x=300, y=100)

janela.mainloop()