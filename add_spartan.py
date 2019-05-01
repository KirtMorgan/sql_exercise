from sql_connection import add_spartan

while True:
    input_1 = input('What is the students name?')
    input_2 = int(input(f'What is {input_1} phone number'))
    input_3 = input(f'What course is {input_1} going on?')
    input_4 = input(f'Who is the trainer for {input_3}')
    add_spartan(f'{input_1}', f'{input_2}', f'{input_3}', f'{input_4}')
    user_input = input('Do you wish to add another item? y/n')

    if user_input == 'y':
        continue
    else:
        break
