# Coursera, Google IT Automation with Python
# Course 6, Automating Real-World Tasks with Python
# Week 4, FINAL PROJECT, Part 4 of 5

import os
import emails
from datetime import datetime
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def main():
	source_dir = 'supplier-data/descriptions'
	pdf_path = '/tmp/processed.pdf'
	pdf_title = 'Process Updated on ' + datetime.now().strftime('%B %d, %Y')
	pdf_body = ''

	# Generate the body of the report
	os.chdir(source_dir)	# making life easy
	for filename in os.listdir():
		if filename.endswith('.txt'):
			pdf_body += create_body(filename)
	
	# Make the PDF report and save to disk
	create_pdf(pdf_path, pdf_title, pdf_body)
	
	# Define parameters to be used to generate the email
	email_params = {
		'from'    : 'automation@example.com',
		'to'      : f"{os.environ['USER']}@example.com",
		'subject' : 'Upload Completed - Online Fruit Store',
		'content' : 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
	}

	# Generate and send the email with the the report as attachment
	message = emails.create_email(params=email_params, attachment=pdf_path)
	emails.send_email(message)


def create_body(filename):
	"""Reads fruit name and weight from text file
	and returns them as a formatted string"""

	with open(filename, 'r') as file:
		text = [line.strip() for line in file]
	return f"name: {text[0]}<br/>weight: {text[1]}<br/><br/>"


def create_pdf(pdf_path, pdf_title, pdf_body):
	"""Generates the PDF report using given
	parameters and saves to disk"""

	styles = getSampleStyleSheet()
	report = SimpleDocTemplate(pdf_path)
	report_title = Paragraph(text=pdf_title, style=styles['h1'])
	report_body = Paragraph(text=pdf_body, style=styles['BodyText'])
	report.build([report_title, Spacer(1,15), report_body])


if __name__ == '__main__':
	main()