from identifyneeds.entities import Condition


class MemRepo():

    def __init__(self, condition_dicts):
        self.conditions = condition_dicts

    def list(self):
        return [Condition.from_dict(i) for i in self.conditions]
