# MANUAL
## 1. INSTALAÇÃO:
### A. INSTALAR PYTHON:
Se você ainda não tem o Python instalado, baixe e instale a versão mais recente do [site oficial do Python](https://www.python.org/downloads/).

### B. INSTALAR `CUSTOMTKINTER`:
Você pode instalar a biblioteca `customtkinter` usando `pip`, o gerenciador de pacotes do Python. Abra seu terminal ou prompt de comando e execute:

```sh
pip install customtkinter
```

## 2. CONFIGURAÇÃO:
### A. CRIAR UM AMBIENTE VIRTUAL (OPCIONAL):
É uma boa prática criar um ambiente virtual para gerenciar as dependências do seu projeto. No terminal, navegue até a pasta do seu projeto e execute:

```sh
python -m venv venv
```

Para ativar o ambiente virtual:
- **Windows**:
  ```sh
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```sh
  source venv/bin/activate
  ```

### B. INSTALAR `CUSTOMTKINTER` NO AMBIENTE VIRTUAL:
Após ativar o ambiente virtual, instale `customtkinter`:

```sh
pip install customtkinter
```

## 3. PRIMEIRO PROJETO:
Vamos criar um projeto simples para entender os conceitos básicos de `customtkinter`.

### A. ESTRUTURA DO PROJETO:
Crie uma pasta para o seu projeto e dentro dela, crie um arquivo Python, por exemplo, `app.py`.

### B. CÓDIGO DO PROJETO:
Abra o `app.py` e adicione o seguinte código:

```python
import customtkinter as ctk

# Criar a janela principal
janela = ctk.CTk()
janela.title("Meu Primeiro App com CustomTkinter")
janela.geometry("700x400")
janela.maxsize(width=900, height=600)
janela.minsize(width=500, height=250)
janela.resizable(width=False, height=False)

# Definir o tema inicial
janela._set_appearance_mode("system")  # "light", "dark" ou "system"

# Função para alternar entre temas
def alternar_tema():
    current_mode = ctk.get_appearance_mode()
    if current_mode == "Light":
        ctk.set_appearance_mode("dark")
    elif current_mode == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("light")

# Adicionar um botão para alternar o tema
botao_tema = ctk.CTkButton(janela, text="Alternar Tema", command=alternar_tema)
botao_tema.pack(pady=20)

# Adicionar um rótulo
rotulo = ctk.CTkLabel(janela, text="Olá, CustomTkinter!", font=("Arial", 24))
rotulo.pack(pady=20)

# Iniciar o loop principal da aplicação
janela.mainloop()
```

## 4. EXECUTANDO O PROJETO:
Para executar seu projeto, certifique-se de que o ambiente virtual está ativado (se você estiver usando um) e execute:

```sh
python app.py
```

Isso abrirá uma janela com um botão que permite alternar entre os temas "light" e "dark", e um rótulo exibindo uma mensagem de boas-vindas.

## EXPLICAÇÃO DO CÓDIGO:
- **Importação**:
  ```python
  import customtkinter as ctk
  ```
  Importa a biblioteca `customtkinter`.

- **Janela Principal**:
  ```python
  janela = ctk.CTk()
  ```
  Cria a janela principal da aplicação.

- **Configuração da Janela**:
  ```python
  janela.title("Meu Primeiro App com CustomTkinter")
  janela.geometry("700x400")
  janela.maxsize(width=900, height=600)
  janela.minsize(width=500, height=250)
  janela.resizable(width=False, height=False)
  ```
  Define título, tamanho inicial, tamanho máximo, tamanho mínimo e se a janela pode ser redimensionada.

- **Tema da Janela**:
  ```python
  janela._set_appearance_mode("system")
  ```
  Define o tema inicial da aplicação.

- **Função de Alternância de Tema**:
  ```python
  def alternar_tema():
      current_mode = ctk.get_appearance_mode()
      if current_mode == "Light":
          ctk.set_appearance_mode("dark")
      elif current_mode == "Dark":
          ctk.set_appearance_mode("light")
      else:
          ctk.set_appearance_mode("light")
  ```
  Função que alterna entre os modos "light" e "dark".

- **Botão para Alternar Tema**:
  ```python
  botao_tema = ctk.CTkButton(janela, text="Alternar Tema", command=alternar_tema)
  botao_tema.pack(pady=20)
  ```
  Cria um botão que chama a função `alternar_tema` quando clicado.

- **Rótulo**:
  ```python
  rotulo = ctk.CTkLabel(janela, text="Olá, CustomTkinter!", font=("Arial", 24))
  rotulo.pack(pady=20)
  ```
  Adiciona um rótulo com texto personalizado.

- **Loop Principal**:
  ```python
  janela.mainloop()
  ```
  Inicia o loop principal da aplicação, mantendo a janela aberta e esperando por interações do usuário.

Pronto! Você criou seu primeiro aplicativo usando `customtkinter`. Agora você pode experimentar adicionar mais widgets e funcionalidades à sua aplicação.