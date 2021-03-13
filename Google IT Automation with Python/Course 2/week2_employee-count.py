# Coursera, Google IT Automation with Python
# Course 2, Using Python to Interact with the Operating System
# Week 2, Managing Files with Python
# Count the number of employees in each department and write to a file.

import csv

def read_employees(file_path):
	csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
	employee_file = csv.DictReader(open(file_path), dialect='empDialect')
	employee_list = []
	for employee in employee_file:
		employee_list.append(employee)
	return employee_list

def process_data(employee_list):
	department_list = []
	for employee in employee_list:
		department_list.append(employee['Department'])

	department_data = {}
	for department in set(department_list):
		department_data[department] = department_list.count(department)
	return department_data

def write_report(department_data, report_file):
	with open(report_file, "w+") as file:
		for key in sorted(department_data):
			file.write("{} has {} employees\n".format(key, department_data[key]))

employee_list = read_employees("files/employees.csv")
print(employee_list, '\n')

department_data = process_data(employee_list)
print(department_data)

write_report(department_data, "files/department_data.txt")

