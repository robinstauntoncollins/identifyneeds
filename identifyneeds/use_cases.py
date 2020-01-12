from typing import Callable


class ListConditions():
    def __init__(self, repo: Callable):
        self.repo = repo

    def execute(self):
        return self.repo.get()


class UpdateCondition():

    def __init__(self, repo: Callable):
        self.repo = repo

    def execute(self, characteristic: Callable):
        conditions = self.repo.get(filters={'name': characteristic.conditions})
        for condition in conditions:
            characteristic.add_points_to_condition(condition)
        condition_dicts = [condition.to_dict() for condition in conditions]
        self.repo.put(condition_dicts)


class GetMostLikelyConditions():

    def __init__(self, repo: Callable):
        self.repo = repo

    def execute(self):
        conditions = self.repo.get()
        highest = self._get_most_likely_conditions(conditions)
        return highest

    def _get_most_likely_conditions(self, conditions_list):
        highest_score = self._get_highest_condition_score(conditions_list)
        return [cnd for cnd in conditions_list if cnd.points >= highest_score]

    def _get_highest_condition_score(self, conditions_list):
        highest_score = 0
        for condition in conditions_list:
            if condition.points > highest_score:
                highest_score = condition.points
            else:
                continue
        return highest_score
