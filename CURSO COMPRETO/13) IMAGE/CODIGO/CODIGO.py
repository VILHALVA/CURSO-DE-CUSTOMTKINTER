import customtkinter as ctk #Importando a biblioteca
from PIL import Image

janela = ctk.CTk() #Criar a nossa janela

#Configurando a nossa janela principal
janela.title("App Teste") #Colocando título
janela.geometry("700x400") #Dimensao inicial da janela

ctk.CTkLabel(janela, text="Curso de Customtkinter - Aula 13 (Imagem)", font=("arial", 20, "bold")).pack(pady=20, padx=5)

img = ctk.CTkImage(light_image=Image.open("./images/youtube.png"), dark_image=Image.open("./images/youtube.png"))

img1 = ctk.CTkImage(light_image=Image.open("./images/img.png"), dark_image=Image.open("./images/img.png"), size=(250,250))

ctk.CTkLabel(janela, text=None, image=img1).pack()

def evento():
    print("Ja foi para o Youtube")

ctk.CTkButton(janela, text="Youtube", image=img, command=evento, width=300, height=70, fg_color="transparent", hover_color="green", text_color="red", font=("arial", 18, "bold"), border_color="#fff", border_width=3, border_spacing=2, corner_radius=20, state="normal").pack(pady=30)

janela.mainloop() #Rodando a janela