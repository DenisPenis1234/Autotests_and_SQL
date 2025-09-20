import configuration

import data

import requests

def post_new_order(body):
    #делаем POST запрос на создание заказа, используем URL и End-point из файла configuration.py, телом запроса является параметр функции
    res= requests.post(configuration.URL_YASAMOKAT + configuration.END_CREATEORDER, json=body)
    #получаем значение трек-номера заказа
    return res.json()['track']

def get_order_by_track():
    #получаем трек заказа
    track = post_new_order(data.order_body)
    #вызываем метод GET для получения заказа по его номеру
    res = requests.get(configuration.URL_YASAMOKAT + configuration.END_GETODERBYTRACK + "?t=" + str(track))
    return res.status_code


