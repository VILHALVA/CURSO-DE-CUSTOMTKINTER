# SWITCH
O Switch é um widget do CustomTkinter que permite aos usuários selecionar um valor entre um conjunto de valores mutuamente exclusivos. É semelhante ao widget `Radiobutton` do Tkinter, mas possui uma aparência mais moderna e personalizável.

Para colocar um Switch em um aplicativo CustomTkinter, você pode usar o seguinte código:

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Define os valores
valores = ["Opção 1", "Opção 2", "Opção 3"]

# Cria o Switch
switch = s.CTkSwitch(master=janela, values=valores)

# Posiciona o widget
switch.place(relx=0.5, rely=0.5, anchor="center")

# Inicia o loop principal
janela.mainloop()
```

Este código cria uma janela e um Switch com três valores. O Switch é posicionado no centro da janela.

Para personalizar o Switch, você pode usar os seguintes atributos:

* **`values`**: Lista de strings representando os valores.
* **`theme`**: Tema claro ou escuro.
* **`fg_color`**: Cor do texto e bordas.
* **`bg_color`**: Cor de fundo do Switch.
* **`font`**: Família e tamanho da fonte.
* **`width`**: Largura do Switch.
* **`height`**: Altura do Switch.
* **`corner_radius`**: Arredondamento dos cantos.
* **`selected_value`**: Valor selecionado inicialmente.
* **`command`**: Função chamada quando o valor é alterado.

Por exemplo, para definir o tema como escuro, alterar as cores, definir o estilo da fonte, definir o tamanho e o arredondamento dos cantos, e vincular uma função ao atributo `command`, você pode usar o seguinte código:

```python
switch.theme("dark")
switch.fg_color = "white"
switch.bg_color = "#333333"
switch.font = s.CTkFont(size=16, family="Arial")
switch.width = 150
switch.height = 30
switch.corner_radius = 5

def on_value_changed(value):
    print(f"Valor selecionado: {value}")

switch.command = on_value_changed
```

Para acessar o valor selecionado atualmente, você pode usar o método `get()`. Por exemplo, para imprimir o valor selecionado, você pode usar o seguinte código:

```python
valor_selecionado = switch.get()
print(f"Valor selecionado: {valor_selecionado}")
```

Para adicionar ou remover valores dinamicamente, você pode usar os métodos `insert()` e `delete()`. Por exemplo, para adicionar um novo valor chamado "Opção 4", você pode usar o seguinte código:

```python
switch.insert(len(switch.values), "Opção 4")
```

Para remover o segundo valor, você pode usar o seguinte código:

```python
switch.delete(1)
```

Em resumo, para colocar um Switch em um aplicativo CustomTkinter, você precisa:

1. Importar o módulo `customtkinter`.
2. Criar uma janela.
3. Definir os valores do Switch.
4. Criar o Switch.
5. Posicionar o Switch.
6. Inicia o loop principal.

Para personalizar o Switch, você pode usar os atributos e métodos descritos acima.