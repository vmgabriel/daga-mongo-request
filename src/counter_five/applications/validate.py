# Develop: vmgabriel
# Libraries
import datetime
from typing import List, TypeVar, Generic, Any

# Domains
from domain.models.validation_interface import Validate_Interface
from utils.validations.validation_handler import Validate_Handler

from counter_five.domain.measure_five import MeasureFive

class MeasureFiveValidate(Validate_Interface[MeasureFive]):
    """Validation for Input of Measure"""
    def __init__(self):
        self.v = Validate_Handler()
        self.not_verify = lambda x: True

    def validate_object(self, data: Any) -> (str, MeasureFive):
        """Validation of Object Complete"""
        _id            = data['_id'] if ('_id' in data) else None
        tookTime       = data['tookTime'] if ('tookTime' in data) else datetime.datetime.now()
        min            = data['min'] if ('min' in data) else 0.0
        max            = data['max'] if ('max' in data) else 0.0
        counter        = data['counter'] if ('counter' in data) else 0
        gr1            = data['gr1'] if ('gr1' in data) else 0.0
        gr2            = data['gr2'] if ('gr2' in data) else 0.0
        gr3            = data['gr3'] if ('gr3' in data) else 0.0
        gr4            = data['gr4'] if ('gr4' in data) else 0.0
        idReader       = data['idReader'] if ('idReader' in data) else None
        nameReader     = data['nameReader'] if ('nameReader' in data) else None
        idController   = data['idController'] if ('idController' in data) else None
        nameController = data['nameController'] if ('nameController' in data) else None
        createdAt      = data['tookTime'] if ('tookTime' in data) else datetime.datetime.now()
        updatedAt      = data['tookTime'] if ('tookTime' in data) else datetime.datetime.now()
        deletedAt      = data['tookTime'] if ('tookTime' in data) else datetime.datetime.now()

        return ('done correctly', MeasureFive(
            _id,
            tookTime,
            min,
            max,
            counter,
            gr1,
            gr2,
            gr3,
            gr4,
            idReader,
            nameReader,
            idController,
            nameController,
            createdAt,
            updatedAt,
            deletedAt
        ))


    def validate_object_update(self, data: Any) -> (str, MeasureFive):
        """Validate Object Update"""
        _id            = data['_id'] if ('_id' in data) else None
        tookTime       = data['tookTime'] if ('tookTime' in data) else datetime.datetime.now()
        min            = data['min'] if ('min' in data) else 0.0
        max            = data['max'] if ('max' in data) else 0.0
        counter        = data['counter'] if ('counter' in data) else 0
        gr1            = data['gr1'] if ('gr1' in data) else 0.0
        gr2            = data['gr2'] if ('gr2' in data) else 0.0
        gr3            = data['gr3'] if ('gr3' in data) else 0.0
        gr4            = data['gr4'] if ('gr4' in data) else 0.0
        idReader       = data['idReader'] if ('idReader' in data) else None
        nameReader     = data['nameReader'] if ('nameReader' in data) else None
        idController   = data['idController'] if ('idController' in data) else None
        nameController = data['nameController'] if ('nameController' in data) else None
        createdAt      = data['tookTime'] if ('tookTime' in data) else datetime.datetime.now()
        updatedAt      = data['tookTime'] if ('tookTime' in data) else datetime.datetime.now()
        deletedAt      = data['tookTime'] if ('tookTime' in data) else datetime.datetime.now()

        return ('done correctly', MeasureFive(
            _id,
            tookTime,
            min,
            max,
            counter,
            gr1,
            gr2,
            gr3,
            gr4,
            idReader,
            nameReader,
            idController,
            nameController,
            createdAt,
            updatedAt,
            deletedAt
        ))


    def data_filter_content(self, limit: int, offset: int) -> str:
        """Validate Filter content Data"""
        return self.validation_base.data_filter_content(limit, offset)

    def data_order_content(self, order: List[str]) -> bool:
        """Data order Content"""
        return self.validation_base.data_order_content(order)
