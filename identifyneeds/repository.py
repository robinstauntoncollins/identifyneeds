from typing import Optional, List, Union

from identifyneeds.entities import Condition


class MemRepo():

    def __init__(self, condition_dicts):
        self.conditions = condition_dicts

    def get(self, filter_names: Optional[Union[str, List[str]]] = None):
        condition_objects = [Condition.from_dict(i) for i in self.conditions]
        if not filter_names:
            return condition_objects
        else:
            return [item for item in condition_objects if item.name in filter_names]
