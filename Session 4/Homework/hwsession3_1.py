items = ['T-shirt', 'sweater', 'Jeans']
i = input("Welcome to our shop, what do you want (C, R, U, D)? ")

if i == "C":
    n = input("Enter new item: ")
    items.append(n)
    print('Our items:', *items, sep=', ')

if i == 'R':
    print('Our items: ' , *items, sep=', ')

if i == 'U':
    u = int(input('Update Position? '))
    n = input('New item? ')
    items[u - 1] = n
    print('Our items: ', *items, sep=', ')

if i == 'D':
    d = input('What do you want to remove? ')
    if d in items:
        items.remove(d)
        print('Our items: ', *items, sep=', ')
    else:
        print('There is no ',d, 'in our list')
