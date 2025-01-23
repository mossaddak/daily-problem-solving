start_time, end_time = map(int, input().split())

if start_time > end_time:
    end_time += 24

duration = end_time - start_time if start_time != end_time else 24
print("O JOGO DUROU {} HORA(S)".format(duration))