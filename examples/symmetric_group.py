import context
from src.std_group_lib import SymmetricGroup


def main():
    group = SymmetricGroup(3)
    print("group is abel? ", group.is_abel())
    for i in group.subgroups():
        print(i)
    group.print_table()


if __name__ == '__main__':
    main()
