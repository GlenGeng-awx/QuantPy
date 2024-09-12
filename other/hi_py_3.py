#
# example for **kwargs
#
def process_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Example usage
process_kwargs(name="Alice", age=30, city="Wonderland")


# Passing kwargs to another function
def another_function(name, age, city, **kwargs):
    print(f"Name: {name}, Age: {age}, City: {city}")
    print(kwargs)


def yet_another_function(x, y, z, **kwargs):
    print(f"x: {x}, y: {y}, z: {z}")
    print(kwargs)
    another_function(**kwargs)


kwargs = {"name": "Alice", "age": 30, "city": "Wonderland"}
another_function(**kwargs)
yet_another_function(x=1, y=2, z=3, name="Alice", age=30, city="Wonderland", country="USA")


d1 = {
    'a': 1,
    'b': 2,
    'c': 3,
}

d2 = {
    **d1,
    'c': 4,
}

print(d1)
print(d2)
