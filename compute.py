def myadd(a, b):
    """aとbの和を計算する

    Args:
        a (int): 1つ目の引数
        b (int): 2つ目の引数

    Returns:
        int: aとbの和
    """

    if a > 0 and b > 0:
        return a + b

    if a < 0 and b < 0:
        return a + b

    if a == 0:
        return b

    if b == 0:
        return a

    if a > 0 and b < 0:
        if abs(a) > abs(b):
            return a + b
        if abs(a) < abs(b):
            return a + b

    return 0


def mymult(a, b):
    """aとbの積を計算する

    Args:
        a (int): 1つ目の引数
        b (int): 2つ目の引数

    Returns:
        int: aとbの積
    """

    if a > 0 and b > 0:
        return a * b

    if a < 0 and b < 0:
        return a * b

    if a > 0 and b < 0:
        return a * b

    if a < 0 and b > 0:
        return a * b

    if a == 0:
        return 0

    if b == 0:
        return 0

    return -100
