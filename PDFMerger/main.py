from PyPDF2 import PdfWriter

merger = PdfWriter()
pdfs = []

n = int(input("Enter the number of PDF files to merge: \n"))

for i in range(0, n):
    pdf = input(f"Enter the name of PDF file {i + 1}: \n")
    pdfs.append(pdf)

for pdf in pdfs:
    merger.append(pdf)
    
merger.write("merged-pdf.pdf")
merger.close()
