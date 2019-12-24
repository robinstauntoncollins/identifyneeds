from typing import Dict


class Characteristic():

    def __init__(
            self,
            uuid: str = None,
            text: str = None,
            category: str = None,
            condition_weightings: Dict[str, int] = None):
        self.uuid = uuid
        self.text = text
        self.category = category
        self.condition_weightings = condition_weightings

    def __str__(self):
        return f"{self.text} - Category: {self.category} - Associated Conditions: {self.condition_weightings.keys()}"

    def __repr__(self):
        return f"{self.text} - Category: {self.category} - Associated Conditions: {self.condition_weightings.keys()}"

    def add_points_to_condition(self, condition, points):
        if condition.name in self.condition_weightings.keys():
            points = points * self.condition_weightings[condition.name]
            condition.add_points(points)


class Condition():

    def __init__(
            self,
            uuid: str = None,
            name: str = None,
            points: int = 0
    ):
        self.uuid = uuid
        self.name = name
        self.points = points

    def __repr__(self):
        return f"{self.name} - {self.points}"

    def add_points(self, amount: int):
        self.points += amount
