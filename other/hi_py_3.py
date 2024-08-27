#
# example for *args
#
def impl(a: str, b: str, c: list):
    print(f"impl(a={a}, b={b}, c={c})")


def test(name: str, *args):
    impl(*args)


test("test", "1", "2", [4, 5, 6])


#
# example for **kwargs
#
def process_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Example usage
process_kwargs(name="Alice", age=30, city="Wonderland")


# Passing kwargs to another function
def another_function(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")


kwargs = {"name": "Alice", "age": 30, "city": "Wonderland"}
another_function(**kwargs)


def yet_another_function(x, y, z, **kwargs):
    print(f"x: {x}, y: {y}, z: {z}")
    print(kwargs)


yet_another_function(x=1, y=2, z=3, name="Alice", age=30, city="Wonderland", country="USA")
