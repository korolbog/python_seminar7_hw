import csv
from csv import DictWriter
import operations_shell as opshell

def show_phone_entries(file_name):
    fields = []
    rows = []
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    print('' + ''.join(field for field in fields))
    for row in rows:
        for col in row:
            print("%10s"%col,end=" "),
        print('\n')


def add_phone_entry():
    opshell.show()
    print('Введите ID человека: ')
    id_person = int(input())
    print('Введите фамилию: ')
    family_name = input()
    print('Введите имя: ')
    first_name = input()
    print('Введите отчество или второе имя: ')
    second_name = input()
    print('Введите номер телефона с плюсом и без пробелов: ')
    phone_number = input()

    phone_book_field_names = ['id_person', 'family_name', 'first_name', 'second_name', 'phone_number']

    phone_book_dict = {'id_person': id_person, 'family_name': family_name,
                       'first_name': first_name, 'second_name': second_name,
                       'phone_number': phone_number}

    with open('phone_book.csv.txt', 'a') as file:
        dictwriter = DictWriter(file, fieldnames=phone_book_field_names)
        dictwriter.writerow(phone_book_dict)
        file.close()

    print('Спасибо. Данные внесены.')

def search_phone_entry(file_name):
    phone_number = input('Введите искомый номер телефона: ')

    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if phone_number in line:
                print(line)

def delete_phone_entry(file_name):
    try:
        with open(file_name, 'r') as rfile:
            lines = rfile.readlines()
            phone_number = input('Введите номер телефона для удаления: ')
            with open(file_name, 'w') as wfile:
                for line in lines:
                    if phone_number not in line:
                        wfile.write(line)
                        print(line)
    except:
        print("Oops! Something went wrong.")