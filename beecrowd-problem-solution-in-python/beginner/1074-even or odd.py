N = int(input())

for _ in range(N):
    n = int(input())
    if n > 0 and n % 2 == 0:
        print("EVEN POSITIVE")
    elif n < 0 and n % 2 == 0:
        print("EVEN NEGATIVE")
    elif n > 0 and n % 2 != 0:
        print("ODD POSITIVE")
    elif n < 0 and n % 2 != 0:
        print("ODD NEGATIVE")
    else:
        print("NULL")
