import pytest
import json
import logging
import os
import joblib
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data ={
    "incorrect_range":
        {
            "Type": 12,
            "Process_temperature_[K]": 12,
            "Rotational_speed_[rpm]": 12,
            "Tool_wear_[min]":12 ,
            "Machine_failure": 12
        },
    "correct_range":
        {
            "Type": 1,
            "Process_temperature_[K]": 307,
            "Rotational_speed_[rpm]": 1200,
            "Tool_wear_[min]":120 ,
            "Machine_failure": 1
        },
    "incorrect_col":
        {
            "Typet": 120,
            "Process_temperature_[K]t": 121,
            "Rotationalyu speed_[rpm]": 1,
            "Tool_wear_ty[min]":129 ,
            "Machine_yufailure": 120
        }
            }
Air_temperature_range ={
        "min" : 295.3,
        "max" : 304.5
    }
def test_form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert Air_temperature_range["min"] <= res <= Air_temperature_range["max"]

def test_api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)
    assert Air_temperature_range["min"] <= res["response"] <= Air_temperature_range["max"]

def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)

def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message

def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCols().message