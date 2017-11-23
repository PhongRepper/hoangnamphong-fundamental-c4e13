from random import randint, choice
from calcu import eval

while True:
    x = randint(0, 10)
    y = randint(0,10)
    op = choice(['+', '-', '*', '/'])
    error = randint(-1,1)
    TrueResult = eval(x, y, op)
    Result = TrueResult + error

    # correction = TrueResult - RanResult
    print("{0} {3} {1} = {2}".format(x,y,Result,op))
    # guess = input("(Y/N) ").lower()
    # gs = ['y', 'n']
    # if guess not in gs:
    #     print("ak;fjla;ksdjf")
    #     break
    # else:
    #     if correction == 0:
    #         if guess == 'y':
    #             print("correct")
    #         elif guess == 'n':
    #             print('incorrect')
    #             break
    #     else:
    #         if guess == 'y':
    #             print("incorrect")
    #             break
    #         elif guess == 'n':
    #             print('correct')
    # print("*" * 40)
