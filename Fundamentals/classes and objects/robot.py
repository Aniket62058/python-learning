class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0, 0]
        print("My name is ", self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print("New Position : ", self.position)
