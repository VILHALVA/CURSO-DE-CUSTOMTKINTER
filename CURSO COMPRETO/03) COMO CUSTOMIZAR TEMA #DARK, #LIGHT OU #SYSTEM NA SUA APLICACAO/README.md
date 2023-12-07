# COMO CUSTOMIZAR TEMA #DARK, #LIGHT OU #SYSTEM NA SUA APLICACAO 
Para customizar o tema da sua aplicação usando o `customtkinter`, você pode usar os seguintes métodos e propriedades:

* **`theme()`:** Define o tema da aplicação.
* **`theme_color()`:** Define a cor de fundo do tema.
* **`theme_foreground()`:** Define a cor da fonte do tema.
* **`theme_primary()`:** Define a cor principal do tema.
* **`theme_secondary()`:** Define a cor secundária do tema.

Por exemplo, o seguinte código configura a aplicação para usar o tema `dark` com a cor de fundo preta e a cor da fonte branca:

```python
import customtkinter as s

def main():
    # Cria a janela principal
    janela = s.CTk()

    # Configura o tema
    janela.theme("dark")
    janela.theme_color("black")
    janela.theme_foreground("white")

    # Cria um botão
    botao = s.CTkButton(janela, text="Fechar")
    botao.place(x=0, y=0)

    # Define o callback do botão
    botao.config(command=janela.destroy)

    # Inicia o loop de eventos
    janela.mainloop()

if __name__ == "__main__":
    main()
```

Este código criará uma janela com o tema `dark` e a cor de fundo preta. O botão também terá a cor de fundo preta e a cor da fonte branca.

Você também pode usar os métodos e propriedades de estilo para personalizar a aparência do tema. Por exemplo, o seguinte código configura o tema `dark` para usar uma fonte bold:

```python
import customtkinter as s

def main():
    # Cria a janela principal
    janela = s.CTk()

    # Configura o tema
    janela.theme("dark")
    janela.theme_foreground("white")
    janela.theme_color("black")
    janela.theme_configure(font=("Arial", 10, "bold"))

    # Cria um botão
    botao = s.CTkButton(janela, text="Fechar")
    botao.place(x=0, y=0)

    # Define o callback do botão
    botao.config(command=janela.destroy)

    # Inicia o loop de eventos
    janela.mainloop()

if __name__ == "__main__":
    main()
```

Este código criará uma janela com o tema `dark` e a cor de fundo preta. O botão também terá a cor de fundo preta e a cor da fonte branca em negrito.

Para obter mais informações sobre como customizar o tema da sua aplicação, você pode consultar a documentação do módulo `customtkinter`.

Aqui estão alguns exemplos específicos de como customizar o tema da sua aplicação:

* **Para definir a cor de fundo do tema:**

```python
janela.theme_color("red")
```

* **Para definir a cor da fonte do tema:**

```python
janela.theme_foreground("blue")
```

* **Para definir a cor principal do tema:**

```python
janela.theme_primary("green")
```

* **Para definir a cor secundária do tema:**

```python
janela.theme_secondary("yellow")
```

* **Para definir a fonte do tema:**

```python
janela.theme_configure(font=("Arial", 10, "bold"))
```

Você pode combinar esses métodos e propriedades para customizar o tema da sua aplicação da maneira que desejar.