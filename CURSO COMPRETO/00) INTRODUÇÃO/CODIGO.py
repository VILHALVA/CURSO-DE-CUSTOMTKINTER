import customtkinter as tk
from customtkinter import Frame

class Calculadora(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        # Define o layout da janela
        self.grid()
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)

        # Cria os widgets
        self.display = tk.Label(self, text="0")
        self.botao_soma = tk.Button(self, text="+")
        self.botao_subtracao = tk.Button(self, text="-")
        self.botao_multiplicacao = tk.Button(self, text="*")
        self.botao_divisao = tk.Button(self, text="/")

        # Adiciona os widgets à janela
        self.display.grid(row=0, column=0, sticky="nsew")
        self.botao_soma.grid(row=1, column=0, sticky="nsew")
        self.botao_subtracao.grid(row=2, column=0, sticky="nsew")
        self.botao_multiplicacao.grid(row=3, column=0, sticky="nsew")
        self.botao_divisao.grid(row=4, column=0, sticky="nsew")

        # Define os callbacks dos botões
        self.botao_soma.config(command=self.somar)
        self.botao_subtracao.config(command=self.subtrair)
        self.botao_multiplicacao.config(command=self.multiplicar)
        self.botao_divisao.config(command=self.dividir)

    def somar(self):
        # Obtém os números da exibição
        primeiro_numero = float(self.display.cget("text"))
        segundo_numero = float(input("Informe o segundo número: "))

        # Realiza a soma
        resultado = primeiro_numero + segundo_numero

        # Atualiza a exibição
        self.display.configure(text=str(resultado))

    def subtrair(self):
        # Obtém os números da exibição
        primeiro_numero = float(self.display.cget("text"))
        segundo_numero = float(input("Informe o segundo número: "))

        # Realiza a subtração
        resultado = primeiro_numero - segundo_numero

        # Atualiza a exibição
        self.display.configure(text=str(resultado))

    def multiplicar(self):
        # Obtém os números da exibição
        primeiro_numero = float(self.display.cget("text"))
        segundo_numero = float(input("Informe o segundo número: "))

        # Realiza a multiplicação
        resultado = primeiro_numero * segundo_numero

        # Atualiza a exibição
        self.display.configure(text=str(resultado))

    def dividir(self):
        # Obtém os números da exibição
        primeiro_numero = float(self.display.cget("text"))
        segundo_numero = float(input("Informe o segundo número: "))

        # Realiza a divisão
        resultado = primeiro_numero / segundo_numero

        # Atualiza a exibição
        self.display.configure(text=str(resultado))

# Cria a janela principal
root = tk.Tk()

# Cria a calculadora
calculadora = Calculadora(root)

# Inicia o loop da GUI
root.mainloop()
