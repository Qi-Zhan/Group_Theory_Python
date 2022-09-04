from src.std_group_lib import ProductGroup, CyclicGroup, KleinFourGroup


def main():
    g = ProductGroup([CyclicGroup(2), CyclicGroup(2)])
    g.print_table()
    g = KleinFourGroup("product")
    g.print_table()


if __name__ == '__main__':
    main()
