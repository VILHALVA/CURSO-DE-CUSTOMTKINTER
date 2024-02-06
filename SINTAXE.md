# SINTAXE:
```python
import customtkinter as ctk

# Criar a janela principal
janela = ctk.CTk()

# Definir o título da janela
janela.title("Exemplo CustomTkinter")

# Definir o tamanho da janela
janela.geometry("400x200")

# Criar um label
label = ctk.CTkLabel(janela, text="Olá, mundo!")

# Posicionar o label no centro da janela
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Criar um botão
botao = ctk.CTkButton(janela, text="Fechar")

# Posicionar o botão na parte inferior da janela
botao.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

# Definir a função que será executada quando o botão for clicado
def fechar_janela():
    janela.destroy()

# Associar a função ao evento de clique do botão
botao.configure(command=fechar_janela)

# Iniciar o loop principal da janela
janela.mainloop()
```

**Explicação do código:**

* Importamos a biblioteca `customtkinter` como `ctk`.
* Criamos a janela principal usando a classe `CTk`.
* Definimos o título da janela usando o método `title()`.
* Definimos o tamanho da janela usando o método `geometry()`.
* Criamos um label usando a classe `CTkLabel`.
* Definimos o texto do label usando o parâmetro `text`.
* Posicionamos o label no centro da janela usando o método `place()`.
* O parâmetro `relx` define a posição horizontal do label em relação à largura da janela.
* O parâmetro `rely` define a posição vertical do label em relação à altura da janela.
* O parâmetro `anchor` define a posição do label dentro da área de posicionamento.
* Criamos um botão usando a classe `CTkButton`.
* Definimos o texto do botão usando o parâmetro `text`.
* Posicionamos o botão na parte inferior da janela usando o método `place()`.
* Definimos a função que será executada quando o botão for clicado usando o parâmetro `command`.
* Associamos a função ao evento de clique do botão usando o método `configure()`.
* Iniciamos o loop principal da janela usando o método `mainloop()`.


