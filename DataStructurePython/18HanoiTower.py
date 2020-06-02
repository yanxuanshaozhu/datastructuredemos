def move(height: int, fromtower: int, totower: int, sidetower: int) -> None:
    if height >= 1:
        move(height - 1, fromtower, sidetower, totower)
        transfer(fromtower, totower)
        move(height - 1, sidetower, totower, fromtower)


def transfer(fromtower: int, totower: int) -> None:
    print("move one disk from tower ", fromtower, " to tower ", totower)


if __name__ == "__main__":
    move(3, 1, 2, 3)
