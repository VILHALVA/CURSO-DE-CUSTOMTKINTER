# GRID NO CUSTOMTKINTER
O Grid é um layout manager disponível no CustomTkinter que permite organizar seus widgets em uma grade. Ele é mais flexível do que o `pack` e o `place`, pois oferece mais controle sobre o posicionamento e tamanho dos widgets.

Aqui estão alguns pontos importantes sobre o Grid:

**Conceitos:**

* **Linhas e Colunas**: O grid é dividido em linhas e colunas, e cada widget ocupa uma ou mais células.
* **Span**: O `span` define quantas células um widget deve ocupar em uma linha ou coluna.
* **Padding**: O `padding` define o espaço ao redor de um widget.
* **Sticky**: O `sticky` define como um widget deve ser alinhado dentro de sua célula.

**Criando um Grid:**

1. **Importar o módulo:**

```python
import customtkinter as s
```

2. **Criar o grid:**

```python
grid = s.CTkGrid(master=janela)
```

3. **Adicionar widgets ao grid:**

```python
widget1 = s.CTkLabel(master=janela, text="Widget 1")
widget2 = s.CTkButton(master=janela, text="Botão")

grid.add(widget1, row=0, column=0)
grid.add(widget2, row=1, column=0, span=2)
```

**Atributos do Grid:**

* **master**: O widget pai do grid.
* **columnspan**: O número de colunas que um widget deve ocupar.
* **rowspan**: O número de linhas que um widget deve ocupar.
* **sticky**: Como o widget deve ser alinhado dentro de sua célula (N, S, E, W, NE, SE, NW, SW, or center).
* **padx**: Espaço horizontal de preenchimento ao redor do widget.
* **pady**: Espaço vertical de preenchimento ao redor do widget.
* **ipadx**: Espaço horizontal de preenchimento interno do widget.
* **ipady**: Espaço vertical de preenchimento interno do widget.

**Gerenciando o Grid:**

* **`remove(widget)`**: Remove um widget do grid.
* **`move(widget, row, column)`**: Move um widget para uma nova posição no grid.
* **`configure(widget, **kwargs)`**: Altera os atributos de um widget no grid.

**Recursos adicionais:**

* **Documentação do CustomTkinter:** [https://github.com/TomSchimansky/CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* **Tutorial do Grid:** [https://m.youtube.com/watch?v=BSfbjrqIw20](https://m.youtube.com/watch?v=BSfbjrqIw20)

**Exemplos:**

1. **Posicionar dois botões lado a lado:**

```python
button1 = s.CTkButton(master=janela, text="Botão 1")
button2 = s.CTkButton(master=janela, text="Botão 2")

grid.add(button1, row=0, column=0)
grid.add(button2, row=0, column=1)
```

2. **Posicionar um título e um input field em uma linha:**

```python
titulo = s.CTkLabel(master=janela, text="Título:")
input_field = s.CTkEntry(master=janela)

grid.add(titulo, row=0, column=0)
grid.add(input_field, row=0, column=1)
```

3. **Posicionar um botão em toda a largura da janela:**

```python
button = s.CTkButton(master=janela, text="Botão")

grid.add(button, row=1, column=0, span=2)
```

O grid é uma ferramenta poderosa que permite criar interfaces flexíveis e organizadas em CustomTkinter.
