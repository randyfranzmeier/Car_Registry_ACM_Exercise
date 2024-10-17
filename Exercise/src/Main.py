from Exercise.src.Registry import Registry
from src.Car import Car

def get_user_bool_input(prompt):
    while True:
        expired_tabs = input(prompt)
        if expired_tabs.len() == 1:
            if expired_tabs == 'y':
                return True
            elif expired_tabs == 'n':
                return False
        print("Invalid input. Please try again.")


def is_valid_make_or_model(input, is_make):
    for char in input
        if not (char.isalpha()) and is_make:
            return False
    return True


def get_user_make():
    while True:
        make = string(input('Please enter your cars make (eg. Honda): '))
        if is_valid_make_or_model(make, True):
            return make
        else:
            print('invalid input. Try again.')


def get_user_model():
    while True:
        model = input('Please enter your cars model (eg. Civic): ')
        if is_valid_make_or_model(model):
            return model
        else:
            print('invalid input. Try again.')


def get_user_year():
    while True:
        try:
            year = input('Please enter your cars year: ')
            if year > 2025 or year < 1900:
                print('invalid year. Please enter a year from 1901-2025')
            else:
                return year
        catch:
            print("Invalid input. Please try again.")


def is_valid_vin(VIN):
    if len(VIN) == 0:
        return False

    letters, nubers = 0, 0
    for char in VIN:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            nubers += 1
    return letters == 5 and nubers == 5


def get_user_vin():
    while True:
        vin = input('Please enter your cars VIN \nA VIN is a sequence of 5 letters and 5 numbers: ')
        if is_valid_vin(vin):
            print(vin)
        else:
            print('Invalid input. Try again.')


def get_user_car_options():
    vin = get_user_vin()
    make = get_user_make()
    model = get_user_make()
    year = get_user_year()
    has_expired_tabs = get_user_bool_input('Does your car have expired tabs (yes-> y, no -> n): ')
    return new Car(vin, make, model, year, has_expired_tabs)


def print_welcome_message():
    print('-----Welcome to Cool Car Registry-----')
    print('You will be prompted to enter your cars information, and can register multiple cars if you wish.')
    print('Business hours are 4:30-6:30pm Every Thursday.\n')


class Main:

    def start_program(self):
        registry = Registry([])
        print_welcome_message()

        while True:
            car = get_user_car_options
            registry.add_car_to_registry(car)
            registry.print_registered_cars()
            if get_user_bool_input('Register more cars? (yes -> y, no -> n): '):
                break

        print('Thanks for registering your cool cars!')
        if registry.cars_have_expired_tabs():
            print('Make sure to renew your tabs!')


start_program()

