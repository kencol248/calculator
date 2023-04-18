# Kenyah Collins
# 11/3/2022
# collins-calculator.py

# This program will provide the user the choices of add, subract, multiply, 
# and divide in order to make calculations of two numbers of the users choice.

calc_options = input('Please select one option: add/subtract/multiply/divide: ').lower()
print('You chose {}.'.format(calc_options))

first_num = input('What is the first number?')
second_num = input('What is the second number?')

first_num = float(first_num)
second_num = float(second_num)

answer = 0

# Shown below is the arithmetic for each option, with the results being 
# calculated then the calculation being shown to the user using print.
if calc_options == 'add':
    answer = first_num + second_num
    print('{} + {} = {}'.format(first_num, second_num, answer))
elif calc_options == 'subtract':
    answer = first_num - second_num
    print('{} - {} = {}'.format(first_num, second_num, answer))
elif calc_options == 'multiply':
    answer = first_num * second_num
    print('{} * {} = {}'.format(first_num, second_num, answer))     
elif calc_options == 'divide':
    answer = first_num / second_num
    print('{} / {} = {}'.format(first_num, second_num, answer))
else:
    print('Sorry, the option ({}) is not valid.'.format(calc_options))
    print('please Choose another option')
