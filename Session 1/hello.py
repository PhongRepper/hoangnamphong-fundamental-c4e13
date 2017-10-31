# yob = int(input("Your year of birth?"))
# age = 2017 - int(yob)
# print(age)
#
# if age < 10:
#     print("Baby")
# elif age < 18:
#     print("Teenager")
# else:
#     print("Adult")
# print("Bye bye")
a = int(input("a = ?"))
b = int(input("b = ?"))
c = int(input("c = ?"))
delta = b ** 2 - 4 * a * c
d_2 = delta ** 0.5
f_2 = 2 * a
if delta < 0:
    print("VN")
elif delta == 0:
    x = -b / f_2
    print("NK", x)
else:
    x1 = -b + d_2 / f_2
    x2 = -b - d_2 / f_2
    print("NPB", x1, x2)
    print("2NPB: x1={0}, x2={1}".format(x1, x2))
