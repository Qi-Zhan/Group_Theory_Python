import context
from src.group_element import Permutation
from src.std_group_lib import SymmetricGroup


def main():
    """
    A nontrivial quotient group example
    Name    Group                      Order
    G       S(4)                       24
    N       klein4Group.elements()     4
    G / N   S(4) / klein4group         6
    """
    G = SymmetricGroup(4)
    N = {Permutation((1, 2, 3, 4)), Permutation((2, 1, 4, 3)), Permutation((3, 4, 1, 2)), Permutation((4, 3, 2, 1))}
    G_mod_N = G.quotient(N)
    G_mod_N.print_table()


if __name__ == '__main__':
    main()
