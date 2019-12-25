import pytest

from identifyneeds.entities import Condition
from identifyneeds.repository import MemRepo


@pytest.fixture()
def condition_dicts():
    return [
        {
            'uuid': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
            'name': "Autism",
            'points': 39,
        },
        {
            'uuid': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
            'name': "Aspergers",
            'points': 66,
        },
        {
            'uuid': '913694c6-435a-4366-ba0d-da5334a611b2',
            'name': "ADHD",
            'points': 60,
        },
        {
            'uuid': 'eed76e77-55c1-41ce-985d-ca49bf6c0585',
            'name': "Anxiety",
            'points': 48,
        }
    ]


class TestMemRepo():

    def test_init_memrepo(self, condition_dicts):
        repo = MemRepo(condition_dicts)
        conditions = [Condition.from_dict(item_dict) for item_dict in condition_dicts]
        assert repo.get() == conditions

    cnd_by_name_test_data = [
        ("Autism", ['Autism']),
        ("Aspergers", ['Aspergers']),
        ("ADHD", ['ADHD']),
        ("Anxiety", ['Anxiety']),
        (['Autism', 'Aspergers'], ['Autism', 'Aspergers'])
    ]

    @pytest.mark.parametrize("names,expected", cnd_by_name_test_data)
    def test_get_condition_by_name(self, names, expected, condition_dicts):
        repo = MemRepo(condition_dicts)
        results = repo.get(filter_names=names)
        result_names = [cnd.name for cnd in results]
        assert result_names == expected
