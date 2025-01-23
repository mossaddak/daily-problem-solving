A, B, C, D = map(int, input().split())

(
    print("Valores aceitos")
    if B > C and D > A and (C + D) > (A + B) and D > 0 and A % 2 == 0
    else print("Valores nao aceitos")
)
