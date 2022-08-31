import math
from typing import Tuple, List, Any


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


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
