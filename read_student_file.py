import csv
with open('students.csv', 'r') as file:
    reader=csv.reader(file)
    next(reader)
    for i in reader:
        first_name=i[0]
        last_name=i[1]
        phone_number=i[2]
        birthdate=i[3]
        full_name=first_name+" "+last_name
        print(f"Name: {full_name:<20} Phone: {phone_number:<25} Birthdate: {birthdate}")