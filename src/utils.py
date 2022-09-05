import math
from typing import Tuple, List, Set, Any
from itertools import chain, combinations, permutations, product
from functools import reduce
from src.group_element import GroupElement


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def factor(n: int) -> List[int]:
    assert n >= 1
    return [i for i in range(1, n + 1) if n % i == 0]


def all_permutations(n: int) -> [Tuple[int, ...]]:
    return list(permutations(range(1, n + 1), n))


def permute(f: Tuple[int, ...], g: Tuple[int, ...]) -> Tuple[int, ...]:
    """ return f(g())
    """
    assert (len(f) == len(g))
    assert (len(set(f)) == len(f))
    assert (len(set(g)) == len(g))
    res = []
    for order, i in enumerate(f):
        res.insert(order, g[i - 1])
    return tuple(res)


def power_set(s: Set[GroupElement]) -> Set[Tuple[GroupElement, ...]]:
    s = list(s)
    pt = chain.from_iterable(set(combinations(s, r)) for r in range(len(s) + 1))
    return set(pt)


def cartesian_product(s: [Set[Any]]) -> Set[Any]:
    return set(product(*s))


def reduce_multi(factors: [int]) -> int:
    return reduce(lambda x, y: x * y, factors, 1)


def rotation_n(order: int, n: int) -> Tuple[int, ...]:
    return tuple(map(lambda x: x + 1, [(order + i) % n for i in range(n)]))


def reflection_n(order: int, n: int) -> Tuple[int, ...]:
    if n % 2 == 1:
        return tuple(map(lambda x: x + 1, [(2 * (order - 1) - i + n) % n for i in range(n)]))
    else:
        return tuple(map(lambda x: x + 1, [((order - 1) - i + n) % n for i in range(n)]))


def parity_permutation(p: Tuple[int, ...]) -> int:
    """
    :param p: permutation
    :return: 1 if odd permutation, 0 if even permutation
    """
    count = 0
    for i, num in enumerate(p, start=1):
        count += sum(num > num2 for num2 in p[i:])
    return count % 2
