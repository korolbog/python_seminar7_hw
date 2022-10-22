import operations_logic as oplgc
import logger

def show():
    oplgc.show_phone_entries("phone_book.csv.txt")
    logger.add_log_entry('показ всех записей телефонной книги')

def add():
    oplgc.add_phone_entry()
    logger.add_log_entry('добавление номера')

def search():
    oplgc.search_phone_entry("phone_book.csv.txt")
    logger.add_log_entry('поиск номера')

def delete():
    oplgc.delete_phone_entry("phone_book.csv.txt")
    logger.add_log_entry('удаление номера')

