# APRENDA A CRIAR TABS (ABAS) NO CUSTOMTKINTER
Para criar tabs (abas) no `customtkinter`, você pode usar o método `tabview()` da classe `CTk()`.

O método `tabview()` cria um novo tabview que é um widget que pode conter múltiplos widgets. Você pode usar tabs para organizar conteúdo em uma interface.

Por exemplo, o seguinte código cria um tabview com duas abas:

```python
import customtkinter as s

def main():
    # Cria a janela principal
    janela = s.CTk()

    # Cria um tabview
    tabview = s.CTkTabview(janela)

    # Adiciona uma aba ao tabview
    aba1 = tabview.add("Aba 1")

    # Adiciona um botão à aba 1
    botao1 = s.CTkButton(aba1, text="Fechar")
    botao1.pack()

    # Adiciona outra aba ao tabview
    aba2 = tabview.add("Aba 2")

    # Adiciona um botão à aba 2
    botao2 = s.CTkButton(aba2, text="Fechar")
    botao2.pack()

    # Inicia o loop de eventos
    janela.mainloop()

if __name__ == "__main__":
    main()
```

Este código criará uma janela principal com um tabview. O tabview terá duas abas, chamadas "Aba 1" e "Aba 2". Cada aba terá um botão com o texto "Fechar".

Você pode usar os métodos e propriedades da classe `CTkTabview()` para configurar a aparência e o comportamento do tabview. Por exemplo, o seguinte código configura o tabview para usar o estilo `primary`:

```python
tabview.theme("primary")
```

Este código fará com que o tabview use o estilo `primary`, que é um estilo moderno com cores brilhantes.

Você também pode adicionar widgets às abas usando os métodos e propriedades da classe `CTkTabview()`. Por exemplo, o seguinte código adiciona um label à aba 1:

```python
label = s.CTkLabel(aba1, text="Este é um label")
label.pack()
```

Este código adicionará um label com o texto "Este é um label" à aba 1.

Você pode combinar esses elementos para criar tabs personalizados com diferentes funcionalidades.

## Exemplo

Aqui está um exemplo de como criar e configurar um tabview:

```python
import customtkinter as s

def main():
    # Cria a janela principal
    janela = s.CTk()

    # Cria um tabview
    tabview = s.CTkTabview(janela)

    # Adiciona uma aba ao tabview
    aba1 = tabview.add("Aba 1")

    # Adiciona um botão à aba 1
    botao1 = s.CTkButton(aba1, text="Fechar")
    botao1.pack()

    # Adiciona outra aba ao tabview
    aba2 = tabview.add("Aba 2")

    # Adiciona um label à aba 2
    label = s.CTkLabel(aba2, text="Este é um label")
    label.pack()

    # Configura o tabview para usar o estilo primary
    tabview.theme("primary")

    # Inicia o loop de eventos
    janela.mainloop()

if __name__ == "__main__":
    main()
```

Este código criará uma janela principal com um tabview. O tabview terá duas abas, chamadas "Aba 1" e "Aba 2". Cada aba terá um botão com o texto "Fechar".

O tabview também usará o estilo `primary`.

Você pode modificar este código para personalizar a aparência e o comportamento do tabview.

Aqui estão algumas coisas que você pode fazer para modificar o código:

* Alterar o título da janela principal.
* Alterar o tamanho da janela principal.
* Alterar o estilo da janela principal.
* Alterar o título da aba 1.
* Alterar o título da aba 2.