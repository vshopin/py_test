import pytest

from src.base_classes.response import Response
from src.schemas.user import User


def test_getting_users_list(get_users):
    test_obj = Response(get_users)
    test_obj.assert_status_code(200).validate(User)


@pytest.mark.production
@pytest.mark.skip
def test_another():
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'b', 'bb')
])
def test_calculation(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result
