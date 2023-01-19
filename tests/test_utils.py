import pytest
from utils import *


# все эти тесты работают
def test_load_data():
    """
    тесты функции load_data
    :return:
    """
    assert len(load_data()) == 116
    assert type(load_data()) == list
    assert type(load_data()[0]) == dict


def test_get_place():
    """
    тесты функции get_place
    :return:
    """
    assert len(get_place('захарово')) == 15
    assert type(get_place('захарово')) == list
    assert type(get_place('захарово')[0]) == dict


def test_get_by_days():
    """
    тесты функции get_by_days
    :return:
    """
    assert len(get_by_days('будни')) == 15
    assert type(get_by_days('будни')) == list
    assert type(get_by_days('будни')[0]) == dict
