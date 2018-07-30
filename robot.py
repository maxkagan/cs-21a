# -----------------------------------------------------------------------------
# Name:   robot.py
# Purpose: To create cute little robots and have them wander in a maze forever
#
# Author: Max Kagan
# Date: 7/22
# -----------------------------------------------------------------------------

"""
Module to describe and control robot objects in a maze. A fun game for
children of all ages
"""
import tkinter


class Robot(object):
    """
    Defines a robot to be placed in the maze

    Arguments:
    list the arguments here (__init__'s arguments)
    :argument name Sets robot name
    :argument color Sets robot Color
    :argument row Positions robot in desired row on init
    :argument column Positions robot in desired column on init

    Attributes:
    list ALL the attributes here (ALL the instance variables)
    :var name Sets robot name
    :var color Sets robot Color
    :var row robots row position
    :var column robots column position
    :var battery Representation of total charge of robot. One charge allows
    robot to move one space

    """

    # class variable used by the show method
    unit_size = 60

    # Class variable describing the maze
    # False represents an obstacle, True represents open space
    maze = [[True, True, False, True, True, True, False, True, True, True],
            [True, True, False, True, True, True, False, True, True, True],
            [True, False, True, True, True, True, False, True, True, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, False, False, False, False, True, True, True, True, True],
            [True, True, False, True, True, True, True, True, False, True],
            [True, False, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True]]

    maze_size = len(maze)
    # class variable to represent a full charge
    # A robot with a fully charged battery can take up to 20 steps
    full = 20

    def __init__(self, name, color, row=0, column=0):
        self.name = name
        self.color = color
        self.row = row
        self.column = column
        self.battery = Robot.full

    def __str__(self):
        return '{} is a {} robot lost in the maze'.format(self.name,
                                                          self.color)

    def __gt__(self, other):
        if self.battery > other.battery:
            return True
        return False

    def recharge(self):
        """
        Sets the robots battery level to its maximum charge
        """
        self.battery = Robot.full
        return self

    def one_step_forward(self):
        """
        Method used to move the robot downward in the grid. Checks to ensure
        there is no wall or boundary in the robots path before moving to the
        desired position

        :returns True if robot can and did move to down square
        :returns False if robot is unable to move due to battery level,
        boundary, or obstacle.
        """
        if self.row + 1 <= Robot.maze_size - 1:
            if Robot.maze[self.row + 1][self.column]:
                if self.battery > 0:
                    self.row += 1
                    self.battery -= 1
                    return True
        return False

    def one_step_back(self):
        """
        Method used to move the robot upward in the grid. Checks to ensure
        there is no wall or boundary in the robots path before moving to the
        desired position

        :returns True if robot can and did move to upward square
        :returns False if robot is unable to move due to battery level,
        boundary, or obstacle.
        """
        if self.row - 1 > -1:
            if Robot.maze[self.row - 1][self.column]:
                if self.battery > 0:
                    self.row -= 1
                    self.battery -= 1
                    return True
        return False

    def one_step_right(self):
        """
        Method used to move the robot right in the grid. Checks to ensure
        there is no wall or boundary in the robots path before moving to the
        desired position

        :returns True if robot can and did move to right square
        :returns False if robot is unable to move due to battery level,
        boundary, or obstacle.
        """
        if self.column + 1 <= Robot.maze_size - 1:
            if Robot.maze[self.row][self.column + 1]:
                if self.battery > 0:
                    self.column += 1
                    self.battery -= 1
                    return True
        return False

    def one_step_left(self):
        """
        Method used to move the robot left in the grid. Checks to ensure
        there is no wall or boundary in the robots path before moving to the
        desired position

        :returns True if robot can and did move to left square
        :returns False if robot is unable to move due to battery level,
        boundary, or obstacle.
        """
        if self.column - 1 > -1:
            if Robot.maze[self.row][self.column - 1]:
                if self.battery > 0:
                    self.column -= 1
                    self.battery -= 1
                    return True
        return False

    def forward(self, steps):
        """
        Method used to move the robot downward in the grid a desired number
        of times. Checks to ensure there is no wall or boundary in the robots
        path before moving to the desired position
        """
        for i in range(0, steps):
            self.one_step_forward()

    def backward(self, steps):
        """
        Method used to move the robot upward in the grid a desired number
        of times. Checks to ensure there is no wall or boundary in the robots
        path before moving to the desired position
        """
        for i in range(0, steps):
            self.one_step_back()

    def right(self, steps):
        """
        Method used to move the robot right in the grid a desired number
        of times. Checks to ensure there is no wall or boundary in the robots
        path before moving to the desired position
        """
        for i in range(0, steps):
            self.one_step_right()

    def left(self, steps):
        """
        Method used to move the robot left in the grid a desired number
        of times. Checks to ensure there is no wall or boundary in the robots
        path before moving to the desired position
        """
        for i in range(0, steps):
            self.one_step_left()

    # The method below has been written for you
    # You can use it when testing your class

    def show(self):
        """
        Draw a graphical representation of the robot in the maze.

        The robot's position and color are shown.
        The color is assumed to be one of the colors recognized by tkinter
        (https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm)
        If the robot's battery is empty, the robot is shown in a
        horizontal position. Otherwise the robot is shown in an upright
        position.
        The obstacles in the maze are shown in red.

        Parameter: None
        Return: None
        """
        root = tkinter.Tk()
        root.title(self.name + ' in the Maze')
        canvas = tkinter.Canvas(root, background='light green',
                                width=self.unit_size * self.maze_size,
                                height=self.unit_size * self.maze_size)
        canvas.grid()

        # draw a representation of the robot in the maze
        if self.battery:
            upper_x = self.column * self.unit_size + self.unit_size / 4
            upper_y = self.row * self.unit_size
            lower_x = upper_x + self.unit_size / 2
            lower_y = upper_y + self.unit_size
            eye_x = lower_x - 3 * self.unit_size / 20
            eye_y = upper_y + self.unit_size / 10

        else:  # the robot ran out of battery
            upper_x = self.column * self.unit_size
            upper_y = self.row * self.unit_size + self.unit_size / 2
            lower_x = upper_x + self.unit_size
            lower_y = upper_y + self.unit_size / 2
            eye_x = lower_x - 9 * self.unit_size / 10
            eye_y = lower_y - 3 * self.unit_size / 20

        rectangle = canvas.create_rectangle(upper_x,
                                            upper_y,
                                            lower_x,
                                            lower_y,
                                            fill=self.color)
        # draw the robot's eyes
        canvas.create_oval(upper_x + self.unit_size / 10,
                           upper_y + self.unit_size / 10,
                           upper_x + 3 * self.unit_size / 20,
                           upper_y + 3 * self.unit_size / 20,
                           fill='black')
        canvas.create_oval(eye_x,
                           eye_y,
                           eye_x + self.unit_size / 20,
                           eye_y + self.unit_size / 20,
                           fill='black')
        # draw the obstacles in the maze
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                if not self.maze[row][col]:
                    canvas.create_rectangle(col * self.unit_size,
                                            row * self.unit_size,
                                            (col + 1) * self.unit_size,
                                            (row + 1) * self.unit_size,
                                            fill='red')
        for row in range(self.maze_size):
            canvas.create_line(0,
                               row * self.unit_size,
                               self.maze_size * self.unit_size,
                               row * self.unit_size)
        for col in range(self.maze_size):
            canvas.create_line(col * self.unit_size,
                               0,
                               col * self.unit_size,
                               self.maze_size * self.unit_size)
        root.mainloop()


# Enter you UnderwaterRobot Class definition below
class UnderwaterRobot(Robot):
    """
    Defines an underwater robot to be placed in the maze

    Arguments:
    list the arguments here (__init__'s arguments)
    :argument name String Sets robot name
    :argument color String Sets robot Color
    :argument row int Positions robot in desired row on init
    :argument column int Positions robot in desired column on init
    :argument depth int Sets robot depth

    Attributes:
    list ALL the attributes here (ALL the instance variables)
    :var name String Sets robot name
    :var color String Sets robot Color
    :var row int robots row position
    :var column int robots column position
    :var battery int Representation of total charge of robot. One charge allows
    robot to move one space
    :var depth represents robots current depth underwater

    """

    def __init__(self, name, color, depth=0, row=0, column=0):
        self.name = name
        self.color = color
        self.row = row
        self.column = column
        self.depth = depth
        self.battery = Robot.full

    def __str__(self):
        return '{} is a {} robot diving under water'.format(self.name,
                                                            self.color)

    def dive(self, distance):
        """
        Representation of the robot diving deeper into the water
        :param distance: The desired change in depth
        :return: the updated object
        """
        if (self.depth + distance) < 0:
            self.depth = 0
            return self
        else:
            self.depth += distance
            return self
