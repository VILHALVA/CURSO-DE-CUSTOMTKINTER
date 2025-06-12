# SLIDER
`CTkSlider` é um widget em CustomTkinter que permite aos usuários selecionar um valor dentro de um intervalo especificado. É semelhante ao widget `Scale` do Tkinter, mas possui uma aparência mais moderna e personalizável.

Aqui estão as principais características do `CTkSlider`:

* **Seleção de valor:** Permite aos usuários escolher um valor arrastando o cursor.
* **Personalização:** Permite alterar o estilo, cor, fonte e outras propriedades do slider.
* **Valor mínimo e máximo:** Define o intervalo de valores que podem ser selecionados.
* **Valor inicial:** Define o valor inicial do slider.
* **Orientação:** Pode ser horizontal ou vertical.
* **Eventos:** Fornece eventos para detectar interações do usuário, como arrastar e soltar o cursor.

## Criando um Slider
Para criar um slider básico, use o seguinte código:

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Cria um slider com valor mínimo de 0 e máximo de 100
slider = s.CTkSlider(janela, from_=0, to=100)

# Posiciona o slider no centro da janela
slider.place(relx=0.5, rely=0.5, anchor='c')

# Inicia o loop principal
janela.mainloop()
```

Este código cria uma janela com um slider no centro, permitindo a seleção de valores entre 0 e 100.

## Personalizando o Slider
Você pode personalizar a aparência do `CTkSlider` usando vários métodos e atributos:

* **`from_`**: Define o valor mínimo do intervalo.
* **`to`**: Define o valor máximo do intervalo.
* **`value`**: Define o valor inicial do slider.
* **`width`**: Define a largura do slider.
* **`height`**: Define a altura do slider.
* **`orientation`**: Define a orientação do slider ("horizontal" ou "vertical").
* **`theme`**: Define o tema do slider ("light" ou "dark").
* **`fg_color`**: Define a cor do cursor e do texto.
* **`bg_color`**: Define a cor de fundo.
* **`progress_color`**: Define a cor da barra de progresso.
* **`border_width`**: Define a largura da borda.
* **`corner_radius`**: Define o arredondamento dos cantos.

Aqui está um exemplo de personalização da aparência:

```python
slider.theme("dark")
slider.fg_color = "white"
slider.bg_color = "#333333"
slider.progress_color = "#00ff00"
slider.border_width = 2
slider.corner_radius = 5
```

Este código define o tema como escuro, altera a cor do cursor e do texto para branco, a cor de fundo para #333333, a cor da barra de progresso para verde, a largura da borda para 2 pixels e o arredondamento dos cantos para 5 pixels.

## Eventos
O `CTkSlider` fornece eventos como:

* **`<B1-Motion>`**: Evento disparado quando o cursor é arrastado.
* **`<ButtonRelease-1>`**: Evento disparado ao soltar o cursor.
* **`<ValueChanged>`**: Evento disparado quando o valor do slider muda.

Você pode conectar a esses eventos usando o método `bind`:

```python
def on_slider_change(value):
    print(f"Valor selecionado: {value}")

slider.bind("<ValueChanged>", on_slider_change)
```

Este código define uma função `on_slider_change` que imprime o valor selecionado no console. A função é vinculada ao evento `<ValueChanged>` do `CTkSlider`.


