class Grand:
    def __init__(self):
        self.name = "爷爷"
        pass


class Parent(Grand):
    def __init__(self):
        super().__init__()
        # self.name = "父亲"
        pass


class Child(Parent):
    def __init__(self):
        super().__init__()
        # self.name = "儿子"
        pass


child = Child()
# child.name = '张破虏'
print(child.name)
