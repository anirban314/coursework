# Coursera, Google IT Automation with Python
# Course 6, Automating Real-World Tasks with Python
# Week 3, Automatic Output Generation

import os
import json
import mimetypes
import smtplib
from email.message import EmailMessage
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Spacer

def main():
	json_path = 'files/car_sales.json'
	report_path = 'files/car_sales.pdf'

	title = 'Sales Summary for Last Month'
	table = create_table(json_path)
	summary = create_summary(table)
	create_pdf(report_path, title, summary, table)
	
	email_details = {
		'server'	: '<address of SMTP server>',
		'username'	: '<user account to use to send the mail>',
		'password'	: '<password to use to log in to the account>',
		'to'		: '<email address of the recipient>',
		'subject'	: '<subject line goes here>',
		'content'	: '<message body goes here>'
	}
	message = create_email_message(report_path, email_details)
	send_email_message(message, email_details)

def create_table(path):
	#Define local functions
	def format_car(car):
		return f"{car['car_make']} {car['car_model']} ({car['car_year']})"
	def format_price(price):
		return float(price[1:])
	
	#Load JSON file from disk
	with open(path, 'r') as file:
		car_json = json.load(file)

	#Convert JSON to list of lists
	table = []
	for item in car_json:
		item_description = format_car(item['car'])
		item_price = format_price(item['price'])
		item_revenue = round(item_price * item['total_sales'], 2)
		table.append([
			item['id'],
			item_description,
			item_price,
			item['total_sales'],
			item_revenue
		])
	return table

def create_summary(table):
	#Calculate most popular year
	year = {}
	for car in table:  #car[0]=ID, car[1]=Make Model (Year), car[2]=Price, car[3]=Total_Sales, car[4]=Revenue
		car_year = car[1].split()[2][1:5]  #The notation [1:5] removes the brackets around the year
		year[car_year] = year.get(car_year,0) + car[3]
	
	max_sales = sorted(table, key=lambda val: val[3], reverse=True)[0]  #table[3]=Total_Sales
	max_revenue = sorted(table, key=lambda val: val[4], reverse=True)[0]  #table[4]=Revenue
	pop_car_year = sorted(year.items(), key=lambda val: val[1], reverse=True)[0]

	return f"""\
		The {max_sales[1]} had the most sales: {max_sales[3]}. \
		The {max_revenue[1]} generated the most revenue: ${max_revenue[4]}. \
		The most popular year was {pop_car_year[0]} with {pop_car_year[1]} sales."""

def create_pdf(path, title, summary, table):
	report = SimpleDocTemplate(path)
	title_style = getSampleStyleSheet()
	table_style = [('GRID', (0,1), (-1,-1), 0.25, colors.gray)]

	#Add header
	table.insert(0, ['ID', 'Car Description', 'Price per Unit', 'Units Sold', 'Revenue Generated'])

	report_title = Paragraph(text=title, style=title_style['h1'])
	report_summary = Paragraph(text=summary, style=title_style['h6'])
	report_table = Table(data=table, style=table_style, hAlign='LEFT')
	
	report.build([report_title, Spacer(1,5), report_summary, Spacer(1,15), report_table])

def create_email_message(attachment, email_details):
	message = EmailMessage()
	message['from'] = email_details['username']
	message['to'] = email_details['to']
	message['subject'] = email_details['subject']
	message.set_content(email_details['content'])

	mime_type = mimetypes.guess_type(attachment)[0]
	mime_type, mime_subtype = mime_type.split('/')
	with open(attachment, 'rb') as file:
		message.add_attachment(
			file.read(),
			maintype=mime_type,
			subtype=mime_subtype,
			filename=os.path.basename(attachment))
	return message

def send_email_message(message, email_details):
	mail_server = smtplib.SMTP_SSL(email_details['server'])
	mail_server.login(email_details['username'], email_details['password'])
	mail_server.send_message(message)
	mail_server.quit()

if __name__ == '__main__':
	main()