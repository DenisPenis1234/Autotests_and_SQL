import configuration

import data

import requests

def post_new_order(body):
    #делаем POST запрос на создание заказа, используем URL и End-point из файла configuration.py, телом запроса является параметр функции
    res= requests.post(configuration.URL_YASAMOKAT + configuration.END_CREATEORDER, json=body)
    #получаем значение трек-номера заказа
    return res.json()['track']

