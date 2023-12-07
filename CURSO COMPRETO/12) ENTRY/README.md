# ENTRY
## Entry em CustomTkinter
`CTkEntry` é um widget em CustomTkinter que permite coletar dados do usuário em sua interface gráfica. É semelhante ao widget `Entry` do Tkinter, mas possui uma aparência mais moderna e personalizável.

Aqui estão as principais características do `CTkEntry`:

* **Entrada de texto:** Permite que o usuário digite texto.
* **Personalização:** Permite alterar o estilo, cor, fonte e outras propriedades da caixa de entrada.
* **Senha:** Pode ser configurado para ocultar o texto digitado como uma senha.
* **Validação:** Permite validar o texto digitado pelo usuário.
* **Eventos:** Fornece eventos para detectar interações do usuário, como digitação e pressionamento de teclas.

### Criando uma Caixa de Entrada
Para criar uma caixa de entrada básica, use o seguinte código:

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Cria uma caixa de entrada
entrada = s.CTkEntry(janela)

# Posiciona a caixa de entrada no centro da janela
entrada.place(relx=0.5, rely=0.5, anchor='c')

# Inicia o loop principal
janela.mainloop()
```

Este código cria uma janela com uma caixa de entrada no centro. O usuário pode digitar texto nesta caixa.

### Personalizando a Caixa de Entrada
Você pode personalizar a aparência do `CTkEntry` usando vários métodos e atributos:

* **`placeholder_text`**: Define o texto exibido na caixa de entrada quando vazia.
* **`show`**: Define se o texto digitado deve ser ocultado como uma senha (True or False).
* **`text`**: Define o texto inicial a ser exibido na caixa de entrada.
* **`width`**: Define a largura da caixa de entrada.
* **`theme`**: Define o tema da caixa de entrada ("light" ou "dark").
* **`fg_color`**: Define a cor do texto.
* **`bg_color`**: Define a cor de fundo.
* **`font`**: Define a fonte do texto.
* **`border_width`**: Define a largura da borda.
* **`corner_radius`**: Define o arredondamento dos cantos.

Aqui está um exemplo de personalização da aparência:

```python
entrada.placeholder_text = "Digite seu nome"
entrada.show = False
entrada.width = 200
entrada.theme("dark")
entrada.fg_color = "white"
entrada.bg_color = "#333333"
entrada.font = s.CTkFont(size=16)
entrada.border_width = 2
entrada.corner_radius = 5
```

Este código define um texto de placeholder, oculta o texto digitado como senha, define a largura, tema, cores, fonte, largura da borda e arredondamento dos cantos.

### Validação de Entrada
Você pode validar o texto digitado pelo usuário usando métodos como:

* **`validatecommand`**: Define um comando que será executado quando o texto for alterado.
* **`validate`**: Define o tipo de validação a ser realizada (e.g., "integer", "alphanumeric").

Aqui está um exemplo de validação para aceitar apenas números inteiros:

```python
def validate_integer(text):
    if text.isdigit() or text == "":
        # Texto válido
        return True
    else:
        # Texto inválido
        return False

entrada.validatecommand = validate_integer
entrada.validate = "integer"
```

Este código define uma função `validate_integer` que verifica se o texto é um número inteiro. A função é então vinculada ao `validatecommand` do `CTkEntry` e o tipo de validação é definido como "integer".

### Eventos
O `CTkEntry` fornece eventos como:

* **`<Key>`**: Evento disparado quando uma tecla é pressionada.
* **`<Return>`**: Evento disparado quando o usuário pressiona Enter.
* **`<FocusIn>`**: Evento disparado quando o usuário foca na caixa de entrada.
* **`<FocusOut>`**: Evento disparado quando o usuário sai da caixa de entrada.

Você pode conectar a esses eventos usando o método `bind`:

```python
def on_key_press(event):
    print(f"Tecla pressionada: {event.keysym}")

entrada.bind("<Key>", on_key_press)
```
