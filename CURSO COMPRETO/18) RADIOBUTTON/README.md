# RADIOBUTTON
O RadioButton é um widget do CustomTkinter que permite aos usuários selecionar uma opção de um conjunto de opções mutuamente exclusivas. É semelhante ao widget `Radiobutton` do Tkinter, mas possui uma aparência mais moderna e personalizável.

Para colocar um RadioButton em um aplicativo CustomTkinter, você pode usar o seguinte código:

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Define as opções
opções = ["Opção 1", "Opção 2", "Opção 3"]

# Cria o RadioButton
radio_button = s.CTkRadioButton(master=janela, values=opções)

# Posiciona o widget
radio_button.place(relx=0.5, rely=0.5, anchor="center")

# Inicia o loop principal
janela.mainloop()
```

Este código cria uma janela e um RadioButton com três opções. O RadioButton é posicionado no centro da janela.

Para personalizar o RadioButton, você pode usar os seguintes atributos:

* **`values`**: Lista de strings representando as opções.
* **`theme`**: Tema claro ou escuro.
* **`fg_color`**: Cor do texto e bordas.
* **`bg_color`**: Cor de fundo do RadioButton.
* **`font`**: Família e tamanho da fonte.
* **`width`**: Largura do RadioButton.
* **`height`**: Altura do RadioButton.
* **`corner_radius`**: Arredondamento dos cantos.
* **`selected_value`**: Opção selecionada inicialmente.
* **`command`**: Função chamada quando a opção é selecionada.

Por exemplo, para definir o tema como escuro, alterar as cores, definir o estilo da fonte, definir o tamanho e o arredondamento dos cantos, e vincular uma função ao atributo `command`, você pode usar o seguinte código:

```python
radio_button.theme("dark")
radio_button.fg_color = "white"
radio_button.bg_color = "#333333"
radio_button.font = s.CTkFont(size=16, family="Arial")
radio_button.width = 150
radio_button.height = 30
radio_button.corner_radius = 5

def on_option_selected(value):
    print(f"Opção selecionada: {value}")

radio_button.command = on_option_selected
```

Para acessar a opção selecionada atualmente, você pode usar o método `get()`. Por exemplo, para imprimir a opção selecionada, você pode usar o seguinte código:

```python
opção_selecionada = radio_button.get()
print(f"Opção selecionada: {opção_selecionada}")
```

Para adicionar ou remover opções dinamicamente, você pode usar os métodos `insert()` e `delete()`. Por exemplo, para adicionar uma nova opção chamada "Opção 4", você pode usar o seguinte código:

```python
radio_button.insert(len(radio_button.values), "Opção 4")
```

Para remover a segunda opção, você pode usar o seguinte código:

```python
radio_button.delete(1)
```

Em resumo, para colocar um RadioButton em um aplicativo CustomTkinter, você precisa:

1. Importar o módulo `customtkinter`.
2. Criar uma janela.
3. Definir as opções do RadioButton.
4. Criar o RadioButton.
5. Posicionar o RadioButton.
6. Inicia o loop principal.

Para personalizar o RadioButton, você pode usar os atributos e métodos descritos acima.

Aqui estão alguns exemplos de como usar o RadioButton:

* Você pode usar o RadioButton para permitir que os usuários selecionem um gênero, uma preferência de idioma ou um nível de dificuldade.
* Você pode usar o RadioButton para permitir que os usuários selecionem uma opção de menu ou um item de lista.
* Você pode usar o RadioButton para permitir que os usuários selecionem um modo de operação ou uma configuração.

O RadioButton é uma ferramenta versátil que pode ser usada em uma variedade de aplicativos.