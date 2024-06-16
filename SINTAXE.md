# SINTAXE:
## 1. LABELS:
Os labels são usados para exibir texto estático na interface.

### CÓDIGO:
```python
import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("400x200")

# Adicionar um label
label = ctk.CTkLabel(janela, text="Este é um Label", font=("Arial", 18))
label.pack(pady=20)

janela.mainloop()
```

### EXPLICAÇÃO:
- `ctk.CTkLabel`: Cria um label.
- `text`: Define o texto exibido pelo label.
- `font`: Define a fonte e o tamanho do texto.

## 2. BOTÕES:
Os botões permitem ao usuário executar ações quando clicados.

### CÓDIGO:
```python
import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("400x200")

# Função que será chamada quando o botão for clicado
def on_click():
    print("Botão clicado!")

# Adicionar um botão
button = ctk.CTkButton(janela, text="Clique Aqui", command=on_click)
button.pack(pady=20)

janela.mainloop()
```

### EXPLICAÇÃO:
- `ctk.CTkButton`: Cria um botão.
- `text`: Define o texto exibido no botão.
- `command`: Define a função que será chamada quando o botão for clicado.

## 3. CAIXAS DE ENTRADA DE TEXTO (ENTRY):
As caixas de entrada de texto permitem ao usuário inserir texto.

### CÓDIGO:
```python
import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("400x200")

# Adicionar uma caixa de entrada de texto
entry = ctk.CTkEntry(janela, placeholder_text="Digite algo aqui")
entry.pack(pady=20)

# Função que será chamada quando o botão for clicado
def get_text():
    texto = entry.get()
    print(f"Você digitou: {texto}")

# Adicionar um botão para capturar o texto
button = ctk.CTkButton(janela, text="Enviar", command=get_text)
button.pack(pady=20)

janela.mainloop()
```

### EXPLICAÇÃO:
- `ctk.CTkEntry`: Cria uma caixa de entrada de texto.
- `placeholder_text`: Define o texto de espaço reservado que aparece na caixa de entrada.

## 4. CAIXAS DE SELEÇÃO (CHECKBUTTONS):
As caixas de seleção permitem ao usuário selecionar ou desmarcar opções.

### CÓDIGO:
```python
import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("400x200")

# Variável para armazenar o estado da caixa de seleção
check_var = ctk.StringVar(value="unchecked")

# Adicionar uma caixa de seleção
checkbox = ctk.CTkCheckBox(janela, text="Aceito os termos e condições", variable=check_var, onvalue="checked", offvalue="unchecked")
checkbox.pack(pady=20)

# Função que será chamada quando o botão for clicado
def check_status():
    status = check_var.get()
    print(f"Checkbox está: {status}")

# Adicionar um botão para verificar o estado da caixa de seleção
button = ctk.CTkButton(janela, text="Verificar", command=check_status)
button.pack(pady=20)

janela.mainloop()
```

### EXPLICAÇÃO:
- `ctk.CTkCheckBox`: Cria uma caixa de seleção.
- `variable`: Define a variável que armazena o estado da caixa de seleção.
- `onvalue`: Define o valor quando a caixa de seleção está marcada.
- `offvalue`: Define o valor quando a caixa de seleção está desmarcada.

## 5. RADIO BUTTONS:
Os radio buttons permitem ao usuário selecionar apenas uma opção de um grupo de opções.

### CÓDIGO:
```python
import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("400x200")

# Variável para armazenar o estado do radio button
radio_var = ctk.StringVar(value="")

# Adicionar radio buttons
radio1 = ctk.CTkRadioButton(janela, text="Opção 1", variable=radio_var, value="Opção 1")
radio1.pack(pady=5)
radio2 = ctk.CTkRadioButton(janela, text="Opção 2", variable=radio_var, value="Opção 2")
radio2.pack(pady=5)

# Função que será chamada quando o botão for clicado
def check_selection():
    selecao = radio_var.get()
    print(f"Você selecionou: {selecao}")

# Adicionar um botão para verificar a seleção do radio button
button = ctk.CTkButton(janela, text="Verificar Seleção", command=check_selection)
button.pack(pady=20)

janela.mainloop()
```

### EXPLICAÇÃO:
- `ctk.CTkRadioButton`: Cria um radio button.
- `variable`: Define a variável que armazena o estado do radio button.
- `value`: Define o valor associado a cada radio button.

## 6. SLIDERS:
Os sliders permitem ao usuário selecionar um valor de um intervalo.

### CÓDIGO:
```python
import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("400x200")

# Função que será chamada quando o valor do slider mudar
def slider_changed(value):
    print(f"Valor do slider: {value}")

# Adicionar um slider
slider = ctk.CTkSlider(janela, from_=0, to=100, command=slider_changed)
slider.pack(pady=20)

janela.mainloop()
```

### EXPLICAÇÃO:
- `ctk.CTkSlider`: Cria um slider.
- `from_`: Define o valor mínimo do slider.
- `to`: Define o valor máximo do slider.
- `command`: Define a função que será chamada quando o valor do slider mudar.

## 7. COMBOBOXES:
As comboboxes permitem ao usuário selecionar um valor de uma lista suspensa.

### CÓDIGO:
```python
import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("400x200")

# Lista de opções
opcoes = ["Opção 1", "Opção 2", "Opção 3"]

# Adicionar uma combobox
combobox = ctk.CTkComboBox(janela, values=opcoes)
combobox.pack(pady=20)

# Função que será chamada quando o botão for clicado
def get_selection():
    selecao = combobox.get()
    print(f"Você selecionou: {selecao}")

# Adicionar um botão para verificar a seleção da combobox
button = ctk.CTkButton(janela, text="Verificar Seleção", command=get_selection)
button.pack(pady=20)

janela.mainloop()
```

### EXPLICAÇÃO:
- `ctk.CTkComboBox`: Cria uma combobox.
- `values`: Define a lista de opções da combobox.

## 8. FRAMES:
Os frames são usados para agrupar outros widgets.

### CÓDIGO:
```python
import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("400x300")

# Adicionar um frame
frame = ctk.CTkFrame(janela)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Adicionar widgets ao frame
label = ctk.CTkLabel(frame, text="Label no Frame")
label.pack(pady=10)
button = ctk.CTkButton(frame, text="Botão no Frame")
button.pack(pady=10)

janela.mainloop()
```

### EXPLICAÇÃO:
- `ctk.CTkFrame`: Cria um frame.
- Widgets adicionados ao frame são posicionados dentro dele.

Esses são os componentes básicos do `customtkinter`. Você pode usá-los para criar interfaces gráficas mais complexas e interativas em suas aplicações.