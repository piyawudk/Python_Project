def powerLoop(upto: int) -> None:
    for i in range(upto+1):
        print(i, end = ' ')
        print((7**i)%97)

powerLoop(3)
