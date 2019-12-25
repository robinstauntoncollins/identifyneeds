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

    @classmethod
    def from_dict(cls, input_dict: dict):
        return cls(
            uuid=input_dict['uuid'],
            text=input_dict['text'],
            category=input_dict['category'],
            condition_weightings=input_dict['condition_weightings']
        )

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "text": self.text,
            "category": self.category,
            "condition_weightings": self.condition_weightings
        }

    def add_points_to_condition(self, condition, points):
        if condition.name in self.condition_weightings.keys():
            points = points * self.condition_weightings[condition.name]
            condition.add_points(points)

    def get_condition_names(self):
        return list(self.condition_weightings.keys())


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

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def add_points(self, amount: int):
        self.points += amount

    @classmethod
    def from_dict(cls, input_dict: dict):
        return cls(
            uuid=input_dict['uuid'],
            name=input_dict['name'],
            points=input_dict.get('points', 0)
        )

    def to_dict(self):
        return {
            'uuid': self.uuid,
            'name': self.name,
            'points': self.points
        }
