prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stocks = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

# for fruit in prices:
#     print(fruit)
#     print('price: {}'.format(prices[fruit]))
#     print('stock: {}'.format(stocks[fruit]))
for fruit in prices:
    print(fruit,':', stocks[fruit])
    print('price:', prices[fruit])
    total = stocks[fruit]*prices[fruit]
    print("total money from", fruit, 'is', total, "$")
    print()
# money sold
