from faker import Faker

"""
Пример описания билдера для локализации.
Example of declaration for localization builder.
"""


class PlayerLocalization:
    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {
            "nickname": self.fake.first_name()
        }

    def set_number(self, number=11):
        self.result['number'] = number
        return self

    def build(self):
        """
        Возвращает наш обьект в виде JSON.
        Returns object as JSON.
        """
        return self.result
