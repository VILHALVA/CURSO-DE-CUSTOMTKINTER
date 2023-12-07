# BUTTON
## Button em CustomTkinter
`CTkButton` é um widget em CustomTkinter que permite criar botões interativos em sua interface gráfica. É semelhante ao widget `Button` do Tkinter, mas possui uma aparência mais moderna e personalizável.

Aqui estão as principais características do `CTkButton`:

* **Ação:** Executa uma função predefinida quando clicado.
* **Personalização:** Permite alterar o estilo, cor, fonte e outras propriedades do botão.
* **Texto e ícone:** Pode exibir texto, ícone ou ambos.
* **Estados:** Possui diferentes estados como normal, pressionado, desabilitado e pairando.

### Criando um Botão
Para criar um botão básico, use o seguinte código:

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Cria um botão com texto "Clique aqui!"
botao = s.CTkButton(janela, text="Clique aqui!")

# Define uma função para ser executada ao clicar no botão
def click_handler():
    print("Botão clicado!")

# Conecta a função click_handler ao evento de clique do botão
botao.command = click_handler

# Posiciona o botão no centro da janela
botao.place(relx=0.5, rely=0.5, anchor='c')

# Inicia o loop principal
janela.mainloop()
```

Este código cria uma janela com um botão no centro exibindo "Clique aqui!". Quando o botão é clicado, a função `click_handler` é executada, imprimindo "Botão clicado!" no console.

### Personalizando o Botão
Você pode personalizar a aparência do `CTkButton` usando vários métodos e atributos:

* **`text`**: Define o texto a ser exibido no botão.
* **`image`**: Define uma imagem para ser exibida no botão.
* **compound`**: Define como o texto e a imagem serão exibidos (LEFT, CENTER, RIGHT, TOP, BOTTOM).
* **`theme`**: Define o tema do botão ("light" ou "dark").
* **`fg_color`**: Define a cor do texto.
* **`bg_color`**: Define a cor de fundo.
* **`font`**: Define a fonte do texto.
* **`width`**: Define a largura do botão.
* **`height`**: Define a altura do botão.
* **`corner_radius`**: Define o arredondamento dos cantos.

Aqui está um exemplo de personalização da aparência:

```python
botao.theme("dark")
botao.fg_color = "white"
botao.bg_color = "#333333"
botao.font = s.CTkFont(size=16, weight="bold")
botao.width = 150
botao.height = 50
botao.corner_radius = 5
```

Este código define o tema como escuro, altera a cor do texto para branco, a cor de fundo para #333333, o tamanho e estilo da fonte, a largura, a altura e o arredondamento dos cantos para 5 pixels.

### Estados do Botão
O `CTkButton` possui diferentes estados que afetam sua aparência:

* **`normal`**: Estado padrão do botão.
* **`pressed`**: Estado quando o botão é pressionado.
* **`disabled`**: Estado quando o botão está desabilitado.
* **`hover`**: Estado quando o cursor do mouse está sobre o botão.

Você pode personalizar a aparência do botão em cada estado usando métodos como:

* **configure(state="disabled")** - Desabilita o botão.
* **configure(fg_color_pressed="red")** - Define a cor do texto quando o botão é pressionado.

## Recursos adicionais
* **Documentação oficial:** [https://github.com/TomSchimansky/CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* **Tutorial:** [https://www.youtube.com/watch?v=30L3pJ73TSY](https://www.youtube.com/watch?v=30L3pJ73TSY)

Ao entender e usar esses recursos, você pode criar botões personalizados e interativos para suas aplicações CustomTkinter.
