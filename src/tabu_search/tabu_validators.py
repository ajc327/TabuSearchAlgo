# Created by Andy at 04-Jan-21

# Enter description here
# This contains the validator classes used for input validation
# ___________________________________
from abc import ABC, abstractmethod


class Validator(ABC):

    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        return setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        '''This is implemented in the concrete classes to set validation rules'''


class Number(Validator):

    def __init__(self, min_value=None, max_value=None, is_int=False):

        self.min_value = min_value
        self.max_value = max_value
        self.is_int = is_int

    def validate(self, value):
        if self.is_int and not isinstance(value, int):
            raise TypeError(f"{value} should be an integer!")

        if not isinstance(value, (int, float)):
            raise ValueError("f{value} should be float or integer")

        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{value} should be at least {self.min_value}")

        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{value} should be less than {self.max_value}")


