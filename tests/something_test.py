import requests
from configuration import SERVICE_URL
from src.base_classes.response import Response
from src.schemas.user import User


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_obj = Response(response)
    test_obj.assert_status_code(200).validate(User)

# z = {'meta': {'pagination': {'total': 2892, 'pages': 290, 'page': 1, 'limit': 10,
#                              'links': {'previous': None, 'current': 'https://gorest.co.in/public/v1/users?page=1',
#                                        'next': 'https://gorest.co.in/public/v1/users?page=2'}}},
#                                        'data': [
#     {'id': 1217909, 'name': 'Lalita Chattopadhyay', 'email': 'lalita_chattopadhyay@morissette.example',
#      'gender': 'male', 'status': 'active'},
#     {'id': 1203756, 'name': 'Avani Ahuja', 'email': 'ahuja_avani@adams-fisher.example', 'gender': 'female',
#      'status': 'active'},
#     {'id': 1203755, 'name': 'Adhiraj Nayar', 'email': 'adhiraj_nayar@batz.example', 'gender': 'female',
#      'status': 'inactive'},
#     {'id': 1203751, 'name': 'Rukmin Bhattathiri', 'email': 'bhattathiri_rukmin@vandervort.example', 'gender': 'male',
#      'status': 'inactive'},
#     {'id': 1203750, 'name': 'Dhanadeepa Malik', 'email': 'malik_dhanadeepa@daugherty.example', 'gender': 'female',
#      'status': 'inactive'},
#     {'id': 1203746, 'name': 'Giriraaj Kakkar LLD', 'email': 'giriraaj_lld_kakkar@cassin.example', 'gender': 'female',
#      'status': 'active'},
#     {'id': 1203745, 'name': 'Kanaka Shah DO', 'email': 'kanaka_shah_do@hilll.example', 'gender': 'male',
#      'status': 'inactive'},
#     {'id': 1203744, 'name': 'Tanushri Shah VM', 'email': 'vm_shah_tanushri@bradtke.example', 'gender': 'male',
#      'status': 'active'},
#     {'id': 1203742, 'name': 'Kirti Embranthiri', 'email': 'kirti_embranthiri@gibson.example', 'gender': 'male',
#      'status': 'active'},
#     {'id': 1203741, 'name': 'Dayamayee Nehru CPA', 'email': 'dayamayee_cpa_nehru@kutch.example', 'gender': 'female',
#      'status': 'inactive'}]}
