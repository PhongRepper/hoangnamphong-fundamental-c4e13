print("""________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________
______¶¶¶¶¶¶_____________¶¶¶¶¶¶________
_____¶¶¶¶¶_________________¶¶¶¶¶¶______
____¶¶¶¶_____________________¶¶¶¶¶_____
___¶¶¶¶_______________________¶¶¶¶¶____
__¶¶¶¶_____¶¶¶¶_______¶¶¶¶______¶¶¶____
__¶¶¶_____¶¶¶¶¶¶_____¶¶¶¶¶¶_____¶¶¶¶___
_¶¶¶¶_____¶¶¶¶¶¶_____¶¶¶¶¶¶______¶¶¶___
_¶¶¶_______¶¶¶¶_______¶¶¶¶_______¶¶¶¶__
_¶¶¶______________________________¶¶¶__
_¶¶¶______________________________¶¶¶__
_¶¶¶______________________________¶¶¶__
_¶¶¶____________¶¶¶¶¶____________¶¶¶¶__
_¶¶¶¶________¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶___
__¶¶¶______¶¶¶¶¶_____¶¶¶¶¶______¶¶¶¶___
__¶¶¶¶____¶¶¶___________¶¶¶____¶¶¶¶____
___¶¶¶¶___¶¶_____________¶¶___¶¶¶¶_____
____¶¶¶¶____________________¶¶¶¶¶______
_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______
_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________""")
print("Welcome")
from random import randint
n = randint(1, 100)
if n < 30:
    print("sad")
elif n < 60:
    print("normal")
else:
    print("happy")
