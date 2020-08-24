# shapes.py
from __future__ import print_function

import winsound
import time
import sys

""" A colletion of functions
for printing basic shapes. 
"""

CHAR = '*'

def rectangle(height, width):
    """ Prints a rectange. """
    for row in range(height):
        for col in range(width):
            print(CHAR, end = '')
        print()

def square(side):
    """Prints a square."""
    rectangle(side, side)

def triangle(height):
    """ Prints a right triangle. """
    for row in range(height):
        for col in range(0, row + 1):
            print(CHAR, end = '')
        print()

keep = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'}

def normalize(s):
    """
    convert s to normalized string.
    :param s:
    :return:
    """
    return ''.join(c for c in s.lower() if c in keep)

d = {'a': 2, 'ago': 1, 'galaxy': 1, 'time': 1, 'far': 2, 'away': 1, 'in': 1, 'long': 1}
lst = []

for k in d:
    pair = (d[k], k)
    lst.append(pair)

print(lst)

i = 1
for count, word in lst:
    print('%2s. %4s %8s' % (i, count, word))
    i += 1

frequency = 2500
duration = 100

#winsound.Beep(frequency, duration)

def countdown(t):
    while t:
        min, sec = divmod(t, 60)
        print("{:02d}:{:02d} left".format(min, sec))
        time.sleep(1)
        t -= 1

countdown(80)
