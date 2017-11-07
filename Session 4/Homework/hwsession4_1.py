inventory = {
    'gold': 500,
    'pouch':  ['flint', 'wine', 'gem stone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
}
# Add 'pocket' to inventory
print('Add pocket')
inventory['pocket']=[]
print (inventory)

# Set value to pocket
print('Set value to pocket')
inventory['pocket']=['seashell', 'strange berry', 'lint']
print(inventory)

# Remove dagger
print('Remove dagger')
inventory['backpack'].remove('dagger')
print(inventory)

 # Add money
n = int(input('How much do ya wanna add? '))
inventory['gold'] = 500 + n
print(inventory)
