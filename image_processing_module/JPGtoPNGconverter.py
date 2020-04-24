import argparse
import os
from PIL import Image
import glob
import re


parser = argparse.ArgumentParser(
    description="Converte imagens .jpg para .png, script feito considerando o PATH do OS Windows", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("source_dir", help="Diretório fonte")

# nargs='?' permite um argumento posicional ser opcional
parser.add_argument("destination_dir", nargs='?',
                    default="./pasta_pngs", help="Diretório destino, caso não especificado os arquivos serão salvos em uma nova pasta")

ajuda_mode = ("Seleciona o modo de tipo e profundidade dos pixels da imagem, modos:\n"
              "-> 1 (1-bit pixels, black and white, stored with one pixel per byte)\n"
              "-> L (8-bit pixels, black and white)\n"
              "-> P (8-bit pixels, mapped to any other mode using a color palette)\n"
              "-> RGB (3x8-bit pixels, true color)\n"
              "-> RGBA (4x8-bit pixels, true color with transparency mask)\n"
              "-> I (32-bit signed integer pixels)\n")

choices_mode = ['1', 'L', 'P', 'RGB', 'RGBA', 'I']

parser.add_argument("-m", "--mode", default="RGB",
                    choices=choices_mode, help=ajuda_mode)

args = parser.parse_args()

destination_dir = os.path.join(args.destination_dir)
if not os.path.exists(destination_dir):
    os.mkdir(destination_dir)

arquivos_png_achados = glob.glob(rf"{args.source_dir}/*.jpg")

if len(arquivos_png_achados) is 0:
    raise Exception("Diretório fonte não existe")


def get_nome_path(path):
	regex_pattern = re.compile(r"\\(?:.(?!\\))+$")
	nome = regex_pattern.search(path).group()
	return f"{nome[:-4]}.png"


def transforma_e_salva_image(img):
    img_aberta = Image.open(imagem)
    img_filtrada = img_aberta.convert(args.mode)
    img_filtrada.save(f"./{destination_dir}/{get_nome_path(img)}", "png")

for imagem in arquivos_png_achados:
    transforma_e_salva_image(imagem)

print(f"Arquivos convertidos com sucesso no diretório -> {destination_dir}")
