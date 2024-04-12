a, b, c = map(float, input().split())

triangle = 1 / 2 * a * c
circle = 3.14159 * c**2
trapezium = 1 / 2 * (a + b) * c
square = b**2
rectangle = a * b

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")
