money = int(input())
print(money)

print("{} nota(s) de R$ 100,00".format(money // 100))
money %= 100

print("{} nota(s) de R$ 50,00".format(money // 50))
money %= 50

print("{} nota(s) de R$ 20,00".format(money // 20))
money %= 20

print("{} nota(s) de R$ 10,00".format(money // 10))
money %= 10

print("{} nota(s) de R$ 5,00".format(money // 5))
money %= 5

print("{} nota(s) de R$ 2,00".format(money // 2))
money %= 2

print("{} nota(s) de R$ 1,00".format(money // 1))
money %= 1
