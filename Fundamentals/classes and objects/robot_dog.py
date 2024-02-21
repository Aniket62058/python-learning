from robot import Robot


class Robot_Dog(Robot):
    def make_noise(self):
        print("Woof Woof!")

    def walk(self, x):  # Overriding walk method
        super().walk(x)  # For calling parent walk()
        self.position[1] = self.position[1] + x
        print("New Position : ", self.position)


# Main program
my_robot = Robot_Dog("Sheru")
my_robot.make_noise()
my_robot.walk(10)
