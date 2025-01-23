def get_total_price(x, y):
    prices = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}
    print("Total: R$ {:.2f}".format(prices.get(x) * y))


x, y = map(int, input().split())
get_total_price(x, y)
