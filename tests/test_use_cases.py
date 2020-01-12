import pytest

from unittest.mock import Mock

from identifyneeds.entities import Characteristic
from identifyneeds.repository import MemRepo
from identifyneeds.use_cases import ListConditions, UpdateCondition, GetMostLikelyConditions


@pytest.fixture()
def memrepo():
    repo = MemRepo([
        {
            'uuid': 'cnd-1',
            'name': 'Autism',
        },
        {
            'uuid': 'cnd-2',
            'name': 'Aspergers',
        },
        {
            'uuid': 'cnd-3',
            'name': 'Anxiety',
        }
    ])
    return repo


class TestListConditionsUseCase():

    def test_list_conditions_use_case(self):
        repo = Mock()
        repo.get.return_value = []
        uc = ListConditions(repo)
        result = uc.execute()
        assert result == []
        repo.get.assert_called_with()


class TestUpdateConditionUseCase():

    @pytest.fixture()
    def characteristic(self):
        char = Characteristic.from_dict({
            'uuid': 'char-1',
            'text': 'Disruptive',
            'category': 'Motivation and Focus',
            'user_input_level': 2,
            'condition_weightings': {
                'Anxiety': 2,
                'Autism': 1
            }
        })
        return char

    def test_update_conditions_use_case(self, characteristic, memrepo):
        """Given a characteristic. Update conditions will have the characteristic
        calculate the points and update the points for each of its conditions"""
        update_condition = UpdateCondition(memrepo)
        update_condition.execute(characteristic)
        affected_conditions = memrepo.get(filters={'name': ['Anxiety', 'Autism']})
        cnd_dict = {}
        for cnd in affected_conditions:
            cnd_dict[cnd.name] = cnd
        assert cnd_dict['Anxiety'].points == 4
        assert cnd_dict['Autism'].points == 2


class TestGetMostLikelyConditions():

    @pytest.fixture()
    def memrepo(self):
        return MemRepo([
            {
                'uuid': 'cnd-1',
                'name': 'Autism',
                'points': 5
            },
            {
                'uuid': 'cnd-2',
                'name': 'Aspergers',
                'points': 4
            },
            {
                'uuid': 'cnd-3',
                'name': 'Anxiety',
                'points': 2
            }
        ])

    def test_get_most_likely_condition(self, memrepo):
        uc = GetMostLikelyConditions(memrepo)
        results = uc.execute()
        result = [cnd.to_dict() for cnd in results]
        assert result == [{
            'uuid': 'cnd-1',
            'name': 'Autism',
            'points': 5
        }]

    @pytest.fixture()
    def memrepo_with_two_highest(self):
        return MemRepo([
            {
                'uuid': 'cnd-1',
                'name': 'Anxiety',
                'points': 5
            },
            {
                'uuid': 'cnd-2',
                'name': 'Aspergers',
                'points': 5
            },
            {
                'uuid': 'cnd-3',
                'name': 'ADHD',
                'points': 4
            }
        ])

    def test_get_all_most_likely(self, memrepo_with_two_highest):
        uc = GetMostLikelyConditions(memrepo_with_two_highest)
        result = uc.execute()
        result = [cnd.to_dict() for cnd in result]
        assert result == [
            {
                'uuid': 'cnd-1',
                'name': 'Anxiety',
                'points': 5
            },
            {
                'uuid': 'cnd-2',
                'name': 'Aspergers',
                'points': 5
            }
        ]
