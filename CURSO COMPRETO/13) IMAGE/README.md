# IMAGE
Para colocar uma imagem no CustomTkinter, você pode usar o widget `CTkImage`. Este widget permite carregar e exibir imagens de vários formatos, como PNG, JPEG e GIF.

Para criar um widget `CTkImage`, você precisa especificar o seguinte:

* O **arquivo da imagem** que você deseja carregar.
* O **pai** do widget, que é a janela na qual o widget será exibido.

Aqui está um exemplo de como criar um widget `CTkImage`:

```python
import customtkinter as s

# Cria a janela
janela = s.CTk()

# Carrega a imagem
imagem = s.CTkImage(file="imagem.png")

# Cria e posiciona o widget
imagem_widget = s.CTkImage(master=janela, image=imagem)
imagem_widget.place(relx=0.5, rely=0.5, anchor="center")

# Inicia o loop principal
janela.mainloop()
```

Este código carrega uma imagem chamada "imagem.png" e a exibe em uma janela centrada na tela.

Você pode personalizar a aparência e o comportamento do widget `CTkImage` usando vários métodos e atributos:

* **`width`**: Define a largura desejada da imagem exibida.
* **`height`**: Define a altura desejada da imagem exibida.
* **`corner_radius`**: Define a redondeza das bordas da imagem.
* **`state`**: Habilita ou desabilita a interação do usuário com a imagem.

Aqui está um exemplo de como personalizar a aparência da imagem:

```python
imagem_widget.width = 300
imagem_widget.height = 200
imagem_widget.corner_radius = 10
```

Este código define a largura da imagem para 300 pixels, a altura para 200 pixels e adiciona bordas arredondadas com raio de 10 pixels.

Você também pode adicionar interatividade ao widget `CTkImage` vinculando eventos a ele. Por exemplo, você pode vincular o evento `<Button-1>` para que a imagem seja clicada.

Aqui está um exemplo de como adicionar interatividade à imagem:

```python
def on_image_click(event):
    print("Imagem clicada!")

imagem_widget.bind("<Button-1>", on_image_click)
```

Este código define uma função `on_image_click` que imprime uma mensagem na console quando a imagem é clicada. A função é então vinculada ao evento `<Button-1>`, que é acionado por um clique esquerdo.

Para obter mais informações sobre como usar o widget `CTkImage`, consulte a documentação oficial do CustomTkinter.