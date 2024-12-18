# tests/main_bdd_test.feature
import pytest
from pytest_bdd import scenario, given, then
from lab_python_oop.Box import Box


@pytest.fixture
def figure():
    return None


@scenario("main_bdd_test.feature", "Incorrectly launching")
def test_is_input():
    pass


@given("the correct value - height = 5")
def test_user_input():
    figure.box = Box(5)


@then("the user should see an area of the figure = 25")
def test_box_square():
    assert figure.box.square() == 25
