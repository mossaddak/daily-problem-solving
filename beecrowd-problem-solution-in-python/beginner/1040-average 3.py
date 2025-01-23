n1, n2, n3, n4 = map(float, input().split())
average = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / (2 + 3 + 4 + 1)

print("Media: {:.1f}".format(average))

if average < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= average <= 6.9:
    print("Aluno em exame.")
    score = float(input())
    print("Nota do exame: {}".format(score))
    average = (score + average) / 2
    if average >= 5.0:
        print("Aluno aprovado.")
        print("Media final: {}".format(average))
    else:
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(average))

elif average >= 7.0:
    print("Aluno aprovado.")
