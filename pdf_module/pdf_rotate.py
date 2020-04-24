import PyPDF2

# Função exercício


def pdf_rotate():
	with open("./pdf_files/dummy_pdf.pdf", "rb") as pdf:
		print(pdf)
		reader = PyPDF2.PdfFileReader(pdf)
		
		page = reader.getPage(0)
		page.rotateCounterClockwise(90)
		
		writer = PyPDF2.PdfFileWriter()
		writer.addPage(page)
		
		with open("tilt.pdf", "wb") as novo_pdf:
			writer.write(novo_pdf)	

pdf_rotate()
