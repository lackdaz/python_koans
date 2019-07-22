from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from runner.koan import *

import re

def count_lines(self, file_name):
    try:
        f = open(file_name)
        try:
            return len(f.readlines())
        finally:
            f.close()
    except IOError:
        # should never happen
        self.fail()

def find_line(self, file_name):
    try:
        f = open(file_name)
        try:
            for line in f.readlines():
                match = re.search('e', line)
                if match:
                    return line
        finally:
            f.close()
    except IOError:
        # should never happen
        self.fail()
