# home work # 9
user_list = [
    {'user_name': 'Oliver', 'tel_number': '0670002222'},
    {'user_name': 'Katie', 'tel_number': '0670006688'},
    {'user_name': 'Jessica', 'tel_number': '0670007799'},
    {'user_name': 'Olivia', 'tel_number': '0670004777'},
    {'user_name': 'Harry', 'tel_number': '0670002255'}
]

say_hello = lambda: print('How can I help you?')
say_bye = lambda: print('Good bye!')

def show_all():
    for item in user_list:
        print(item.get('user_name'), item.get('tel_number'))

def add_contact(user_name, tel_number):
    new_contact = {'user_name': user_name, 'tel_number': tel_number}
    return user_list.append(new_contact)

def show_contact(user_name):
    contact = 'This contact does not exist!'
    for item in user_list:
        if item.get('user_name') == user_name:
            contact = item.get('user_name') + ' ' + item.get('tel_number')
    return print(contact)

def change_contact(user_name,phone):
    contact = 'this contact does not exist!'
    for item in user_list:
        if item.get('user_name') == user_name:
            item['tel_number'] = phone
            contact = f'The number {phone} {user_name} changed successfully!'
            return print(contact)
    return print(f'{user_name} - {contact}')

OPERATIONS = {
    'show': show_all,
    'add': add_contact,
    'phone': show_contact,
    'change': change_contact,
    'hello': say_hello,
    'exit': say_bye,
}

def user_input():
    user_msg = input('Enter one of the commands: hello, add, change, phone, show all, good bye, close, exit:')
    proc_user_msg = user_msg.split(' ')
    return proc_user_msg

def handler():
    while True:
        list = user_input()
        msg = list[0].lower()
        user_name = 'Noname'
        phone = '0000000000'
        if len(list) >= 2:
            user_name = list[1]
            if len(list) >= 3:
                phone = list[2]

        if msg == 'hello':
            OPERATIONS[msg]()
        elif msg == 'add':
            OPERATIONS[msg](user_name,phone)
        elif msg == 'change':
            OPERATIONS[msg](user_name,phone)
        elif msg == 'phone':
            OPERATIONS[msg](user_name)
        elif msg + ' ' + user_name.lower() == 'show all':
            OPERATIONS[msg]()
        elif (msg + ' ' + user_name.lower() == 'good bye') or msg == 'close' or msg == 'exit' or msg == '.':
            OPERATIONS['exit']()
            break
        else:
            print('Unknown command! Enter one of the commands: hello, add, change, phone, show all, good bye, close, exit.')

if __name__ == "__main__":
    handler()