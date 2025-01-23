initial_hour, initial_minute, final_hour, final_minute = map(int, input().split())

if initial_hour > final_hour or (
    initial_hour == final_hour and initial_minute > final_minute
):
    final_hour += 24

if initial_minute > final_minute:
    final_minute += 60
    final_hour -= 1

hours = final_hour - initial_hour
minutes = final_minute - initial_minute

if hours == minutes == 0:
    hours = 24

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hours, minutes))