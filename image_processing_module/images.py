from PIL import Image, ImageFilter

img = Image.open("./Pokedex/self.png")

#Comando que muda o dimensões da imagem dentros dos limites passados, mas mantendo seu 'aspect ratio' ou proporção de tela
img.thumbnail((210,210))

#Comando deixa em preto em branco
#filtered_img = img.convert('L')
img.save("exemplo.png", "png")

img.show()