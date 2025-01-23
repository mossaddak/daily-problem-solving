durations = int(input())

hours = durations // 3600
durations %= 3600

minuites = durations // 60
durations %= 60

print(f"{hours}:{minuites}:{durations}")
