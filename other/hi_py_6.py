
def fun(x, y, z) -> bool:
    print(x, y, z)

    def rule1() -> bool:
        return x + y > 5

    def rule2() -> bool:
        return x + z > 5

    return rule1() or rule2()


print(fun(1, 2, 3))
print(fun(1, 4, 5))
