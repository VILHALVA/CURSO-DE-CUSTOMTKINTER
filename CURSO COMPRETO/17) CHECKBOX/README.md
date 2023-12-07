# CHECKBOX
O CheckBox é um widget do CustomTkinter que permite aos usuários selecionar uma ou mais opções de um conjunto de opções. É semelhante ao widget `Checkbutton` do Tkinter, mas possui uma aparência mais moderna e personalizável.

Para colocar um CheckBox em um aplicativo CustomTkinter, você pode usar o seguinte código:

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Define as opções
opções = ["Opção 1", "Opção 2", "Opção 3"]

# Cria o CheckBox
check_box = s.CTkCheckBox(master=janela, values=opções)

# Posiciona o widget
check_box.place(relx=0.5, rely=0.5, anchor="center")

# Inicia o loop principal
janela.mainloop()
```

Este código cria uma janela e um CheckBox com três opções. O CheckBox é posicionado no centro da janela.

Para personalizar o CheckBox, você pode usar os seguintes atributos:

* **`values`**: Lista de strings representando as opções.
* **`theme`**: Tema claro ou escuro.
* **`fg_color`**: Cor do texto e bordas.
* **`bg_color`**: Cor de fundo do CheckBox.
* **`font`**: Família e tamanho da fonte.
* **`width`**: Largura do CheckBox.
* **`height`**: Altura do CheckBox.
* **`corner_radius`**: Arredondamento dos cantos.
* **`selected_values`**: Opções selecionadas inicialmente.
* **`command`**: Função chamada quando uma opção é selecionada.

Por exemplo, para definir o tema como escuro, alterar as cores, definir o estilo da fonte, definir o tamanho e o arredondamento dos cantos, e vincular uma função ao atributo `command`, você pode usar o seguinte código:

```python
check_box.theme("dark")
check_box.fg_color = "white"
check_box.bg_color = "#333333"
check_box.font = s.CTkFont(size=16, family="Arial")
check_box.width = 150
check_box.height = 30
check_box.corner_radius = 5

def on_option_selected(values):
    print(f"Opções selecionadas: {values}")

check_box.command = on_option_selected
```

Para acessar as opções selecionadas atualmente, você pode usar o método `get()`. Por exemplo, para imprimir as opções selecionadas, você pode usar o seguinte código:

```python
opções_selecionadas = check_box.get()
print(f"Opções selecionadas: {opções_selecionadas}")
```

Para adicionar ou remover opções dinamicamente, você pode usar os métodos `insert()` e `delete()`. Por exemplo, para adicionar uma nova opção chamada "Opção 4", você pode usar o seguinte código:

```python
check_box.insert(len(check_box.values), "Opção 4")
```

Para remover a segunda opção, você pode usar o seguinte código:

```python
check_box.delete(1)
```

Em resumo, para colocar um CheckBox em um aplicativo CustomTkinter, você precisa:

1. Importar o módulo `customtkinter`.
2. Criar uma janela.
3. Definir as opções do CheckBox.
4. Criar o CheckBox.
5. Posicionar o CheckBox.
6. Inicia o loop principal.

Para personalizar o CheckBox, você pode usar os atributos e métodos descritos acima.