'''
489. Robot Room Cleaner
https://leetcode.com/problems/robot-room-cleaner/
'''
from typing import List

from test_tool import assert_value


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Command:
    def __init__(self, robot):
        self._robot = robot

    def move_forward(self):
        return self._robot.move()

    def move_backward(self):
        self._robot.turnLeft()
        self._robot.turnLeft()
        return self._robot.move()

    def move_left(self):
        self._robot.turnLeft()
        return self._robot.move()

    def move_right(self):
        self._robot.turnRight()
        return self._robot.move()

    def turn_over(self):
        self._robot.turnLeft()
        self._robot.turnLeft()

    def turn_left(self):
        self._robot.turnLeft()

    def turn_right(self):
        self._robot.turnRight()

    def clean(self):
        self._robot.clean()


class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        robot = Command(robot)

        def dfs(y, x, dy, dx):
            robot.clean()
            dirs = {(1, 0), (0, 1), (-1, 0), (0, -1)}
            for df in dirs:
                yf, xf = y + df[0], x + df[1]
                if (yf, xf) in seen:
                    continue
                seen.add((yf, xf))
                # move in the same direction as dy, dx
                if df[0] == dy and df[1] == dx:
                    if robot.move_forward():
                        dfs(yf, xf, df[0], df[1])
                        robot.turn_over()
                        robot.move_forward()
                        robot.turn_over()
                # move in the direction opposite to dy, dx
                elif df[0] == -dy and df[1] == -dx:
                    if robot.move_backward():
                        dfs(yf, xf, df[0], df[1])
                        robot.turn_over()
                        robot.move_forward()
                    else:
                        robot.turn_over()
                # rotate dy, dx to the right by 90 degrees and move
                elif df[0] * dx - df[1] * dy == -1:
                    if robot.move_right():
                        dfs(yf, xf, df[0], df[1])
                        robot.turn_over()
                        robot.move_forward()
                        robot.turn_right()
                    else:
                        robot.turn_left()
                # rotate dy, dx to the left by 90 degrees and move
                else:
                    if robot.move_left():
                        dfs(yf, xf, df[0], df[1])
                        robot.turn_over()
                        robot.move_forward()
                        robot.turn_left()
                    else:
                        robot.turn_right()

        seen = set([(0, 0)])
        dfs(0, 0, 1, 0)