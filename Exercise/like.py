class person:
    def __init__(self, name):
        self.name = name
        self.likes = []

    def like(self, thing):
        self.likes.append(thing)
if __name__ == "__main__":
    alice = person("Alice")
    alice.like("chocolate")
    alice.like("cats")
    print(f"{alice.name} likes: {', '.join(alice.likes)}")
    bob = person("Bob")
    bob.like("pizza")
    print(f"{bob.name} likes: {', '.join(bob.likes)}")
    