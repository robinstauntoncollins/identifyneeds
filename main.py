from uuid import uuid4 as get_uuid
from identifyneeds.entities import Characteristic, Condition


def get_characteristics():
    return [
        Characteristic(
            uuid=str(get_uuid),
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
    ]


def get_conditions():
    conditions = ['Autism', 'Aspergers', 'Anxiety', 'Mutism', 'Depression', 'Conduct Dis', 'ODD', 'Low IQ']
    return [Condition(uuid=get_uuid, name=condition) for condition in conditions]


def main():
    characteristics = get_characteristics()
    conditions = get_conditions()

    for char in characteristics:
        user_input = int(input(f"{char.text} - (Choose: 0,1 or 2): "))

        for cnd in conditions:
            char.add_points_to_condition(cnd, user_input)


if __name__ == '__main__':
    main()
