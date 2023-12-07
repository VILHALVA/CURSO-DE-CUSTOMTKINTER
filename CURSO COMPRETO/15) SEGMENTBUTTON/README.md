# SEGMENTBUTTON
Para colocar um SegmentButton em um aplicativo CustomTkinter, você pode usar o seguinte código:

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Define as opções
opções = ["Opção 1", "Opção 2", "Opção 3"]

# Cria o SegmentButton
segment_button = s.CTkSegmentedButton(master=janela, values=opções)

# Posiciona o widget
segment_button.place(relx=0.5, rely=0.5, anchor="center")

# Inicia o loop principal
janela.mainloop()
```

Este código cria uma janela e um SegmentButton com três opções. O botão é posicionado no centro da janela.

Para personalizar o SegmentButton, você pode usar os seguintes atributos:

* **`values`**: Lista de strings representando as opções.
* **`theme`**: Tema claro ou escuro.
* **`fg_color`**: Cor do texto e bordas.
* **`bg_color`**: Cor de fundo do grupo de botões.
* **`font`**: Família e tamanho da fonte.
* **`width`**: Largura de cada botão.
* **`height`**: Altura de cada botão.
* **`corner_radius`**: Arredondamento dos cantos.
* **`selected_option`**: Opção selecionada inicialmente.
* **`command`**: Função chamada quando uma opção é selecionada.

Por exemplo, para definir o tema como escuro, alterar as cores, definir o estilo da fonte, definir o tamanho e o arredondamento dos cantos, e vincular uma função ao atributo `command`, você pode usar o seguinte código:

```python
segment_button.theme("dark")
segment_button.fg_color = "white"
segment_button.bg_color = "#333333"
segment_button.font = s.CTkFont(size=16, family="Arial")
segment_button.width = 150
segment_button.height = 30
segment_button.corner_radius = 5

def on_option_selected(option):
    print(f"Opção selecionada: {option}")

segment_button.command = on_option_selected
```

Para acessar a opção selecionada atualmente, você pode usar o método `get()`. Por exemplo, para imprimir a opção selecionada, você pode usar o seguinte código:

```python
opção_selecionada = segment_button.get()
print(f"Opção selecionada: {opção_selecionada}")
```

Para desabilitar uma opção específica, você pode usar o atributo `state`. Por exemplo, para desabilitar a segunda opção, você pode usar o seguinte código:

```python
segment_button["values"][1].state = "disabled"
```

Para adicionar ou remover opções dinamicamente, você pode usar os métodos `insert()` e `delete()`. Por exemplo, para adicionar uma nova opção chamada "Opção 4", você pode usar o seguinte código:

```python
segment_button.insert(len(segment_button.values), "Opção 4")
```

Para remover a segunda opção, você pode usar o seguinte código:

```python
segment_button.delete(1)
```