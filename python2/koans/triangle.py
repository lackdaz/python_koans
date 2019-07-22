#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
from IPython import embed

from math import fsum


def check_side_lengths(side, sides):
    remaining_sides = list(sides)
    remaining_sides.remove(side)
    return side > fsum(remaining_sides)


def triangle(a, b, c):
    sides = (a, b, c)
    if any(side <= 0 for side in sides):
        raise TriangleError("negative side")
    elif any(check_side_lengths(side, sides) for side in sides):
        raise TriangleError("weird side")
    else:
        unique_sides = len(set(sides))
        if unique_sides == 3:
            return 'scalene'
        elif unique_sides == 2:
            return 'isosceles'
        else:
            return 'equilateral'


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
