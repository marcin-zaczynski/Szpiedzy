def funkcj(f, liczba):
    return f(liczba)


print(funkcj(lambda x: x * x, 3))

def kwadrat(x):
    return x*x

print(kwadrat(5))

wyn = (lambda x: x * x)(6)

print(wyn)

lam = lambda x: x * x
print(lam(8))

lam2 = lambda x, y: x * y

print(lam2(5,6))

print((lambda x, y: x + y)(5, 4))
