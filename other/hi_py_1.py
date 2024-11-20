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


def xyz():
    print("xyz function called")


xyz.__name__ = 'XYZZZ'

if __name__ == "__main__":
    for c in [ABC, DEF]:
        c().method()

    print(ABC.__name__)
    print(xyz.__name__)
