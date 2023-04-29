from src.base_classes.response import Response
from src.schemas.user import User


def test_getting_users_list(get_users):
    test_obj = Response(get_users)
    test_obj.assert_status_code(200).validate(User)
