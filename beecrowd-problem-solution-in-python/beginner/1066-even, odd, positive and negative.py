even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0

for i in range(5):
    number = int(input())
    if number % 2 == 0:
        even_count += 1
    if number % 2 != 0:
        odd_count += 1
    if number > 0:
        positive_count += 1
    if number < 0:
        negative_count += 1

print("{} valor(es) par(es)".format(even_count))
print("{} valor(es) impar(es)".format(odd_count))
print("{} valor(es) positivo(s)".format(positive_count))
print("{} valor(es) negativo(s)".format(negative_count))