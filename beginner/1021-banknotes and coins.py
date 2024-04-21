from decimal import Decimal

money = Decimal(input())

notes = [
    Decimal("100"),
    Decimal("50"),
    Decimal("20"),
    Decimal("10"),
    Decimal("5"),
    Decimal("2"),
]
coins = [
    Decimal("1"),
    Decimal("0.50"),
    Decimal("0.25"),
    Decimal("0.10"),
    Decimal("0.05"),
    Decimal("0.01"),
]


print("NOTAS:")
for note in notes:
    count = int(money / note)
    print("{} nota(s) de R$ {:.2f}".format(count, note))
    money %= note

print("MOEDAS:")
for coin in coins:
    count = int(money / coin)
    print("{} moeda(s) de R$ {:.2f}".format(count, coin))
    money %= coin
    