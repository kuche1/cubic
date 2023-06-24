#! /usr/bin/env python3

def solve_quadratic(a, b, c):
    # z^2*a + z^1*b + z^0*c = 0

    # divide by a
    b /= a
    c /= a
    a = 1

    # z^2 + z*b + c = 0

    # z = y + d
    # y^2 + 2*y*d + d^2 + by + bd + c = 0
    #
    # 2*y*d + b*y = 0
    # 2*d + b = 0
    # 2*d = -b
    # d = -b/2
    d = -b/2

    # y^2 + d^2 + b*d + c = 0
    e = d**2 + b*d + c
    # y^2 + e = 0
    # y^2 = -e
    # y = +- (-e)**(0.5)

    y1 = (-e)**0.5
    y2 = -y1

    # z = y + d
    x1 = y1 + d
    x2 = y2 + d

    return x1, x2

def solve_cubic(original_a, original_b, original_c, original_d):

    a = original_a
    b = original_b
    c = original_c
    d = original_d


    # divide all by a
    b /= a
    c /= a
    d /= a
    a = 1

    # x^3 + b*x^2 + c*x + d = 0

    # x = y + e
    #
    # (y+e)^3 + b*(y+e)^2 + c(y+e) + d = 0
    # y^3 + 3 y^2 e + 3 y e^2 + e^3 + b y^2 + b 2 y e + b e^2 + cy + ce + d = 0
    #
    # 3 y^2 e + b y^2 = 0
    # 3e + b = 0
    # 3e = -b
    # e = -b/3
    e = -b/3

    # y^3 + 3*y*e^2 + e^3 + 2*b*y*e + b*e^2 + cy + ce + d = 0
    # y^3 + y(3*e^2 + 2*b*e + c) + e^3 + b*e^2 + ce + d = 0

    # f = 3*e^2 + 2*b*e + c
    # g = e^3 + b*e^2 + ce + d
    f = 3*e**2 + 2*b*e + c
    g = e**3 + b*e**2 + c*e + d

    # y^3 + yf + g = 0
    #
    # y = z + h/z

    # (z+h/z)^3 + f(z+h/z) + g = 0
    # z^3 + 3 z^2 h/z + 3 z (h/z)^2 + (h/z)^3 + fz + fh/z + g = 0
    # z^3 + 3zh + 3*h^2/z + (h/z)^3 + fz + fh/z + g = 0
    #
    # 3zh + fz = 0
    # 3h + f = 0
    # 3h = -f
    # h = -f/3
    h = -f/3

    # z^3 + 3*h^2/z + (h/z)^3 + fh/z + g = 0
    # z^3 + 3*f^2 / 9z - f^3/27*z^3 - f^2/3z + g = 0
    # z^3 + f^2 / 3z - f^3/27*z^3 - f^2 / 3z + g = 0
    # z^3 - f^3/27*z^3 + g = 0
    #
    # j =  - f^3 / 27
    j = - f**3 / 27

    # z^3 + j/z^3 + g = 0
    # z^6 + z^3*g + j = 0
    #
    # z^3 = z^3^2
    # w = z^3

    # w^2 + w*g + j = 0
    #
    # w = v + k

    # (v+k)^2 + vg + kg + j = 0
    # v^2 + 2vk + k^2 + vg + kg + j = 0
    #
    # 2vk + vg = 0
    # 2k + g = 0
    # 2k = -g
    # k = -g/2
    k = -g/2

    # v^2 + k^2 + kg + j = 0
    #
    # l = k^2 + kg + j
    l = k**2 + k*g + j

    # v^2 + l = 0
    # v^2 = -l
    # v = +- (-l)**1/2
    v1 = (-l)**(1/2)
    v2 = -v1

    w1 = v1 + k
    w2 = v2 + k

    # # w = z^3
    # # z = w**(1/3)
    # z1 = w1 ** (1/3)
    # z2 = w2 ** (1/3)
    #
    #
    #
    # z^3 = w
    # z^3 - w = 0
    # z^3 - w^(1/3) = 0
    # ( z - w^(1/3) ) * ( z^2 + w^(2/3) + z * w^(1/3) ) = 0
    # 
    # ( z - w^(1/3) ) = 0
    # ( z^2 + w^(2/3) + z * w^(1/3) ) = 0
    #
    # ( z - w^(1/3) ) = 0
    # z - w^(1/3) = 0
    # z = w^(1/3)
    z11 = w1 ** (1/3)
    z12 = w2 ** (1/3)

    # z^2 + w^(2/3) + z * w^(1/3) = 0
    # z^2 + z*(w^(1/3)) + w^(2/3) = 0
    z21, z31 = solve_quadratic(1, w1**(1/3), w1**(2/3))
    z22, z32 = solve_quadratic(1, w2**(1/3), w2**(2/3))

    # make it more readable
    z1 = z11
    z2 = z12
    z3 = z21
    z4 = z22
    z5 = z31
    z6 = z32

    # y1 = z1 + h/z1
    # y2 = z2 + h/z2
    y1 = z1 + h/z1
    y2 = z2 + h/z2
    y3 = z3 + h/z3
    y4 = z4 + h/z4
    y5 = z5 + h/z5
    y6 = z6 + h/z6

    # x1 = y1 + e
    # x2 = y2 + e
    x1 = y2 + e
    x2 = y2 + e
    x3 = y3 + e
    x4 = y4 + e
    x5 = y5 + e
    x6 = y6 + e

    return [x1, x2, x3, x4, x5, x6]


print('a*x^3 + b*x^2 + c*x + d = 0')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
d = int(input('Enter d: '))

solutions = solve_cubic(a, b, c, d)

for idx, x in enumerate(solutions):
    print()
    print(f'Solution {idx+1}')
    print(f'{x=}')
    print(f'{a * x**3 + b * x**2 + c * x**1 + d * x**0 = }')
