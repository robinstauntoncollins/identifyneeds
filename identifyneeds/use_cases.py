from typing import Callable


class ListConditions():
    def __init__(self, repo: Callable):
        self.repo = repo

    def execute(self):
        return self.repo.get()


class UpdateConditions():

    def __init__(self, repo: Callable, characteristic: Callable, user_input_level: int):
        self.repo = repo
        self.characteristic = characteristic
        self.user_input_level = user_input_level

    def execute(self):
        self.characteristic.add_condition
        # conditions_to_fetch = characteristic.get_condition_names()
        # conditions = memrepo.get(filter_names=conditions_to_fetch)
        # for condition in conditions
        result = {'ok': True, 'status_code': 200}
        return result

