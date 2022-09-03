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


def reduce_multi(l: [int]) -> int:
    return reduce(lambda x, y: x * y, l, 1)
