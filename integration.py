class AddOrMult():
    """myaddもしくはmymultを計算する
    """

    def __init__(self, add_func, mult_func):
        super().__init__()
        self.add = add_func
        self.mult = mult_func

    def do(self, a, b, c):
        """aとbの和もしくは積を計算する

        Args:
            a (int): 1つ目の引数
            b (int): 2つ目の引数
            c (str): "add"もしくは"mult"．"add"が指定されたらa+bを，"mult"が指定されたら"a*b"を返す

        Returns:
            int: a+bまたはa*b
        """
        if c == 'add':
            return self.add(a, b)
        if c == 'mult':
            return self.mult(a, b)
        return None
