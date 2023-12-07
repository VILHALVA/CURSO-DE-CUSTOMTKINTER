# CRIANDO UMA INTERFACE GRAFICA MODERNA EM PYTHON COM 3 LINHAS DE CODIGO
## INTRODUÇÃO:
Sim, é possível criar uma interface gráfica moderna em Python com apenas 3 linhas de código. Para isso, podemos usar o módulo `customtkinter`.

O módulo `customtkinter` é uma biblioteca de terceiros que fornece uma interface gráfica moderna e responsiva para Python. Para instalá-lo, você pode usar o comando `pip`:

```
pip install customtkinter
```

Depois de instalar o módulo, você pode criar uma interface gráfica moderna com apenas 3 linhas de código:

```python
import customtkinter as tk

root = tk.Tk()

# Cria um botão
botao = tk.Button(root, text="Olá, mundo!")

# Exibe a janela
root.mainloop()
```

Este código criará uma janela simples com um botão que diz "Olá, mundo!". O botão será exibido no centro da janela.

Para tornar a interface gráfica mais moderna, podemos adicionar alguns estilos:

```python
import customtkinter as tk

root = tk.Tk()

# Cria um botão
botao = tk.Button(root, text="Olá, mundo!", style="primary")

# Exibe a janela
root.mainloop()
```

Este código usará o estilo `primary` do `customtkinter` para o botão. O estilo `primary` é um estilo moderno e colorido que é usado para destacar elementos importantes.

Aqui estão alguns outros estilos que você pode usar:

* `secondary`: um estilo secundário moderno
* `success`: um estilo de sucesso
* `info`: um estilo de informação
* `warning`: um estilo de aviso
* `danger`: um estilo de perigo

Você pode encontrar mais informações sobre os estilos do `customtkinter` na documentação do módulo.

Com um pouco de criatividade, você pode criar interfaces gráficas modernas e responsivas em Python com apenas algumas linhas de código.

## JANELA:
Criar uma interface gráfica moderna com apenas 3 linhas de código pode ser desafiador, mas é possível usando módulos externos que simplificam o processo. Um desses módulos é o `tkinter.ttk` (themed Tkinter), que fornece widgets temáticos mais modernos. Além disso, bibliotecas externas, como `ttkthemes` ou `tkinter.ttkthemes`, podem ser usadas para estilizar ainda mais a interface gráfica.

Aqui está um exemplo usando `ttkthemes` para criar uma janela com uma barra de progresso:

```python
from tkinter import Tk, ttk
from ttkthemes import ThemedStyle

# Criar uma instância da janela principal
janela = Tk()

# Criar uma barra de progresso
barra_progresso = ttk.Progressbar(janela, mode='indeterminate')
barra_progresso.pack(pady=20)

# Aplicar um tema moderno à janela
style = ThemedStyle(janela)
style.set_theme("arc")  # Pode ser "radiance", "clearlooks", etc.

# Iniciar o loop principal
janela.mainloop()
```

Neste exemplo:

1. Importamos a classe `Tk` e `ttk` do módulo `tkinter` para criar a janela e usar widgets temáticos.
2. Importamos `ttkthemes` para aplicar temas modernos à janela.
3. Criamos uma instância da janela principal (`Tk()`).
4. Criamos uma barra de progresso (`ttk.Progressbar`).
5. Aplicamos um tema moderno à janela usando `ttkthemes`.
6. Iniciamos o loop principal (`janela.mainloop()`).

Certifique-se de instalar o `ttkthemes` antes de executar o código:

```bash
pip install ttkthemes
```

Esse exemplo é bastante simples e focado na estilização moderna usando temas temáticos. Dependendo dos requisitos específicos da sua interface gráfica, você pode precisar de mais linhas de código para adicionar funcionalidades e widgets adicionais.