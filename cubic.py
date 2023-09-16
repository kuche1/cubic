#! /usr/bin/env python3

####################################### solve2

import copy

class Const:
    def __init__(s, name, power):
        assert type(name) == str
        assert type(power) in [int, float]
        s.name = name
        s.power = power
    def __repr__(s):
        return f'{s.name}**{s.power}'

class Term:
    def __init__(s, mul, consts_top, consts_bot):
        assert type(mul) in [int, float]
        assert type(consts_top) == set
        assert type(consts_bot) == set
        s.mul = mul
        s.consts_top = consts_top
        s.consts_bot = consts_bot

    def __repr__(s):
        ret = f'({s.mul}'
        for const in s.consts_top:
            ret += f'*{const}'
        ret += ')/('
        for const in s.consts_bot:
            ret += f'*{const}'
        ret += ')'

        if ret.endswith('/()'):
            ret = ret[1:]
            ret = ret[:-4]

        return ret

    def __truediv__(s, oth):
        term = copy.deepcopy(s)
        if type(oth) == Term:
            term_div = oth
            assert len(term_div.consts_top) == len(term_div.consts_bot) == 0, 'not implemented'
            term.mul /= term_div.mul
        else:
            assert False, 'not implemented'
        return term

#     def __add__(s, oth):
#         eq = Equasion(s)
#         eq += oth
#         return eq
#     def comp(s, oth): # compatible
#         return (s.con == oth.con and s.pow == oth.pow) or (s.pow == oth.pow == 0)

class Equasion:
    def __init__(s, terms):
        s.terms = terms
    
    def __repr__(s):
        ret = ''
        for term in s.terms:
            ret += f' + {term}'

        if ret.startswith(' + '):
            ret = ret[3:]

        return ret

    def __truediv__(s, oth):
        eq = s
        #print('+++ 1', eq)
        if type(oth) == Term:
            term_div = oth
            for idx, term in enumerate(eq.terms):
                #print('+++ 2', term)
                eq.terms[idx] = term / term_div
                #print('+++ 3', term)
        else:
            assert False, 'not implemented'
        #print('+++ 4', eq)
        return eq

    def replace_const(s, name, new_term):
        assert type(name) == str
        assert type(new_term) == Term, 'not implemented'
        for term_idx, term in enumerate(terms):
            for const_idx, const in enumerate(term.consts_top): # TODO repeat for bot
                if const.name == name:
                    new_eq = solve2eq_a_plus_b_pow(new_term, const.power)
                    TODO

#     def __add__(s, new_term):
#         eq = copy.deepcopy(s)
#         for term in eq.terms:
#             if term.comp(new_term):
#                 term.val += new_term.val
#                 return
#         eq.terms.append(new_term)
#         return eq

def solve2_pow(a, pow):
    assert type(a) == Term
    assert type(pow) in [int, float]

    if pow == 1:
        TODO
    
    elif pow == 2:
        TODO

    else:
        assert False, 'not implemented'

def solve2_p2_p0(a, b):
    # a*z**2 + b = 0
    # a*z**2 = -b
    # z**2 = -b/a
    # z = +- (-b/a)**0.5
    z1 = (-b/a)**0.5
    z2 = -z1
    return {z1, z2}

def solve2_p2_p1_p0(a, b, c):

    # a*z**2 + b*z + c = 0

    a = Term(a, {Const('z', 2)}, set())
    b = Term(b, {Const('z', 1)}, set())
    c = Term(c, set(),           set())

    eq = Equasion([a, b, c])

    # z**2 + b*z + c = 0
    eq /= Term(a.mul, set(), set())
    
    # z = y + d
    #
    # (y+d)**2 + b*(y+d) + c = 0
    eq.replace_const('z', Term(1, {Const('w', 1), Const('f', 1)}, set()))
    # y**2 + 2yd + d**2 + by + bd + c = 0
    #
    # 2yd + by = 0
    # 2d + b = 0
    # 2d = -b
    # d = -b/2
    #
    # y**2 + d**2 + bd + c = 0
    # y**2 + (-b/2)**2 + (-b/2)*d + c = 0
    # y**2 + b**2/4 -bd/2 + c = 0
    # y**2 + b**2/4 - 2bd/4 + c = 0
    # y**2 + (b**2-2bd)/4 + c = 0
    # y**2 = - (b**2-2bd)/4 - c

    print(eq)

solve2_p2_p1_p0(5, 4, 3)

import sys
sys.exit(69)

####################################### solve1

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

# def solve_4ic(a, b, c, d, e):

#     # a*z^4 + b*z^3 + c*z^2 + d*z + e = 0

#     # div by a
#     b /= a
#     c /= a
#     d /= a
#     e /= a
#     a = 1

#     # z^4 + b*z^3 + c*z^2 + d*z + e = 0


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
