from identifyneeds.entities import Condition


class MemRepo():

    def __init__(self, condition_dicts):
        self.conditions = condition_dicts

    def get(self, filter_name=None):
        condition_objects = [Condition.from_dict(i) for i in self.conditions]
        if not filter_name:
            return condition_objects
        else:
            return [item for item in condition_objects if item.name == filter_name]
