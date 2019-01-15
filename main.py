import os
import csv

def main():
    csv_file = 'students.csv'
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_id = row['id']
            first_name = row['first_name']
            last_name = row['last_name']
            email = row['email']
            gender = row['gender']
            date_of_birth = row['date_of_birth']

            print('useradd -c "{} {}" {}'.format(first_name, last_name, (first_name + last_name + student_id)))

main()
