import pytest

from src.base_classes.response import Response
from src.schemas.user import User


def test_getting_users_list(get_users):
    test_obj = Response(get_users)
    test_obj.assert_status_code(200).validate(User)


@pytest.mark.development
@pytest.mark.production
@pytest.mark.skip
def test_another():
    """
    In that test we are try to check that 1 is equal 2
    """
    assert 1 == 2


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'b', 'bb')
])
def test_calculation(first_value, second_value, result, calculate):
    """
    In that test we are testing calculating with different values(Valid and invalid)
    """
    assert calculate(first_value, second_value) == result
