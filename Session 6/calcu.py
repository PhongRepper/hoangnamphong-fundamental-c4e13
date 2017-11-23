def eval(x, y, op):
    if op == '+':
        result = x + y
    elif op == '*':
        result= x * y
    elif op == '-':
        result = x - y
    elif op == '/':
        if y == 0:
            result = 'none'
        else:
            result = x / y
    return result
# x =10
# y = 5
# op = '+'
# r = eval(x, y, op)
# print(r)
#
#
# x = int(input("x= "))
# op = input("Operation(+, -, *, /): ")
# y = int(input("y = "))
#
# if op in ['+', '-','*', '/']:
#     #call eval here
#     r = eval()
#     print(r)
# else:
#     print('not')
