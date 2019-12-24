from identifyneeds.entities import Characteristic


class TestCharacteristic():

    def test_char_init(self):

        char = Characteristic(
            uuid=1,
            text="Disruptive in Class",
            category="Motivation and Concentration",
        )
        assert char.uuid == 1
        assert char.text == "Disruptive in Class"
        assert char.category == "Motivation and Concentration"

