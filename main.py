from uuid import uuid4 as get_uuid

from identifyneeds.repository import MemRepo
from identifyneeds.entities import Characteristic, Condition
from identifyneeds.use_cases import UpdateCondition


def get_characteristics():
    return [
        Characteristic(
            uuid=get_uuid(),
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
        ),
        Characteristic(
            uuid=get_uuid(),
            text="Slow to start/complete work",
            category="Motivation and Concentration",
            condition_weightings={
                'Anxiety': 1,
                'Depression': 1,
                'Low IQ': 2,
                'ADD-I': 2,
                'ADHD': 2,
                'SLD Dsl': 2,
                'SPLan': 1,
                'Giftedness': 1
            }
        )
    ]


def get_conditions(characteristics_list):
    conditions = []
    for char in characteristics_list:
        conditions += char.conditions
    print(conditions)
    return [Condition(uuid=str(get_uuid()), name=condition) for condition in conditions]


def main():
    characteristics = get_characteristics()
    conditions_objs = get_conditions(characteristics)
    print(conditions_objs)
    print(f"Going into MemRepo: {[cnd.to_dict() for cnd in conditions_objs]}")
    repo = MemRepo([cnd.to_dict() for cnd in conditions_objs])
    print(f"Current state of repo: {repo.get()}")

    for char in characteristics:
        user_input = None
        while user_input not in [0, 1, 2]:
            user_input = int(input(f"{char.text} - (Choose: 0, 1 or 2): "))
        char.user_input_level = user_input

    for char in characteristics:
        print(f"New char user input value: {char.text} - {char.user_input_level}")

    uc_update_condition = UpdateCondition(repo)
    for char in characteristics:
        print(f"Calling 'UpdateCondition' use case on {char.text}")
        uc_update_condition.execute(char)

    final_conditions = repo.get()
    print("Final condition values:")
    for cnd in final_conditions:
        print(cnd)


if __name__ == '__main__':
    main()
