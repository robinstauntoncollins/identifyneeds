from unittest.mock import Mock

import pytest
from identifyneeds.entities import Characteristic, Condition


class TestCharacteristic():

    @pytest.fixture()
    def disruptive_char(self):
        return Characteristic(
            uuid=1,
            text="Disruptive in Class",
            category="Motivation and Concentration",
            condition_weightings={
                'Autism': 2,
                'Aspergers': 1,
                'Conduct Dis': 2,
                'OOD': 2,
                'Low IQ': 1,
                'ADHD': 2,
                'Tourettes': 2,
                'Giftedness': 1,
                'Abuse': 1
            }
        )

    @pytest.fixture()
    def mock_condition(self):
        mock = Mock()
        return mock

    def test_char_init(self):

        char = Characteristic(
            uuid='char-1',
            text="Disruptive in Class",
            category="Motivation and Concentration",
            condition_weightings={
                'Autism': 2,
                'Aspergers': 1,
                'Conduct Dis': 2,
                'OOD': 2,
                'Low IQ': 1,
                'ADHD': 2,
                'Tourettes': 2,
                'Giftedness': 1,
                'Abuse': 1
            }
        )
        assert char.uuid == 'char-1'
        assert char.text == "Disruptive in Class"
        assert char.category == "Motivation and Concentration"
        assert char.condition_weightings == {
            'Autism': 2,
            'Aspergers': 1,
            'Conduct Dis': 2,
            'OOD': 2,
            'Low IQ': 1,
            'ADHD': 2,
            'Tourettes': 2,
            'Giftedness': 1,
            'Abuse': 1
        }

    def test_add_points_to_condition(self, disruptive_char, mock_condition):
        condition = mock_condition
        condition.name = 'Autism'
        disruptive_char.add_points_to_condition(condition, 2)
        condition.add_points.assert_called_once_with(4)


class TestCondition():

    def test_condition_init(self):
        cnd = Condition(
            uuid='cnd-1',
            name="Autism",
            points=2
        )

        assert cnd.uuid == 'cnd-1'
        assert cnd.name == 'Autism'
        assert cnd.points == 2

    def test_add_points(self):
        cnd = Condition()
        cnd.add_points(5)
        assert cnd.points == 5
