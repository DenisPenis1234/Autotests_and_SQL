#Денис Сметанкин, 34-я когорта - Финальный проект. Инженер по тестированию плюс
import send_stand_requests

import requests

import configuration

import data

def test_getorder():
    #получаем трек заказа
    track = send_stand_requests.post_new_order(data.order_body)
    #вызываем метод GET для получения заказа по его номеру
    res = requests.get(configuration.URL_YASAMOKAT + configuration.END_GETODERBYTRACK + "?t=" + str(track))
    #проверяем, что статус код равен 200
    assert res.status_code == 200