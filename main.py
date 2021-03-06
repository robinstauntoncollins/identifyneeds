from uuid import uuid4 as get_uuid
import logging

from yaml import safe_load

from identifyneeds.entities import Characteristic, Condition
from identifyneeds.use_cases import UpdateCondition, GetMostLikelyConditions
from identifyneeds.repository import MemRepo


def get_characteristics_from_file(file_name):
    """Given a yaml file, read it and generate a list of characteristics from the data"""
    with open(file_name, 'r') as f:
        data = safe_load(f.read())
    characteristics_list = get_characteristics(data)
    return characteristics_list


def get_characteristics(data):
    """Generate a list of characteristics from data in a dictionary"""
    char_list = []
    for char, info in data.items():
        logging.debug(f"Char: {char}, Info: {info}")
        char_list.append(Characteristic(
            uuid=get_uuid(),
            text=info['text'],
            category=info['category'],
            condition_weightings=info['condition_weightings']
        ))
    return char_list


def get_conditions(characteristics_list):
    """Get a list of Conditions given a list of Characteristics"""
    conditions = []
    for char in characteristics_list:
        logging.debug(f"Working on {char}")
        conditions += char.conditions
    conditions_set = set(conditions)
    logging.debug(f"Conditions: {conditions_set}")
    return [Condition(uuid=str(get_uuid()), name=condition) for condition in list(conditions_set)]


def main():
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)s - %(levelname)s ] %(message)s"
    logging.basicConfig(level='INFO', format=FORMAT)
    file_name = 'characteristics.yml'
    characteristics = get_characteristics_from_file(file_name)
    logging.debug(f"Characteristics: {characteristics}")
    conditions_objs = get_conditions(characteristics)
    logging.debug(f"Condition objects: {conditions_objs}")
    logging.debug(f"Going into MemRepo: {[cnd.to_dict() for cnd in conditions_objs]}")
    repo = MemRepo([cnd.to_dict() for cnd in conditions_objs])
    logging.debug(f"Current state of repo: {repo.get()}")

    for char in characteristics:
        user_input = None
        while user_input not in [0, 1, 2]:
            try:
                user_input = int(input(f"{char.category} - {char.text} - (Choose: 0, 1 or 2): "))
            except ValueError:
                print(f"Invalid value. Please try again.")
        char.user_input_level = user_input

    for char in characteristics:
        logging.debug(f"New char user input value: {char.text} - {char.user_input_level}")

    uc_update_condition = UpdateCondition(repo)
    for char in characteristics:
        logging.debug(f"Calling 'UpdateCondition' use case on {char.text}")
        uc_update_condition.execute(char)

    final_conditions = repo.get()
    logging.debug("Final condition values:")
    for cnd in final_conditions:
        logging.debug(cnd)

    most_likely = GetMostLikelyConditions(repo).execute()
    print(f"The most likely condition(s) of the child is/are: {most_likely}")


if __name__ == '__main__':
    main()
