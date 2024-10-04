import sys

sys.set_int_max_str_digits(100000000)

num1 = int(input('Введите первое число: '))

num2 = int(input('Введите второе число: '))

import time
time.sleep(0.1)
print('Ответы: ')

#num2 += 10
                
#num1 += 5

print('result:', num1 + num2)
print('result:', num1 - num2)
print('result:', num1 / num2)
print('result:', num1 * num2)
print('result:', num1 ** num2)
print('result:', num1 // num2)

import time
time.sleep(0.1)
print('Удачи ;)')

options = ['1','2','3','4','5' ]
user_input = ''
input_message = "Рейтинг:\n"
for index, item in enumerate(options):
    input_message += f'{index+1}) {item}\n'
input_message += 'Your choice: '
while user_input.lower() not in options:
    user_input = input(input_message)
print('You picked: ' + user_input)
def get_user_choice():
    options = { '1': 'Option 1', '2': 'Option 2', '3': 'Option 3', '4': 'Option 4', }
    while True:
        print("Select an option:")
        for key, value in options.items():
            print(f"{key}: {value}")
        user_input = input("Enter the number of your choice: ")
        if user_input in options:
            return options[user_input]
        else:
            print("Invalid choice. Please try again.")
import time

print('МОЛОДЕЦ')
time.sleep(1)
print('А ТЕПЕРЬ ПОШЁЛЬ НАХУЙ')

