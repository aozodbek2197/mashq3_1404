# 1-masala
class Parent:
    def show(self):
        return "Parent"

class Child(Parent):
    def show(self):
        return "Child"
# 2-masala
class Book:
    def __init__(self, p):
        self.p = p

    def __str__(self):
        return f"Price: {self.p}"
# 3-masala
class Count:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return self.i
        raise StopIteration
# 4-masala
class File:
    def __enter__(self):
        print("Open")
    def __exit__(self, a, b, c):
        print("Close")
# 5-masala
class Decor:
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Start")
        self.f()
        print("End")
