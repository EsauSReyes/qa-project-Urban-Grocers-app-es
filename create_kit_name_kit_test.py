import requests
import data
import sender_stand_request


def possitive_assert(name):
    kit_response = sender_stand_request.create_new_kit(name)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def negative_assert(name):
    kit_response = sender_stand_request.create_new_kit(name)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] != 400
    assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión" \
                                             "De 2 a 15 caracteres"
    print(kit_response.status_code)

def negative_assert_no_kits_name(name):
    kit_response = sender_stand_request.create_new_kit(name)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] != 400
    assert kit_response.json()["message"] == "No se han aprobado los parámetros requeridos"


def test_create_kit_1():
    possitive_assert(data.kit_body)

def test_create_kit_2():
    possitive_assert(data.kit_body_2)

def test_create_kit_3():
    negative_assert(data.kit_body_3)

def test_create_kit_4():
    negative_assert(data.kit_body_4)

def test_create_kit_5():
    possitive_assert(data.kit_body_5)

def test_create_kit_6():
    possitive_assert(data.kit_body_6)

def test_create_kit_7():
    possitive_assert(data.kit_body_7)

def test_create_kit_8():
    negative_assert_no_kits_name(data.kit_body_8)

def test_create_kit_9():
    negative_assert(data.kit_body_9)

