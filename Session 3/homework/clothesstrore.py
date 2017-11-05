items = ['T-shirt', 'Sweater', 'Jeans']
i = input("Welcome to our shop, what do you want (C, R, U, D)? ")
if i.upper() == "C":
    n = input("Enter new item: ")
    items.append(n)
    print("Our items:")
    print(*items, sep=', ')
elif i.upper() == 'R':
    print("Our items:")
    print(*items, sep=', ')
elif i.upper() == 'U':
    u = int(input('Update Position? '))
    n = input('New item? ')
    items[u - 1] = n
    print("Our items:")
    print(*items, sep=', ')
elif i.upper() == 'D':
    d = int(input('Delete position ?  '))
    items.pop(d-1)
    print("Our items:")
    print(*items, sep=', ')
