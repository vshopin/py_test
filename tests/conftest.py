import pytest
from random import randrange
from src.generators.player import Player


@pytest.fixture
def get_player_generator():
    return Player()


@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


def _calculate(a, b):
    try:
        return a + b
    except TypeError:
        pass


@pytest.fixture
def calculate():
    return _calculate


@pytest.fixture
def make_number():
    print("I am getting number")
    number = randrange(1, 1000, 5)
    yield number
    print(f"Number at home {number}")
