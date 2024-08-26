
class ABC:
    def __init__(self):
        print("ABC class object created")

    def method(self):
        print(f"{__class__.__name__}")


class DEF:
    def __init__(self):
        print("DEF class object created")

    def method(self):
        print(f"{__class__.__name__}")


if __name__ == "__main__":
    for c in [ABC, DEF]:
        c().method()


