class myclass:

    species = "human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = myclass("Blu", 10)
woo = myclass("Woo", 15)


print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.__class__.species))

print("{} is {}".format( blu.name, blu.age))
print("{} is {}".format( woo.name, woo.age))