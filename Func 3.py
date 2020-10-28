import itertools
import random


def permutation(li):
    global li_all
    li_all = list(itertools.permutations(li))
    print(li_all)


def function(list1, list2):
    res = []
    for num in list2:
        res.append(list1[num - 1])
    print(res)


if __name__ == '__main__':
    li_all = []
    n = int(input())
    S = range(1, n + 1)
    permutation(S)
    g = random.choice(li_all)
    h = random.choice(li_all)
    print(f"g:{g} h:{h}")
    function(g, h)
