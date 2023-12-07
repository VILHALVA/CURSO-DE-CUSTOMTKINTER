# OPTIONMENU
`CTkOptionMenu` é um widget do `customtkinter` que permite que os usuários selecionem uma única opção de uma lista de opções. É semelhante ao widget `OptionMenu` do Tkinter, mas tem uma aparência mais moderna e personalizável.

Aqui estão algumas características principais do `CTkOptionMenu`:

* **Menu suspenso:** Exibe uma lista de opções ao ser clicado.
* **Personalização:** Permite alterar a aparência do menu por meio de temas, cores e fontes.
* **Seleção de valor:** Fornece acesso ao valor selecionado atualmente.

### Criando um Menu de Opções

Aqui está como criar um `CTkOptionMenu` básico:

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Cria uma lista de opções
opções = ["Opção 1", "Opção 2", "Opção 3"]

# Cria o Menu de Opções
menu_de_opções = s.CTkOptionMenu(janela, values=opções)
menu_de_opções.pack()

# Inicia o loop principal
janela.mainloop()
```

Este código cria uma janela com uma lista de opções e as exibe em um menu suspenso. A opção selecionada atualmente está disponível por meio do método `menu_de_opções.get()`.

### Personalizando o Menu de Opções

Você pode personalizar a aparência do `CTkOptionMenu` usando vários métodos e atributos:

* **`theme`**: Define o tema do menu ("light" ou "dark").
* **`fg_color`**: Define a cor do primeiro plano (cor do texto).
* **`bg_color`**: Define a cor de fundo.
* **`font`**: Define a fonte do texto.
* **`border_width`**: Define a largura da borda.
* **`corner_radius`**: Define a arredondamento dos cantos.

Aqui está um exemplo de personalização da aparência:

```python
menu_de_opções.theme("dark")
menu_de_opções.fg_color = "white"
menu_de_opções.bg_color = "#333333"
menu_de_opções.font = s.CTkFont(size=12)
menu_de_opções.border_width = 2
menu_de_opções.corner_radius = 5
```

Este código define o tema como escuro, altera a cor do texto para branco, a cor de fundo para #333333, o tamanho da fonte para 12, a largura da borda para 2 pixels e o raio dos cantos para 5 pixels.

### Conectando a Eventos

Você pode conectar a eventos como alterações de seleção usando o atributo `command`:

```python
def on_opcao_alterada(opcao):
    print(f"Opção selecionada: {opcao}")

menu_de_opções.command = on_opcao_alterada
```

Este código define uma função chamada `on_opcao_alterada` que imprime a opção selecionada. Em seguida, vincula essa função ao atributo `command` do `CTkOptionMenu`.

### Recursos adicionais

* Você pode acessar o valor selecionado atualmente usando o método `get()`.
* Você pode definir o valor selecionado inicialmente usando o método `set()`.
* Você pode desabilitar o menu usando o atributo `state`.

Aqui estão alguns recursos para aprender mais sobre `CTkOptionMenu`:

* **Documentação oficial:** [https://github.com/TomSchimansky/CustomTkinter/wiki](https://github.com/TomSchimansky/CustomTkinter/wiki): [https://github.com/TomSchimansky/CustomTkinter/wiki](https://github.com/TomSchimansky/CustomTkinter/wiki)
* **Código de exemplo:** [https://m.youtube.com/watch?v=wq3I-6DDVPo](https://m.youtube.com/watch?v=wq3I-6DDVPo): [https://m.youtube.com/watch?v=wq3I-6DDVPo](https://m.youtube.com/watch?v=wq3I-6DDVPo)

Ao entender e usar esses recursos, você pode criar menus de opções personalizados e interativos para seus aplicativos customtkinter.