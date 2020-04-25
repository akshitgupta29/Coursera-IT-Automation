import csv

def read_employees (csv_file_location):
    with open (csv) as file:
        
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        dict1 = csv.DictReader(file, dialect='empDialect')
        employee_list = []
        for data in dict1:
            employee_list.append(data)
    return employee_list

employee_list = read_employees('/home/student-01-b7518cdbbe41/data/employees.csv')

def process_data(employee_list):
    department_list = []
    for emp in employee_list:
        department_list.append(emp['Department'])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

dictionary = process_data(employee_list)

def write_report(dictionary, report_file):
    with open (report_file, 'w+') as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')

write_report(dictionary, '/home/student-01-b7518cdbbe41/data/reports.txt')
    
