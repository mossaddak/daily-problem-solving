age = int(input())

# year
age %= 365
print("{} ano(s)".format(age // 365))

# month
age %= 30
print("{} mes(es)".format(age // 30))

# day
print("{} dia(s)".format(age))
