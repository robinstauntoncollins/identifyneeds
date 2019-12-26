from typing import Callable


class ListConditions():
    def __init__(self, repo: Callable):
        self.repo = repo

    def execute(self):
        return self.repo.get()


class UpdateConditions():

    def __init__(self, repo: Callable, characteristic: Callable):
        self.repo = repo
        self.characteristic = characteristic

    def execute(self):
        conditions_to_fetch = self.characteristic.get_condition_names()
        conditions = self.repo.get(filters={'name': conditions_to_fetch})
        for condition in conditions:
            self.characteristic.add_points_to_condition(condition)
        condition_dicts = [condition.to_dict() for condition in conditions]
        self.repo.put(condition_dicts)
