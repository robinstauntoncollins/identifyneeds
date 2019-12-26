from typing import List, Dict

from identifyneeds.entities import Condition


class MemRepo():

    def __init__(self, condition_dicts):
        self.conditions = {}
        self.put(condition_dicts)

    def get(self, filters: Dict = None):
        condition_objects = [Condition.from_dict(i) for i in self.conditions.values()]
        if not filters:
            return condition_objects

        if 'name' in filters.keys():
            return [item for item in condition_objects if item.name in filters['name']]

    def put(self, condition_dicts: List[dict]):
        self._check_types(condition_dicts)
        for cnd in condition_dicts:
            self.conditions[cnd['uuid']] = cnd

    def _check_types(self, conditions: List[dict]):
        if type(conditions) is not list:
            raise TypeError(f"Expected List of 'dicts'. Received: {type(conditions)}")
        for cnd in conditions:
            if type(cnd) is not dict:
                raise TypeError(f"Expected 'dict' got {type(cnd)}")
