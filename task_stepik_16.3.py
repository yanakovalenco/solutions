# Напишите функцию arithmetic_operation(), которая принимает символ одной из четырех арифметических операций
# (+, -, *, /) и возвращает функцию двух аргументов для соответствующей операции.

def arithmetic_operation(operation):
    mydict = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
    return mydict[operation]


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
