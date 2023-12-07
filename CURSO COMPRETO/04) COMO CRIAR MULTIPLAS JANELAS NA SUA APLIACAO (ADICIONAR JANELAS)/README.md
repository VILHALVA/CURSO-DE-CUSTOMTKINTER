# COMO CRIAR MULTIPLAS JANELAS NA SUA APLIACAO (ADICIONAR JANELAS)
Para criar múltiplas janelas em sua aplicação usando o `customtkinter`, você pode usar o método `toplevel()` da classe `CTk()`.

O método `toplevel()` cria uma nova janela que é independente da janela principal. Você pode usar essa janela para criar uma nova interface ou para adicionar mais funcionalidades à aplicação.

Por exemplo, o seguinte código cria duas janelas:

```python
import customtkinter as s

def main():
    # Cria a janela principal
    janela = s.CTk()

    # Cria uma nova janela
    janela2 = janela.toplevel()

    # Configura a janela
    janela2.title("Janela 2")
    janela2.geometry("300x200")

    # Inicia o loop de eventos
    janela.mainloop()

if __name__ == "__main__":
    main()
```

Este código criará uma janela principal com o título "Janela principal". A segunda janela terá o título "Janela 2" e terá o tamanho de 300x200 pixels.

Você pode usar os métodos e propriedades da classe `CTk()` para configurar a aparência e o comportamento da janela. Por exemplo, o seguinte código configura a segunda janela para usar o estilo `primary`:

```python
janela2.theme("primary")
```

Este código fará com que a segunda janela use o estilo `primary`, que é um estilo moderno com cores brilhantes.

Você também pode adicionar widgets à janela usando os métodos e propriedades da classe `CTk()`. Por exemplo, o seguinte código adiciona um botão à segunda janela:

```python
botao = s.CTkButton(janela2, text="Fechar")
botao.pack()
```

Este código adicionará um botão com o texto "Fechar" à segunda janela. O botão será posicionado no centro da janela.

Você pode combinar esses elementos para criar múltiplas janelas personalizadas com diferentes funcionalidades.