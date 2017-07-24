from contact import Contact


def create_user():
    first_name = input('Please enter first name: ')
    last_name = input('Please enter last name: ')
    phone = input('Please enter phone number: ')
    email = input('Please enter email: ')
    return Contact(first_name, last_name, phone, email)
