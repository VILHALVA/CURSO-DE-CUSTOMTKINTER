import customtkinter as ctk #Importando a biblioteca
from PIL import Image
import os

janela = ctk.CTk() #Criar a nossa janela

#Configurando a nossa janela principal
janela.title("App Teste") #Colocando título
janela.geometry("700x400") #Dimensao inicial da janela

ctk.CTkLabel(janela, text="Curso de Customtkinter - Aula 12 (Button)", font=("arial", 20, "bold")).pack(pady=20, padx=5)

img = ctk.CTkImage(light_image=Image.open("./images/youtube.png"), dark_image=Image.open("./images/youtube.png"), size=(50,50))

def evento():
    os.system("start https://www.youtube.com/watch?v=1ntEudTX_wU")
    print("Ja foi para o Youtube")

def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="teal")
    nova_janela.geometry("500x250")

ctk.CTkButton(janela, text="Youtube", image=img, command=evento, width=300, height=70, fg_color="transparent", hover_color="green", text_color="red", font=("arial", 18, "bold"), border_color="#fff", border_width=3, border_spacing=2, corner_radius=20, state="normal").pack(pady=30)

janela.mainloop() #Rodando a janela