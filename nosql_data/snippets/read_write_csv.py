import csv
keys = employees[0].keys()
# Write to a CSV File
with open('/tmp/employees.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(employees)
# Read from CSV file
with open('/tmp/employees.csv', 'r') as output_file:
    print(output_file.read())