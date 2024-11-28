def somme_varargs(*args):
    s = 0
    for x in args:
        s += x
    return s

print(somme_varargs(1,2,3,4))