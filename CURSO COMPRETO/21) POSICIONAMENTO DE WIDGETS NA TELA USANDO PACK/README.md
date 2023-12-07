# POSICIONAMENTO DE WIDGETS NA TELA USANDO PACK
O método `pack()` é usado para posicionar widgets na janela usando um layout gerenciador. O layout gerenciador `pack()` é o mais simples dos três layout gerenciadores disponíveis no CustomTkinter. Ele permite posicionar widgets na tela usando uma série de argumentos.

Os argumentos mais comuns do método `pack()` são:

* **`side`**: Posição do widget na tela, como "top", "bottom", "left", ou "right".
* **`fill`**: Modo de preenchimento do widget, como "none", "x", "y", ou "both".
* **`expand`**: Indica se o widget deve ser expandido para preencher o espaço disponível, como "true" ou "false".
* **`anchor`**: Ponto de ancoragem do widget, como "center", "n", "s", "e", ou "w".
* **`ipadx`**: Largura do preenchimento interno horizontal do widget, em pixels.
* **`ipady`**: Altura do preenchimento interno vertical do widget, em pixels.

Por exemplo, o seguinte código posiciona um widget no topo da janela:

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Cria o widget
widget = s.CTkLabel(master=janela, text="Meu widget")

# Posiciona o widget
widget.pack(side="top")

# Inicia o loop principal
janela.mainloop()
```

Este código cria uma janela e um widget com o texto "Meu widget". O widget é posicionado no topo da janela usando o argumento `side`.

Outros argumentos do método `pack()` permitem especificar o espaçamento entre widgets, o alinhamento dos widgets, e outros atributos.

Para obter mais informações sobre os argumentos do método `pack()`, consulte a documentação do CustomTkinter.

Aqui estão alguns exemplos de como usar o método `pack()` para posicionar widgets na tela:

* **Posicionar um widget no centro da janela:**

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Cria o widget
widget = s.CTkLabel(master=janela, text="Meu widget")

# Posiciona o widget
widget.pack(side="center")

# Inicia o loop principal
janela.mainloop()
```

* **Posicionar um widget com preenchimento:**

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Cria o widget
widget = s.CTkLabel(master=janela, text="Meu widget")

# Posiciona o widget
widget.pack(side="top", fill="x", expand=True, ipadx=10, ipady=10)

# Inicia o loop principal
janela.mainloop()
```

* **Posicionar dois widgets um ao lado do outro:**

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Cria o primeiro widget
widget1 = s.CTkLabel(master=janela, text="Widget 1")

# Cria o segundo widget
widget2 = s.CTkLabel(master=janela, text="Widget 2")

# Posiciona os widgets
widget1.pack(side="left")
widget2.pack(side="right")

# Inicia o loop principal
janela.mainloop()
```

O método `pack()` é uma ferramenta simples que pode ser usada para posicionar widgets de forma rápida e fácil na tela.