from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
import csv

my_file = "/home/unni/python/reportlab/alphabets.csv"

def get_file(my_file):
	data = csv.reader(open(my_file, "rb"))
	pdf_name = '/home/unni/python/reportlab/Flash7.pdf'
	c = canvas.Canvas(pdf_name, pagesize=letter)
	#h = next(data)
	i = 0
	result =""
	for row in data:
		front = row[0]
		back = row[1]
		#result1,result2 = row[0:1]
		print front
		print back
		
		
		#gen_pdf(front, back, pdf_file)
		i+=1
#def gen_pdf(front, back, pdf_file):
		#result = front+'   '+back + '\n'
		#c = canvas.Canvas(pdf_name, pagesize=letter)
		c.setFont('Helvetica', 12, leading=None)
		result = front+'   '+back
	        c.drawString(250, 800-i*31.5, result)
	c.showPage()
	c.save()
	c = canvas.Canvas(pdf_name, pagesize = letter)
get_file(my_file)

	
	
