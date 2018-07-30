# -----------------------------------------------------------------------------
# Name:        robottest.py
# Purpose:     Test the Robot class
#
# Author:      Rula Khayrallah
# -----------------------------------------------------------------------------
"""
Simple tests for the Robot and UnderwaterRobot classes

Create 4 robots and move them around the maze.
The expected print output is as follows:
WALL-E is a yellow robot lost in the maze.
my_robot's battery: 13
my_robot's battery: 19
your_robot's battery: 17
your_robot > my_robot: False
my_robot > your_robot: True
Nemo is a gold robot diving under water.
Nemo's depth: 14
Nemo's battery: 10
Bubbles is a purple robot diving under water.
Bubbles > Nemo: True
Bubbles's battery: 20
Nemo's battery: 19
"""

from robot import Robot
from robot import UnderwaterRobot


def main():
    # Test the Robot class
    my_robot = Robot('WALL-E', 'yellow')

    print(my_robot)  # WALL-E is a yellow robot lost in the maze.

    my_robot.show()

    my_robot.one_step_right()
    my_robot.show()

    my_robot.one_step_back()
    my_robot.show()

    my_robot.one_step_right()
    my_robot.show()

    my_robot.one_step_left()
    my_robot.show()

    my_robot.one_step_forward()
    my_robot.show()

    my_robot.forward(4)

    my_robot.show()
    print("my_robot's battery: {}".format(my_robot.battery))  # 13

    my_robot.right(18)

    my_robot.show()
    my_robot.backward(6)
    my_robot.show()

    my_robot.recharge().backward(2)

    my_robot.show()

    your_robot = Robot('Eve', 'cyan', 2, 5)

    your_robot.show()

    your_robot.left(5)
    your_robot.show()
    print("my_robot's battery: {}".format(my_robot.battery))  # 19
    print("your_robot's battery: {}".format(your_robot.battery))  # 17
    print("your_robot > my_robot: {}".format(your_robot > my_robot))  # False
    print("my_robot > your_robot: {}".format(my_robot > your_robot))  # True

    # Test the UnderwaterRobot class
    nemo = UnderwaterRobot('Nemo', 'gold', 4)
    print(nemo)  # Nemo is a gold robot diving under water.
    nemo.show()
    nemo.forward(8)
    nemo.show()
    nemo.backward(1)
    nemo.show()
    nemo.right(5)
    nemo.show()
    nemo.dive(10)
    print("Nemo's depth: {}".format(nemo.depth))  # 14
    nemo.show()
    print("Nemo's battery: {}".format(nemo.battery))  # 10
    nemo.recharge()
    nemo.left(6)
    nemo.show()

    bubbles = UnderwaterRobot('Bubbles', 'purple', 7, 5, 3)
    print(bubbles)  # Bubbles is a purple robot diving under water.
    bubbles.show()
    print("Bubbles > Nemo: {}".format(bubbles > nemo))  # True
    print("Bubbles's battery: {}".format(bubbles.battery))  # 20
    print("Nemo's battery: {}".format(nemo.battery))  # 19


if __name__ == '__main__':
    main()
