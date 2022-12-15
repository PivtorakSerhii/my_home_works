from collections import UserDict

class Field():
    def __init__(self, value):
        self.value = value
class Name(Field):
    pass
class Phone(Field):
    pass

class Record():

    def __init__(self, name, phone_number=""):
        self.name = Name(name)
        self.phone_numbers = [Phone(phone_number)] if phone_number else []

    def add_phone_number(self, number):
        self.phone_numbers.append(Phone(number))

    def delete_phone_number(self, number):
        for i in self.phone_numbers:
            if i.value == number:
                self.phone_numbers.remove(i)

    def change_phone_number(self, old_number, new_number):
        self.delete_phone_number(old_number)
        self.add_phone_number(new_number)

    def show_phone_number(self):
        list_phone_number = []
        for i in self.phone_numbers:
            list_phone_number.append(i.value)
        return list_phone_number

class AddressBook(UserDict):

    def search(self, value):
        return value in self.data.values()

    def add_record(self, record):
        self.data[record.name.value] = record

    def all_show_phone_number(self):
        all_cont = ""
        for key, value in self.data.items():
            all_cont += f"{key}: {value.show_phone_number()}\n"
        return all_cont[:-1]


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as exception:
            return exception.args[0]

    return wrapper


def parser(msg):
    msg = msg.replace("show all", "show_all")
    msg = msg.replace("good bye", "good_bye")
    msg = msg.split(' ')
    command = msg[0].lower()
    name = None
    phone = None
    if len(msg) >= 2:
        name = msg[1]
    if len(msg) == 3:
        phone = msg[2]

    return command, name, phone


def show_all():
    return list_user.all_show_phone_number()

@input_error
def show_phone(name):
    res_phone = list_user.get(name)
    if res_phone is None:
        raise ValueError(f"Contact {name} not found")
    else:
        return res_phone.show_phone_number()

@input_error
def add_contact(name, phone=""):
    if not name:
        raise ValueError("More arguments needed")
    else:
        user = Record(name, phone)
        list_user.add_record(user)
        return "Number has been saved"

OPERATIONS = {
    "show all": show_all,
    "phone": show_phone,
    "add": add_contact,
    "change": add_contact
}

list_user = AddressBook()

def handler(user_msg):
    list_msg = parser(user_msg)
    if list_msg[0] == "hello":
        return "How can I help you?"
    elif list_msg[0] == "add":
        return (OPERATIONS["add"](list_msg[1], list_msg[2]))
    elif list_msg[0] == "change":
        return (OPERATIONS["change"](list_msg[1], list_msg[2]))
    elif list_msg[0] == "phone":
        return (OPERATIONS["phone"](list_msg[1]))
    elif list_msg[0] == "show_all":
        return (OPERATIONS["show all"]())
    elif list_msg[0] == "good_bye" or list_msg[0] == "close" or list_msg[0] == "exit":
        return "Good bye!"
    else:
        return "Error command"

def main():
    while True:
        user_msg = input("Enter some command (hello, show all, add, phone, change, exit):")
        result = handler(user_msg)
        print(result)
        if result == "Good bye!":
            break

if __name__ == "__main__":
    main()