# INTRODUÇÃO, INSTALAÇÃO E CONFIGURAÇÃO:
## Introdução:
Customtkinter é uma biblioteca Python que fornece uma interface de usuário (UI) baseada em Tkinter. Tkinter é a biblioteca de UI padrão do Python, mas é um pouco limitada. Customtkinter adiciona uma série de recursos e melhorias a Tkinter, tornando-o mais poderoso e flexível.

## Instalação:
Para instalar Customtkinter, você pode usar o gerenciador de pacotes pip:

```
pip install customtkinter
```

## Configuração:
Para usar Customtkinter, você precisa importar a biblioteca:

```python
import customtkinter as tk
```

Você também pode definir o tema da UI:

```python
tk.set_theme("dark")
```

**Exemplo**

Aqui está um exemplo simples de como usar Customtkinter:

```python
import customtkinter as tk

root = tk.Tk()

# Cria um botão
button = tk.Button(root, text="Clique aqui")

# Adiciona o botão à janela
button.pack()

# Inicia o loop da GUI
root.mainloop()
```

Este código cria uma janela com um botão. Quando você clica no botão, ele imprime uma mensagem na console.

## Conceitos básicos:
Customtkinter fornece uma série de novos conceitos além dos fornecidos por Tkinter. Aqui estão alguns dos conceitos básicos:

* **Widgets**

Widgets são os componentes básicos da UI. Customtkinter fornece uma variedade de widgets novos e aprimorados, incluindo:

    * **Button**
    * **Entry**
    * **Label**
    * **Frame**
    * **Canvas**
    * **Scrollbar**
    * **Menu**
    * **Message**

* **Estilos**

Customtkinter permite que você defina estilos para widgets. Os estilos controlam a aparência dos widgets, incluindo a cor, o tamanho e a fonte.

* **Layout**

Customtkinter fornece uma variedade de ferramentas de layout para organizar widgets na janela.

**Exemplos**

Aqui estão alguns exemplos de como usar os conceitos básicos de Customtkinter:

* **Criando um widget**

```python
import customtkinter as tk

root = tk.Tk()

# Cria um botão
button = tk.Button(root, text="Clique aqui")

# Adiciona o botão à janela
button.pack()

# Inicia o loop da GUI
root.mainloop()
```

Este código cria um botão com o texto "Clique aqui".

* **Definindo um estilo**

```python
import customtkinter as tk

root = tk.Tk()

# Define o estilo do botão
button_style = tk.ButtonStyle()
button_style.configure(foreground="red")

# Cria um botão
button = tk.Button(root, text="Clique aqui", style=button_style)

# Adiciona o botão à janela
button.pack()

# Inicia o loop da GUI
root.mainloop()
```

Este código define o estilo do botão para ter o texto vermelho.

* **Organizando widgets**

```python
import customtkinter as tk

root = tk.Tk()

# Cria dois botões
button1 = tk.Button(root, text="Botão 1")
button2 = tk.Button(root, text="Botão 2")

# Adiciona os botões à janela
button1.pack()
button2.pack()

# Organiza os botões horizontalmente
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)
tk.Grid.pack(button1, row=0, column=0)
tk.Grid.pack(button2, row=0, column=1)

# Inicia o loop da GUI
root.mainloop()
```

Este código adiciona dois botões à janela e os organiza horizontalmente.

**Conclusão**

Customtkinter é uma biblioteca poderosa que pode ser usada para criar interfaces de usuário atraentes e funcionais. Ao aprender os conceitos básicos de Customtkinter, você poderá criar seus próprios aplicativos de GUI personalizados.