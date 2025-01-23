length = int(input())
in_count = 0
out_count = 0
for i in range(length):
    number = int(input())
    if 20 >= number >= 10:
        in_count += 1
    else:
        out_count += 1

print("{} in".format(in_count))
print("{} out".format(out_count))
