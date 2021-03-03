import pytest
from Dev.DogShelter import DogShelter

pytestmark = [pytest.mark.regression]


@pytest.mark.smoke
def test_valid_values():
    assert DogShelter.get_food_quantity(5, 3, 7, 17) == 367


def test_dog_count_max():
    assert DogShelter.get_food_quantity(15, 14, 1, 17) == 535


def test_dog_count_too_high():
    error_text = ''
    try:
        DogShelter.get_food_quantity(15, 15, 1, 17)
    except ValueError as e:
        error_text = str(e)
    assert 'maximum dog count the shelter can hold' in error_text


def test_dog_counts_are_zero():
    assert DogShelter.get_food_quantity(0, 0, 0, 10) == -10


def test_invalid_small_count():
    error_text = ''
    try:
        DogShelter.get_food_quantity(-1, 3, 7, 17)
    except ValueError as e:
        error_text = str(e)
    assert error_text == 'small dog count must be 0 or greater'


def test_invalid_medium_count():
    error_text = ''
    try:
        DogShelter.get_food_quantity(5, -1, 7, 17)
    except ValueError as e:
        error_text = str(e)
    assert error_text == 'medium dog count must be 0 or greater'


def test_invalid_large_count():
    error_text = ''
    try:
        DogShelter.get_food_quantity(5, 3, -1, 17)
    except ValueError as e:
        error_text = str(e)
    assert error_text == 'large dog count must be 0 or greater'


def test_invalid_left_over_count():
    error_text = ''
    try:
        DogShelter.get_food_quantity(5, 3, 7, -1)
    except ValueError as e:
        error_text = str(e)
    assert error_text == 'left over food must be 0 or greater'


def test_left_over_count_is_enough():
    assert DogShelter.get_food_quantity(5, 3, 7, 384) == 0


def test_left_over_count_is_more_than_enough():
    assert DogShelter.get_food_quantity(5, 3, 7, 400) == -16


def test_leftover_count_is_zero():
    assert DogShelter.get_food_quantity(5, 3, 7, 0) == 384
