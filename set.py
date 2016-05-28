


def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(20))
print(20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)