# COMO CONFIGURAR A JANELA DA SUA APLICACAO COMO DESEJAS
Para configurar a janela da sua aplicação como desejas, você pode usar os seguintes métodos e propriedades:

* **`title()`:** Define o título da janela.
* **`geometry()`:** Define o tamanho e a posição da janela.
* **`icon()`:** Define o ícone da janela.
* **`background()`:** Define a cor de fundo da janela.
* **`foreground()`:** Define a cor da fonte da janela.
* **`style()`:** Define o estilo da janela.

Por exemplo, o seguinte código configura a janela para ter o título "Minha aplicação", o tamanho de 800x600 pixels, o ícone do arquivo `my_icon.ico`, a cor de fundo azul e a cor da fonte branca:

```python
import customtkinter as s

janela = s.CTk()

janela.title("Minha aplicação")
janela.geometry("800x600")
janela.icon("my_icon.ico")
janela.background("blue")
janela.foreground("white")

janela.mainloop()
```

Você também pode usar os métodos e propriedades de estilo para personalizar a aparência da janela. Por exemplo, o seguinte código configura a janela para usar o estilo `primary`:

```python
import customtkinter as s

janela = s.CTk()

janela.configure(style="primary")

janela.mainloop()
```

Para obter mais informações sobre como configurar a janela da sua aplicação, você pode consultar a documentação do módulo `customtkinter`.

Aqui estão alguns exemplos específicos de como configurar a janela da sua aplicação:

* **Para centralizar a janela na tela:**

```python
janela.geometry("+0+0")
```

* **Para definir a janela para ser redimensionável:**

```python
janela.resizable(True, True)
```

* **Para definir a janela para ser minimizada:**

```python
janela.minsize(200, 100)
```

* **Para definir a janela para ser maximizada:**

```python
janela.maxsize(1000, 800)
```

* **Para definir a janela para ser fechada ao pressionar a tecla `Esc`:**

```python
janela.protocol("WM_DELETE_WINDOW", lambda: sys.exit(0))
```

Você pode combinar esses métodos e propriedades para configurar a janela da sua aplicação da maneira que desejar.