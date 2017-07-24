import file_module
import user_module


def find_phone_number_by_last_name(entered_last_name, contact_list):
    for contact in contact_list:
        if entered_last_name == contact.last_name:
            return contact.phone

print('* Welcome to contact book 0.1a! *')

while 1 == 1:
    user_input = input('\n'
                       '\nIf you want to CREATE a new user press "1" '
                       '\nIf you want to LOAD existing user by last name press "2" '
                       '\nIf you want to QUIT the application press "q" ')
    if user_input == "1":
        new_user = user_module.create_user()
        file_module.save(new_user)
        print(new_user.first_name + ' ' + new_user.last_name + ' was successfully saved!')

    if user_input == "2":
        file_list = file_module.load_all()
        last_name = input('Enter last name to get a phone number: ')
        phone_number = find_phone_number_by_last_name(last_name, file_list)
        if phone_number == 'None':
            print(phone_number)
        else:
            print('No user with such last_name in contact book!')

    if user_input == "q":
        break
