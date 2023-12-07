# PROGRESSBAR
O Progressbar é um widget do CustomTkinter que permite aos usuários visualizar o progresso de uma tarefa. É semelhante ao widget `Progressbar` do Tkinter, mas possui uma aparência mais moderna e personalizável.

Para colocar um Progressbar em um aplicativo CustomTkinter, você pode usar o seguinte código:

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Cria o Progressbar
progressbar = s.CTkProgressbar(master=janela, from_=0, to=100)

# Posiciona o widget
progressbar.place(relx=0.5, rely=0.5, anchor="center")

# Inicia o loop principal
janela.mainloop()
```

Este código cria uma janela e um Progressbar com um valor inicial de 0 e um valor final de 100. O Progressbar é posicionado no centro da janela.

Para personalizar o Progressbar, você pode usar os seguintes atributos:

* **`from_`**: Valor inicial do Progressbar.
* **`to`**: Valor final do Progressbar.
* **`value`**: Valor atual do Progressbar.
* **`orientation`**: Orientação do Progressbar ("horizontal" ou "vertical").
* **`theme`**: Tema claro ou escuro.
* **`fg_color`**: Cor do texto e bordas.
* **`bg_color`**: Cor de fundo do Progressbar.
* **`progress_color`**: Cor da barra de progresso.
* **`border_width`**: Largura da borda.
* **`corner_radius`**: Arredondamento dos cantos.

Por exemplo, para definir o tema como escuro, alterar as cores, definir o estilo da fonte, definir o tamanho e o arredondamento dos cantos, e vincular uma função ao evento `<ProgressChanged>`, você pode usar o seguinte código:

```python
progressbar.theme("dark")
progressbar.fg_color = "white"
progressbar.bg_color = "#333333"
progressbar.progress_color = "#00ff00"
progressbar.border_width = 2
progressbar.corner_radius = 5

def on_progress_changed(value):
    print(f"Progresso: {value}")

progressbar.bind("<ProgressChanged>", on_progress_changed)
```

Para atualizar o valor do Progressbar, você pode usar o método `set()`. Por exemplo, para definir o valor do Progressbar para 50, você pode usar o seguinte código:

```python
progressbar.set(50)
```

Em resumo, para colocar um Progressbar em um aplicativo CustomTkinter, você precisa:

1. Importar o módulo `customtkinter`.
2. Criar uma janela.
3. Definir os valores do Progressbar.
4. Criar o Progressbar.
5. Posicionar o Progressbar.
6. Inicia o loop principal.

Para personalizar o Progressbar, você pode usar os atributos e métodos descritos acima.

Aqui estão alguns exemplos de como usar o Progressbar:

* Você pode usar o Progressbar para visualizar o progresso de um download, um upload ou uma operação de processamento.
* Você pode usar o Progressbar para visualizar o progresso de uma tarefa em um aplicativo de jogos ou multimídia.
* Você pode usar o Progressbar para visualizar o progresso de um processo em um aplicativo de desenvolvimento.

O Progressbar é uma ferramenta versátil que pode ser usada em uma variedade de aplicativos.