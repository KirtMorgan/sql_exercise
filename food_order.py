from sql_connection import add_order_sort

input_1 = input('What food do you wish to order?')
input_2 = int(input(f'How many {input_1} do you wish to order?'))
input_3 = float(input('How much is this item?'))
input_4 = input('What is the origin of this item?')

add_order_sort(f'{input_1}', f'{input_2}', f'{input_3}', f'{input_4}')