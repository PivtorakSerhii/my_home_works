from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    pass


class Phone(Field):
    @Field.value.setter
    def value(self, new_value):
        if new_value is not None and len(new_value) == 10:
            self._value = new_value
        else:
            self._value = "-"
            print("The phone number must be 10 digits long. Number not saved.")


class Birthday(Field):
    @Field.value.setter
    def value(self, new_value):
        if new_value is not None:
            self._value = datetime.strptime(new_value, "%d.%m.%Y").date()


class AddressBook(UserDict):
    POS = 0
    MAX_CONT = 3

    def str_or_obj(self, bday):
        if isinstance(bday, str):
            return ("-")
        else:
            return bday.value

    def search(self, value):
        return value in self.data.values()

    def add_record(self, record):
        self.data[record.name.value] = record

    def all_show_phone_number(self):
        all_cont = ""
        for key, value in self.data.items():
            all_cont += f"{key}: {value.show_phone_number()[0]} | birthday: {self.str_or_obj(value.birthday)}\n"
        return all_cont[:-1]

    def keys(self):
        key_book = []
        for key, value in self.data.items():
            key_book.append(key)
        return (key_book)

    def __next__(self):
        if self.POS < len(self.keys()):
            cont = ""
            i = self.POS
            k = self.keys()
            while i < self.POS + self.MAX_CONT and i < len(k):
                cont += f"{k[i]}: {self.data.get(k[i]).show_phone_number()[0]} | birthday: {self.str_or_obj(self.data.get(k[i]).birthday)}\n"
                i += 1
            self.POS = i
            return cont
        return "End contact list"
        #raise StopIteration

    def __iter__(self):
        return self


class Record(AddressBook):

    def __init__(self, name, phone_number=None, birthday=None):
        self.name = Name(name)
        self.phone_number = []
        if phone_number:
            self.add_phone_number(phone_number)

        if birthday is not None:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = "-"

    def add_phone_number(self, number):
        self.phone_number.append(Phone(number))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def delete_phone_number(self, number):
        for i in self.phone_number:
            if i.value == number:
                self.phone_number.remove(i)

    def change_phone_number(self, old_number, new_number):
        self.delete_phone_number(old_number)
        self.add_phone_number(new_number)

    def show_phone_number(self):
        list_phone_number = []
        for i in self.phone_number:
            list_phone_number.append(i.value)
        return list_phone_number

    def days_to_birthday(self):
        if self.birthday.value is not None:
            current_datetime = datetime.now().date()
            bday_date = self.birthday.value
            next_bday = datetime(year=current_datetime.year,
                                 month=bday_date.month, day=bday_date.day).date()
            if next_bday >= current_datetime:
                res = (next_bday - current_datetime).days
                return res
            else:
                next_bday = datetime(year=current_datetime.year + 1,
                                     month=bday_date.month, day=bday_date.day).date()
                res = (next_bday - current_datetime).days
                return res
        else:
            return "Birthday not specified"


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
    msg = msg.replace("until birthday", "until_birthday")
    msg = msg.split(' ')
    command = msg[0].lower()
    name = None
    phone = None
    birthday = None
    if len(msg) >= 2:
        name = msg[1]
    if len(msg) >= 3:
        phone = msg[2]
    if len(msg) == 4:
        birthday = msg[3]

    return command, name, phone, birthday


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
def add_contact(name, phone="", birthday=None):
    if not name:
        raise ValueError("More arguments needed")
    else:
        user = Record(name, phone, birthday)
        list_user.add_record(user)
        return "Contact saved"


@input_error
def add_birthday(name, birthday):
    res_birthday = list_user.get(name)
    if res_birthday is None:
        raise ValueError(f"Contact {name} not found")
    else:
        res_birthday.birthday.value = birthday
        return "Birthday saved"


@input_error
def until_birthday(name):
    bday = list_user.get(name)
    if bday is None:
        raise ValueError(f"Contact {name} not found")
    else:
        bday = bday.days_to_birthday()
        return f"Birthday in {bday} days"


@input_error
def show_list():
    return next(list_user)


OPERATIONS = {
    "show all": show_all,
    "phone": show_phone,
    "add": add_contact,
    "change": add_contact,
    "birthday": add_birthday,
    "until birthday": until_birthday,
    "list": show_list
}

list_user = AddressBook()


def handler(user_msg):
    list_msg = parser(user_msg)
    if list_msg[0] == "hello":
        return "How can I help you?"
    elif list_msg[0] == "add":
        return (OPERATIONS["add"](list_msg[1], list_msg[2], list_msg[3]))
    elif list_msg[0] == "change":
        return (OPERATIONS["change"](list_msg[1], list_msg[2]))
    elif list_msg[0] == "phone":
        return (OPERATIONS["phone"](list_msg[1]))
    elif list_msg[0] == "birthday":
        return (OPERATIONS["birthday"](list_msg[1], list_msg[2]))
    elif list_msg[0] == "show_all":
        return (OPERATIONS["show all"]())
    elif list_msg[0] == "good_bye" or list_msg[0] == "close" or list_msg[0] == "exit":
        return "Good bye!"
    elif list_msg[0] == "until_birthday":
        return (OPERATIONS["until birthday"](list_msg[1]))
    elif list_msg[0] == "list":
        return (OPERATIONS["list"]())
    else:
        return "Error command"


def main():
    while True:
        user_msg = input("Enter some commands:")
        result = handler(user_msg)
        print(result)
        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()