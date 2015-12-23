__author__ = 'salmon-the-wise'

c = [2, 4, 8, 3, 1, 2, 3, 4, 7, 6, 9, 5]


def partial_sums(a):
    s = 0
    for i in a:
        s += i
        yield s

print(list(partial_sums(c)))
