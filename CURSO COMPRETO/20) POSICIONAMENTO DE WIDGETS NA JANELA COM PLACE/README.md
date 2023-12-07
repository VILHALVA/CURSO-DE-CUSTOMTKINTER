# POSICIONAMENTO DE WIDGETS NA JANELA COM (PLACE)
O método `place()` é usado para posicionar widgets na janela. Ele aceita uma série de argumentos que permitem especificar a posição e o tamanho do widget.

Os argumentos mais comuns do método `place()` são:

* **`relx`**: Posição relativa horizontal do widget, como um valor entre 0 e 1.
* **`rely`**: Posição relativa vertical do widget, como um valor entre 0 e 1.
* **`anchor`**: Ponto de ancoragem do widget, como "center", "n", "s", "e", ou "w".
* **`x`**: Posição absoluta horizontal do widget, em pixels.
* **`y`**: Posição absoluta vertical do widget, em pixels.
* **`width`**: Largura do widget, em pixels.
* **`height`**: Altura do widget, em pixels.

Por exemplo, o seguinte código posiciona um widget no centro da janela:

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Cria o widget
widget = s.CTkLabel(master=janela, text="Meu widget")

# Posiciona o widget
widget.place(relx=0.5, rely=0.5, anchor="center")

# Inicia o loop principal
janela.mainloop()
```

Este código cria uma janela e um widget com o texto "Meu widget". O widget é posicionado no centro da janela usando os argumentos `relx` e `rely`.

Outros argumentos do método `place()` permitem especificar o preenchimento do widget, a posição das bordas, e outros atributos.

Para obter mais informações sobre os argumentos do método `place()`, consulte a documentação do CustomTkinter.

Aqui estão alguns exemplos de como usar o método `place()` para posicionar widgets na janela:

* **Posicionar um widget no canto superior esquerdo da janela:**

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Cria o widget
widget = s.CTkLabel(master=janela, text="Meu widget")

# Posiciona o widget
widget.place(x=0, y=0, anchor="nw")

# Inicia o loop principal
janela.mainloop()
```

* **Posicionar um widget com um tamanho fixo:**

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Cria o widget
widget = s.CTkLabel(master=janela, text="Meu widget")

# Posiciona o widget
widget.place(relx=0.5, rely=0.5, anchor="center", width=100, height=50)

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
widget.place(relx=0.5, rely=0.5, anchor="center", padx=10, pady=10)

# Inicia o loop principal
janela.mainloop()
```

O método `place()` é uma ferramenta versátil que pode ser usada para posicionar widgets de forma precisa na janela.