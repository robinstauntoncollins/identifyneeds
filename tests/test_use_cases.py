from identifyneeds.entities import Condition
from identifyneeds.repository import MemRepo
from identifyneeds.use_cases import ListConditions


class TestListConditionsUseCase():

    def test_list_conditions_use_case(self):
        repo = MemRepo([])
        uc = ListConditions(repo)
        result = uc.execute()
        assert result == []


class TestUpdateConditionsUseCase():

    def test_update_conditions_use_case(self, characteristic, memRepo):
        conditions_to_fetch = characteristic.get_condition_names()
        conditions = [memRepo.get(filter_name=condition) for condition in conditions_to_fetch]
        for 
        