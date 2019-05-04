
"""
Select Desafio

"""

"""
Desafio 2 - Reading
Read user Birth Date and print message
"""
print('When were you born?')
dia = int(input('Dia = '))
mes = int(input('Mes = '))
ano = int(input('Ano = '))
print('You were born in {}, {}, {}'.format(dia, mes, ano))

"""
Desafio 3 - Sum 2 numbers
Read from user 2 numbers and show the sum result 
"""
num1 = int(input('Type in number 1: '))
num2 = int(input('Type in number 2: '))
print('The sum of {} and {} is {}'.format(num1, num2, num1+num2))

"""
Desafio 4 - Primitive type
Read from user anything and show what type of variable is
"""
num3 = input('Type in anything: ')
print('The variable is alphanumeric? {}'.format(num3.isalnum()))
print('The variable is numeric? {}'.format(num3.isnumeric()))
print('The variable is alpha? {}'.format(num3.isalpha()))
