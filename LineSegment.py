#!/usr/bin/python3

from __future__ import division # solve python2 division
import math

class Point():
    """
    Point in 2D plan
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

class LineSegment():
    """
    Line Segment in 2D plan
    """

    def __init__(self, p1, p2):
        """
        Init the `LineSegment`
        p1: Extreme Point 1
        p2: Extreme Point 2
        """
        if p1 == p2:
            raise ValueError('This is not a `LineSegment`, is a Point!')

        self.p1 = p1
        self.p2 = p2

        try:
            self.slope = (p2.y - p1.y)/(p2.x - p1.x)
        except ZeroDivisionError:
            self.slope = None

        self.lengh = math.hypot((p2.x - p1.x), (p2.y - p1.y))

    def is_parallel(self, ls):
        """
        Check if this `LineSegment` is parallel with ls
        ls: One `LineSegment`
        """
        if self.slope is None:
            return ls.slope is None
        return self.slope == ls.slope

    def is_perpendicular(self, ls):
        """
        Check if this `LineSegment` is perpendicular with ls
        ls: One `LineSegment`
        """
        if self.slope is None:
            return ls.slope == 0

        if self.slope == 0:
            return ls.slope is None

        return self.slope * ls.slope == (-1)
