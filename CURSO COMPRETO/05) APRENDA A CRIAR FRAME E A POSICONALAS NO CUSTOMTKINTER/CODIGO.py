import customtkinter as ctk

janela = ctk.CTk()

#configurando a janela principal
janela.title("App teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=600)
janela.minsize(width=500, height=250)
janela.resizable(width=False, height=False)

#Aula 05 = Frames
frame1 = ctk.CTkFrame(master = janela, width=200, height=330, bg_color="transparent", fg_color="teal", border_width=10, corner_radius=30, border_color="red")
frame1.place(x=10, y=60)

frame2 = ctk.CTkFrame(master = janela, width=200, height=330, fg_color="green")
frame2.place(x=230, y=60)

frame3 = ctk.CTkFrame(master = janela, width=200, height=330, fg_color="white")
frame3.place(x=450, y=60)

janela.mainloop()