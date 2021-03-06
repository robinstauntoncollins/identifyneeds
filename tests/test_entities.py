import uuid
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
            user_input_level=2,
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
            user_input_level=2,
            condition_weightings={
                'Autism': 2,
                'Aspergers': 1,
                'Conduct Dis': 2,
                'ODD': 2,
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
        assert char.user_input_level == 2
        assert char.condition_weightings == {
            'Autism': 2,
            'Aspergers': 1,
            'Conduct Dis': 2,
            'ODD': 2,
            'Low IQ': 1,
            'ADHD': 2,
            'Tourettes': 2,
            'Giftedness': 1,
            'Abuse': 1
        }

    def test_from_dict(self):
        code = uuid.uuid4()
        input_data = {
            "uuid": code,
            "text": "Disruptive in Class",
            "category": "Motivation and Concentration",
            'user_input_level': 2,
            "condition_weightings": {
                'Autism': 2,
                'Aspergers': 1,
                'Conduct Dis': 2,
                'ODD': 2
            }
        }
        char = Characteristic.from_dict(input_data)
        assert char.uuid == code
        assert char.text == "Disruptive in Class"
        assert char.category == "Motivation and Concentration"
        assert char.user_input_level == 2
        assert char.condition_weightings == {
            'Autism': 2,
            'Aspergers': 1,
            'Conduct Dis': 2,
            'ODD': 2
        }

    def test_to_dict(self):
        char_dict = {
            'uuid': uuid.uuid4(),
            'text': "Disruptive in Class",
            'category': 'Motivation and Concentration',
            'user_input_level': 2,
            'condition_weightings': {
                'Autism': 2,
                'Aspergers': 1,
                'Conduct Dis': 2,
                'ODD': 2
            }
        }
        char = Characteristic.from_dict(char_dict)
        assert char.to_dict() == char_dict

    add_points_test_data = [
        ("Autism", 4),
        ("Aspergers", 2),
        ("Conduct Dis", 4)
    ]

    @pytest.mark.parametrize("name,called_with", add_points_test_data)
    def test_add_points_to_condition(self, name, called_with, disruptive_char, mock_condition):
        condition = mock_condition
        condition.name = name
        disruptive_char.add_points_to_condition(condition)
        condition.add_points.assert_called_once_with(called_with)

    def test_get_condition_names(self, disruptive_char):
        result = disruptive_char._get_condition_names()
        assert result == ['Autism', 'Aspergers', 'Conduct Dis', 'OOD', 'Low IQ', 'ADHD', 'Tourettes', 'Giftedness', 'Abuse']

    def test_user_input_level(self, disruptive_char):
        with pytest.raises(ValueError):
            disruptive_char.user_input_level = -1
            disruptive_char.user_input_level = 3
            disruptive_char.user_input_level = 2.1
            disruptive_char.user_input_level = 4
        disruptive_char.user_input_level = 0
        disruptive_char.user_input_level = 1
        disruptive_char.user_input_level = 2

    def test_conditions(self, disruptive_char):
        assert disruptive_char.conditions == [
            'Autism',
            'Aspergers',
            'Conduct Dis',
            'OOD',
            'Low IQ',
            'ADHD',
            'Tourettes',
            'Giftedness',
            'Abuse'
        ]


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

    def test_condition_equals(self):
        cnd_dict = {
            'uuid': 'cnd-1',
            'name': 'Autism',
            'points': 58
        }
        cnd1 = Condition.from_dict(cnd_dict)
        cnd2 = Condition.from_dict(cnd_dict)
        assert cnd1 == cnd2

    add_points_test_data = [
        (2, 2),
        (1, 1),
        (0, 0)
    ]

    @pytest.mark.parametrize("points,expected", add_points_test_data)
    def test_add_points(self, points, expected):
        cnd = Condition()
        cnd.add_points(points)
        assert cnd.points == expected

    def test_add_negative_points_raises_error(self):
        cnd = Condition()
        with pytest.raises(ValueError):
            cnd.add_points(-1)

    def test_set_points(self):
        cnd = Condition()
        cnd.points = 5
        assert cnd._points == 5
        assert cnd.points == 5

    def test_from_dict(self):
        code = uuid.uuid4()
        input_dict = {
            'uuid': code,
            'name': "Autism"
        }
        cnd = Condition.from_dict(input_dict)
        assert cnd.uuid == code
        assert cnd.name == "Autism"
        assert cnd.points == 0

    def test_to_dict(self):
        code = uuid.uuid4()
        expected = {
            'uuid': code,
            'name': 'Autism',
            'points': 15
        }
        cnd = Condition.from_dict(expected)
        assert cnd.to_dict() == expected
