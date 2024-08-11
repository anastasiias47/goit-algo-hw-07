from classes import Record,AddressBook

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            print('There is no such name in contacts. Try another name')
        except IndexError:
            pass
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = 'Phone updated.'
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Phone added."
    if phone:
        record.edit_phone(phone,*_)
    return message


@input_error
def show_contact(args, book: AddressBook):
    name,*_ = args
    record = book.find(name)
    message = record.phones
    if record is None:
        message = 'There is no such record in the Address Book'
    return message


@input_error
def all_contacts(book: AddressBook):
    return book


def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    message = 'Birthday added'
    if record is None:
        message = 'There is no such record in the Address Book'
    if birthday:
        record.add_birthday(birthday)
    return message


def show_birthday(args, book: AddressBook):
    name,*_ = args
    record = book.find(name)
    message = record.birthday
    if record is None:
        message = 'There is no such record in the Address Book'
    return message



