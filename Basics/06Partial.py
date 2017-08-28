#partial function

from functools import partial

def mult(x,y) :
    return x*y

def power(x,y) :
    return y**x

dbl = partial(mult, 2)
sqr = partial(power, 2)

print(dbl(5))
print(sqr(5))

