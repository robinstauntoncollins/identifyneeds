import pytest

from identifyneeds.entities import Condition, Characteristic
from identifyneeds.repository import MemRepo
from identifyneeds.use_cases import ListConditions, UpdateConditions


class TestListConditionsUseCase():

    def test_list_conditions_use_case(self):
        repo = MemRepo([])
        uc = ListConditions(repo)
        result = uc.execute()
        assert result == []


class TestUpdateConditionsUseCase():

    @pytest.fixture()
    def memrepo(self):
        repo = MemRepo([
            {
                'uuid': 'cnd-1',
                'name': 'Autism',
            },
            {
                'uuid': 'cnd-2',
                'name': 'Aspergers'
            },
            {
                'uuid': 'cnd-3',
                'name': 'Anxiety'
            }
        ])
        return repo

    @pytest.fixture()
    def characteristic(self):
        char = Characteristic.from_dict({
            'uuid': 'char-1',
            'text': 'Disruptive',
            'category': 'Motivation and Focus',
            'condition_weightings': {
                'Anxiety': 2,
                'Autism': 1
            }
        })
        return char

    def test_update_conditions_use_case(self, characteristic, memrepo):
        result = UpdateConditions(memrepo, characteristic).execute()
        assert result['ok'] is True
        assert result['status_code'] == 200
        affected_conditions = memrepo.get(filter_names=['Anxiety', 'Autism'])
        assert affected_conditions[0].points == 4
        assert affected_conditions[1].points == 2
