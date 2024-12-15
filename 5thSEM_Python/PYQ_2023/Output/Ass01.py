a=20
def f():
    a=2
    def g():
        a=5
        print(a)
    g()
    print(a)
f()
print(a)