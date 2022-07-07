import argparse
from compute import myadd, mydiv
from integration import AddOrDiv


def mycompute(a, b, c):
    """aとbの和もしくは商を計算する

    Args:
        a (int): 1つ目の引数
        b (int): 2つ目の引数
        c (str): "add"もしくは"div"．"add"が指定されたら"a+b"を，"div"が指定されたら"a/b"（小数点以下切り捨て）を返す

    Returns:
        int: a+bまたはa/b
    """
    if c == "add":
        return myadd(a, b)
    if c == "div":
        return mydiv(a, b)
    return


def main():
    parser = argparse.ArgumentParser(description='add or divide two numbers')
    parser.add_argument('arg1', type=int,
                        help='first argment')
    parser.add_argument('arg2', type=int,
                        help='second argment')
    parser.add_argument('arg3', choices=['add', 'div'],
                        help='add or div (default: add)')
    args = parser.parse_args()
    a = args.arg1
    b = args.arg2
    c = args.arg3

    val = mycompute(a, b, c)
    print(val)

    add_or_mult_instance = AddOrMult(myadd, mydiv)
    val = add_or_mult_instance.do(a, b, c)
    print(val)


if __name__ == '__main__':
    main()
