from typing import Dict


class Characteristic():

    def __init__(
            self,
            uuid: str = None,
            text: str = None,
            category: str = None,
            user_input_level: int = 0,
            condition_weightings: Dict[str, int] = None):
        self.uuid = uuid
        self.text = text
        self.category = category
        self._user_input_level = user_input_level
        self.condition_weightings = condition_weightings
        self.conditions = self._get_condition_names()

    def __str__(self):
        return f"{self.text} - Category: {self.category} - Associated Conditions: {self.condition_weightings.keys()}"

    def __repr__(self):
        return f"{self.text} - Category: {self.category} - Associated Conditions: {self.condition_weightings.keys()}"

    @property
    def user_input_level(self):
        return self._user_input_level

    @user_input_level.setter
    def user_input_level(self, value):
        if value not in [0, 1, 2]:
            raise ValueError(f"User Input value must be either '0', '1' or '2'. Received: {value}")
        else:
            self._user_input_level = value

    @classmethod
    def from_dict(cls, input_dict: dict):
        return cls(
            uuid=input_dict['uuid'],
            text=input_dict['text'],
            category=input_dict['category'],
            user_input_level=input_dict['user_input_level'],
            condition_weightings=input_dict['condition_weightings']
        )

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "text": self.text,
            "category": self.category,
            "user_input_level": self.user_input_level,
            "condition_weightings": self.condition_weightings
        }

    def add_points_to_condition(self, condition):
        if condition.name in self.condition_weightings.keys():
            points = self.user_input_level * self.condition_weightings[condition.name]
            condition.add_points(points)

    def _get_condition_names(self):
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
        self._points = points

    def __repr__(self):
        return f"{self.name} - {self._points}"

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        if value < 0:
            raise ValueError(f"Negative integers not allowed. Received {value}")
        else:
            self._points = value

    def add_points(self, amount: int):
        if amount < 0:
            raise ValueError(f"Expected a positive integer. Received '{amount}'")
        else:
            self._points += amount

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
