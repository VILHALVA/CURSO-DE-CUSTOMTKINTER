import customtkinter as ctk

def btn_call():
    print("Botão clicado")

app = ctk.CTk()
app.title("App")
app.geometry("400x200")
app.grid_columnconfigure((0,1), weight=1)

btn = ctk.CTkButton(app, text='Meu Botão', command=btn_call)
btn.grid(row=0, column=0, pady=20, padx=20, stick='ew', columnspan=2)

check = ctk.CTkCheckBox(app, text='CheckBox')
check.grid(row=1, column=0, padx=20, pady=(0,20), sticky='w')

check1 = ctk.CTkCheckBox(app, text='CheckBox1')
check1.grid(row=1, column=1, padx=20, pady=(0,20), sticky='w')

app.mainloop()