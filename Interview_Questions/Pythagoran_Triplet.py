import itertools


def hasPythagoranTriplet(customList: list):
    customList = set([i ** 2 for i in customList])
    combi = set(map(lambda x: sum(x), itertools.combinations(customList, 2)))
    print(True if customList & combi else False)


if __name__ == '__main__':
    hasPythagoranTriplet(range(29, 50))
