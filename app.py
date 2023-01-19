# импортируем нужные библиотеки
from flask import Flask, render_template, request, jsonify
from utils import *
import logging

# создаем приложение
app = Flask(__name__, template_folder='templates')
# создаем логирование
logging.basicConfig(filename='logs/log.logs', level=logging.DEBUG)


@app.route('/')
def main_page():
    """
    Представление, которое выводит главную страницу со всеми рейсами
    :return:
    """
    logging.debug('открыл главную страницу')
    races = load_data()
    return render_template('index.html', races=races)


@app.route('/place')
def place_page():
    """
    Представление, которое выводит рейсы по нужной станции
    :return:
    """
    logging.debug('открыл представление, которое выводит рейсы по нужной станции')
    query = request.args.get('query')
    races = get_place(query)
    return render_template('place.html', races=races)


@app.route('/date')
def date_page():
    """
    Представление, которое выводит рейсы по нужным дням
    :return:
    """
    logging.debug('открыл представление, которое выводит рейсы по нужным дням')
    days = request.args.get('days')
    races = get_by_days(days)
    return render_template('day.html', races=races)


@app.route('/api')
def api_page():
    """
    вся информация в виде json
    :return:
    """
    logging.info('открыл api')
    races = load_data()
    return jsonify(races)


@app.errorhandler(404)
def page_404(e):
    """
    обрботка ошибки 404
    :param e:
    :return:
    """
    logging.error('ошибка 404')
    return '<h1>Страничка не найдена</h1><p>Попробуйте еще раз</p>', 404


@app.errorhandler(500)
def page_404(e):
    """
    обрботка ошибки 500
    :param e:
    :return:
    """
    logging.error('ошибка 500')
    return '<h1>Внутренняя проблема сервера</h1><p>ждем хозяина и он нам все починит</p>', 500


# Запускаем приложение
app.run()
