# test_with_pytest.py
import math
import pytest
from lab_python_oop.Box import Box
from lab_python_oop.Shape import Shape
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Cyrcle import Cyrcle

# Regular const
"""
def test_always_passes():
    assert True

def test_always_fails():
    assert False
"""


@pytest.fixture
def box_obj():
    return Box(5)


# Box
def test_box_square(box_obj):
    assert box_obj.square() == 25


# Cyrcle
def test_cyrcle_square(mocker):
    cyrc = mocker.Mock(spec=Cyrcle)
    cyrc.r = 5
    cyrc.square.returned_value = math.pi * (cyrc.r**2)
    assert Cyrcle(5).square() == cyrc.square.returned_value


# Rectangle
def test_rect_square():
    assert Rectangle(2, 5).square() == 10
