class AddOrDiv():
    """myaddもしくはmydivを計算する
    """

    def __init__(self, add_func, div_func):
        super().__init__()
        self.add = add_func
        self.div = div_func

    def do(self, a, b, c):
        """aとbの和もしくは商を計算する

        Args:
            a (int): 1つ目の引数
            b (int): 2つ目の引数
            c (str): "add"もしくは"div"．"add"が指定されたら"a+b"を，"div"が指定されたら"a/b"（小数点以下切り捨て）を返す

        Returns:
            int: a+bまたはa/b
        """
        if c == 'add':
            return self.add(a, b)
        if c == 'div':
            return self.div(a, b)
        return None
