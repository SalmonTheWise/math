__author__ = 'salmon-the-wise'
a = [1, 5, 11, 12]
b = 7


def closest_gene(gen, pos):
    n = [abs(i-pos) for i in gen]
    idx = n.index(min(n))
    return gen[idx]

print(closest_gene(a, b))
