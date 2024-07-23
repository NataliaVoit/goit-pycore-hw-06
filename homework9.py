from datetime import datetime, timedelta
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be a 10-digit number.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def remove_phone(self, phone):
        record_phone = self.find_phone(phone)
        if record_phone:  
            self.phones.remove(record_phone)
            return "phone removed"
        return "Phone not found" 

    def edit_phone(self, old_phone, new_phone):
        record_phone = self.find_phone(old_phone)
        if record_phone:  
            record_phone.value = new_phone
            return "phone changed"
        return "Phone not found."

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        print("Phone not found.")



class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        record = self.find(name)
        if record:
            del self.data[name]
            return "contact deleted"
        return "contact not found"
    
if __name__ == "__main__":

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    print("*"*50)
    for name, record in book.data.items():
        print(record)

    maria_record = Record("maria")
    maria_record.add_phone("1555555505")
    maria_record.add_phone("9999999999")
    book.add_record(maria_record)
    maria = book.find("maria")
    
    maria.edit_phone("1555555505", "4444444444" )
    print("*"*50)
    for name, record in book.data.items():
        print(record)


    book.add_record(maria_record)