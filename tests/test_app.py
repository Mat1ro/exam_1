import pytest
from app import app
from utils import *


# с этим тестом что то не так
def test_api():
    """
    тест api
    :return:
    """
    response = app.test_client().get('/api')
    assert response.status_code == 200
