#Денис Сметанкин, 34-я когорта - Финальный проект. Инженер по тестированию плюс
import send_stand_requests

import requests

import configuration

import data

def test_getorder():
    res = send_stand_requests.get_order_by_track()
    assert res == 200

