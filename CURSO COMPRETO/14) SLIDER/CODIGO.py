import customtkinter as ctk #Importando a biblioteca

def slider_event(value):
    if(value == slider.cget("to")):
        slider.configure(fg_color="white")
    label.configure(text=int(value))

janela = ctk.CTk() #Criar a nossa janela

#Configurando a nossa janela principal
janela.title("App Teste") #Colocando título
janela.geometry("700x400") #Dimensao inicial da janela

ctk.CTkLabel(janela, text="Curso de Customtkinter - Aula 14 (Slider)", font=("arial", 20, "bold")).pack(pady=20, padx=5)

label = ctk.CTkLabel(janela)
label.pack()

slider = ctk.CTkSlider(janela, from_=10, to=100, command=slider_event, width=500, button_color="#ddd", button_hover_color="red", bg_color="#102", progress_color="red", button_length=10, corner_radius=10, fg_color="gray")
slider.pack()

label.configure(text=int(slider.get()))

janela.mainloop() #Rodando a janela