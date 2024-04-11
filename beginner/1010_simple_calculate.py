p1 = input().split(" ")
p2 = input().split(" ")
p1_code, p1_unit, p1_price = p1
p2_code, p2_unit, p2_price = p2
total_price = (int(p1_unit) * float(p1_price)) + (int(p2_unit) * float(p2_price))
print(f"VALOR A PAGAR: R$ {total_price:.2f}")
