import customtkinter as ctk

janela = ctk.CTk()
janela.title("App Teste")
janela.geometry("700x400")

ctk.CTkLabel(janela, text="Curso de Customtkinter - Aula 19 (Progressbar)", font=("arial", 20, "bold")).pack(pady=20)

progressbar = ctk.CTkProgressBar(janela, width=400, height=30, corner_radius=30, fg_color="#003", progress_color="#060")
progressbar.pack(pady=20)
progressbar.start()
#progressbar.step()
#progressbar.stop()

janela.mainloop()