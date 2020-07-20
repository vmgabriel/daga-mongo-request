#!/usr/bin/python3
# Develop vmgabriel

"""Define a way for select last datas of sensor based in sensorData"""


# Libraries
from typing import List
from src.sensor_data.domain.sensor_data import SensorData

list_data = {}


def filter_last_data_reader(_y):
    """Define Filter Last Data Reader"""
    return lambda x: x[1].idReader == _y


def is_created_controller(id_controller: str) -> bool:
    """Return True if SensorData have id_controller"""
    return id_controller in list_data


def is_created_reader(id_controller: str, id_reader: str) -> bool:
    """Return True if SensorData with idController and IdReader is
    Already Created."""
    filtered = list(
        filter(
            filter_last_data_reader(id_reader),
            enumerate(list_data[id_controller])
        )
    )
    return len(filtered) > 0


def find_and_delete_reader(id_controller: str, id_reader: str) -> None:
    """Find and Delete in Array name_controller with id_reader"""
    filtered = list(
        filter(
            filter_last_data_reader(id_reader),
            enumerate(list_data[id_controller])
        )
    )
    del list_data[id_controller][filtered[0][0]]


def insert_reader(name_controller: str, data: SensorData) -> None:
    """With a name_controller insert to array data of SensorData"""
    list_data[name_controller].append(data)


def verify_data(data: SensorData) -> None:
    """With data of SensorData select as last data and put"""
    if not is_created_controller(data.idController):
        list_data[data.idController] = []
    if is_created_reader(data.idController, data.idReader):
        find_and_delete_reader(data.idController, data.idReader)
    insert_reader(data.idController, data)


def verify_datas(datas: List[SensorData]) -> None:
    """Use and verify datas"""
    for data in datas:
        verify_data(data)


def get_data_relation() -> List[SensorData]:
    """Get data relation valid"""
    data = []
    for _, value in list_data.items():
        data += value
    return data


def remove_datas() -> None:
    """Remove data"""
    list_data = {}
