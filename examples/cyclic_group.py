import context
from src.std_group_lib import CyclicGroup


def main():
    group = CyclicGroup(11)
    group.print_table()
    for i in group.subgroups():
        print(i)
    assert len(group.nontrivial_subgroups()) == 0


if __name__ == '__main__':
    main()
