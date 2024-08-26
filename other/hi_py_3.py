
def impl(a: str, b: str, c: list):
    print(f"impl(a={a}, b={b}, c={c})")


def test(name: str, *args):
    impl(*args)


test("test", "1", "2", [4, 5, 6])
