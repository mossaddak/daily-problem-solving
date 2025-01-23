import math

a, b, c = map(float, input().split())

quadratic_discriminant = (b**2) - (4 * a * c)

if quadratic_discriminant > 0 and a > 0:
    twice_a = 2 * a
    r1 = (-b + (math.sqrt(quadratic_discriminant))) / twice_a
    r2 = (-b - (math.sqrt(quadratic_discriminant))) / twice_a

    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))

else:
    print("Impossivel calcular")
