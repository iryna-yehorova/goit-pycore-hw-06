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
        if  len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain exactly 10 digits")

        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def find_phone(self, phone):
        for recorded_phone in self.phones:
            if recorded_phone.value == phone:
                return recorded_phone
        return None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        found_phone = self.find_phone(phone)
        if found_phone:
            self.phones.remove(found_phone)

    def edit_phone(self, phone, new_phone):
        found_phone = self.find_phone(phone)
        if found_phone is None:
            raise ValueError("Phone not found")

        index = self.phones.index(found_phone)
        self.phones[index] = Phone(new_phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record (self, record):
        self.data[record.name.value] = record

    def find (self, name):
        return self.data.get(name)

    def delete (self, name):
        self.data.pop(name, None)







