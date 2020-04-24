import argparse
import PyPDF2


def get_args():
    parser = argparse.ArgumentParser(
        description="Adiciona marca d'água em arquivos .pdf")
    parser.add_argument("marca", help="Marca D'água")
    parser.add_argument("arquivo", help="Arquivo .pdf")

    args = parser.parse_args()

    return args.marca, args.arquivo


def adiciona_marca(marca, arquivo):
    template = PyPDF2.PdfFileReader(open(arquivo, "rb"))
    marca_dagua = PyPDF2.PdfFileReader(open(marca, "rb"))
    output = PyPDF2.PdfFileWriter()

    for index in range(template.getNumPages()):
        pagina = template.getPage(index)
        # Este pdf só possui uma página
        pagina.mergePage(marca_dagua.getPage(0))
        output.addPage(pagina)

    with open("pdf_transformado.pdf", "wb") as novo_pdf:
        output.write(novo_pdf)


marca, arquivo = get_args()

adiciona_marca(marca, arquivo)
print("Marca d'água adicionada")
