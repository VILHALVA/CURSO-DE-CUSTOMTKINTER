# APRENDA A CRIAR FRAME E A POSICONALAS NO CUSTOMTKINTER
Para criar um frame no `customtkinter`, você pode usar o método `frame()` da classe `CTk()`.

O método `frame()` cria um novo frame que é um widget de container. Você pode usar frames para organizar outros widgets em sua interface.

Por exemplo, o seguinte código cria um frame:

```python
import customtkinter as s

def main():
    # Cria a janela principal
    janela = s.CTk()

    # Cria um frame
    frame = s.CTkFrame(janela)

    # Inicia o loop de eventos
    janela.mainloop()

if __name__ == "__main__":
    main()
```

Este código criará uma janela principal com um frame. O frame será posicionado no centro da janela.

Você pode usar os métodos e propriedades da classe `CTkFrame()` para configurar a aparência e o comportamento do frame. Por exemplo, o seguinte código configura o frame para usar o estilo `primary`:

```python
frame.theme("primary")
```

Este código fará com que o frame use o estilo `primary`, que é um estilo moderno com cores brilhantes.

Você também pode adicionar widgets ao frame usando os métodos e propriedades da classe `CTkFrame()`. Por exemplo, o seguinte código adiciona um botão ao frame:

```python
botao = s.CTkButton(frame, text="Fechar")
botao.pack()
```

Este código adicionará um botão com o texto "Fechar" ao frame. O botão será posicionado no centro do frame.

Você pode combinar esses elementos para criar frames personalizados com diferentes funcionalidades.

## Posicionando frames

Para posicionar um frame, você pode usar os métodos e propriedades da classe `CTkFrame()`.

Os métodos e propriedades mais comuns para posicionar frames são:

* `place()`:** Posiciona o frame em uma posição específica.
* `pack()`:** Posiciona o frame no centro da janela.
* `grid()`:** Posiciona o frame em uma grade.

Por exemplo, o seguinte código posiciona um frame no canto superior esquerdo da janela:

```python
frame.place(x=0, y=0)
```

Este código posiciona o frame no canto superior esquerdo da janela, com a coordenada x igual a 0 e a coordenada y igual a 0.

O seguinte código posiciona um frame no centro da janela:

```python
frame.pack()
```

Este código posiciona o frame no centro da janela.

O seguinte código posiciona um frame em uma grade:

```python
frame.grid(row=0, column=0)
```

Este código posiciona o frame na primeira linha e na primeira coluna da grade.

Você pode combinar esses métodos e propriedades para posicionar frames da maneira que desejar.

## Exemplo

Aqui está um exemplo de como criar e posicionar um frame:

```python
import customtkinter as s

def main():
    # Cria a janela principal
    janela = s.CTk()

    # Cria um frame
    frame = s.CTkFrame(janela)

    # Posiciona o frame no canto superior esquerdo
    frame.place(x=0, y=0)

    # Adiciona um botão ao frame
    botao = s.CTkButton(frame, text="Fechar")
    botao.pack()

    # Inicia o loop de eventos
    janela.mainloop()

if __name__ == "__main__":
    main()
```

Este código criará uma janela principal com um frame. O frame será posicionado no canto superior esquerdo da janela. O frame também terá um botão com o texto "Fechar" que está posicionado no centro do frame.

Você pode modificar este código para personalizar a aparência e o comportamento do frame.

Aqui estão algumas coisas que você pode fazer para modificar o código:

* Alterar o título da janela principal.
* Alterar o tamanho da janela principal.
* Alterar o estilo da janela principal.
* Alterar a posição do frame.
* Alterar o tamanho do frame.
* Alterar o estilo do frame.
* Adicionar mais widgets ao frame.

Você pode combinar esses elementos para criar frames personalizados com diferentes funcionalidades.