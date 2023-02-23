from src.Blockchain import Blockchain


def main():
    bc = Blockchain()
    print(f"{bc.epoch}")
    print(f"Adding elements to BC")
    for i in range(10):
        bc.add_block(f"data {i}")
    print(f"Printing Block")
    print(bc.getBlock(3))
    bc.print_chain()


if __name__ == '__main__':
    main()
