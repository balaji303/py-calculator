#This is the file used to test calculator.py

from calculator import *

def test_add():
    assert(Calculator.add(1,2) == 3)
    assert(Calculator.add(-1,2) == 1)
    assert(Calculator.add(1,-2) == -1)
    assert(Calculator.add(1.6,2.4) == 4)
    assert(Calculator.add(1,0) == 1)

def test_sub():
    assert(Calculator.sub(3,1) == 2)
    assert(Calculator.sub(-1,2) == -3)
    assert(Calculator.sub(1,-2) == 3)
    assert(Calculator.sub(2.6,2.6) == 0)
    assert(Calculator.sub(1,0) == 1)

def test_mul():
    assert(Calculator.mul(3,2) == 6)
    assert(Calculator.mul(-1,5) == -5)
    assert(Calculator.mul(2,-2) == -4)
    assert(Calculator.mul(4,2.0) == 8.0)
    assert(Calculator.mul(1,0) == 0)

def test_div():
    assert(Calculator.div(6,3) == 2)
    assert(Calculator.div(-4,2) == -2)
    assert(Calculator.div(-9,-3) == 3)
    assert(Calculator.div(2,0) == 0)
    assert(Calculator.div(5,5) == 1)    