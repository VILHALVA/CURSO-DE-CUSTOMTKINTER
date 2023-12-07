# LABEL
## Label em CustomTkinter
`CTkLabel` é um widget em CustomTkinter que permite exibir texto na sua interface gráfica. É semelhante ao widget `Label` do Tkinter, mas possui uma aparência mais moderna e personalizável.

Aqui estão as principais características do `CTkLabel`:

* **Exibe texto:** Apresenta o texto fornecido na interface.
* **Personalização:** Permite alterar o estilo, cor, fonte e outras propriedades do texto.
* **Alinhamento:** Controla o alinhamento do texto (esquerda, centro, direita).
* **Interação:** Pode ser usado para interagir com o usuário em alguns casos.

### Criando um Label
Para criar um label básico, use o seguinte código:

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Cria o label com o texto "Olá, mundo!"
label = s.CTkLabel(janela, text="Olá, mundo!")

# Posiciona o label no centro da janela
label.place(relx=0.5, rely=0.5, anchor='c')

# Inicia o loop principal
janela.mainloop()
```

Este código cria uma janela com um label no centro exibindo "Olá, mundo!".

### Personalizando o Label
Você pode personalizar a aparência do `CTkLabel` usando vários métodos e atributos:

* **`text`**: Define o texto a ser exibido.
* **`theme`**: Define o tema do label ("light" ou "dark").
* **`fg_color`**: Define a cor do texto.
* **`bg_color`**: Define a cor de fundo.
* **`font`**: Define a fonte do texto.
* **`width`**: Define a largura do label.
* **`height`**: Define a altura do label.
* **`justify`**: Define o alinhamento do texto (LEFT, CENTER, RIGHT).
* **`corner_radius`**: Define o arredondamento dos cantos.

Aqui está um exemplo de personalização da aparência:

```python
label.theme("dark")
label.fg_color = "white"
label.bg_color = "#333333"
label.font = s.CTkFont(size=20, family="Arial")
label.width = 200
label.height = 50
label.justify = s.CENTER
label.corner_radius = 10
```

Este código define o tema como escuro, altera a cor do texto para branco, a cor de fundo para #333333, o tamanho e a família da fonte, a largura, a altura, o alinhamento para centralizado e o arredondamento dos cantos para 10 pixels.

### Interação com o Label
Você pode interagir com o `CTkLabel` em alguns casos. Por exemplo, você pode:

* Mudar o texto dinamicamente usando o método `configure(text="novo texto")`.
* Obter o texto atual usando o método `cget("text")`.
* Vinculá-lo a eventos como cliques usando o método `bind(sequence, command)`.

Aqui está um exemplo de como alterar o texto dinamicamente:

```python
def alterar_texto():
    label.configure(text="Texto alterado!")

botao = s.CTkButton(janela, text="Alterar texto", command=alterar_texto)
botao.pack()
```

Este código cria um botão que, ao ser clicado, altera o texto do label para "Texto alterado!".

## Recursos adicionais
* **Documentação oficial:** [https://github.com/TomSchimansky/CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* **Tutorial:** [https://m.youtube.com/watch?v=fKVa7o_ly6A](https://m.youtube.com/watch?v=fKVa7o_ly6A)

Ao entender e usar esses recursos, você pode criar labels personalizados e interativos para suas aplicações CustomTkinter.
