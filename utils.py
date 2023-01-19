# импортируем нужные библиотеки
import json


def load_data():
    """
    Загружаем информацию по рейсам из data/data1.json
    """
    with open('data/data1.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_place(place):
    """
    Находим все рейсы, которые начинают ехать со станции "place"
    :param place:
    :return:
    """
    result = []
    for race in load_data():
        if place.lower() in race['station'].lower():
            result.append(race)
    return result


def get_by_days(days):
    """
    Находим все рейсы, которые ездят по таким дням "days"
    :param days:
    :return:
    """
    result = []
    for race in load_data():
        if days.lower() in race['days'].lower():
            result.append(race)
    return result

