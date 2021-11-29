from abc import ABC, abstractmethod
from task_0_singleton import singleton


class FlightClass(ABC):
    @staticmethod
    @abstractmethod
    def perks(self):
        pass


@singleton
class FirstClass(FlightClass):

    def __repr__(self) -> str:
        return f'{type(self).__name__}(Object)'

    @staticmethod
    def perks():
        return f'{__class__.__name__}:\n\tPerks:\n\t\tExtra Leg Room\n\t\tComfortable Seats\n\t\tFree Beverages'
    


@singleton
class BusinessClass(FlightClass):

    def __repr__(self) -> str:
        return f'{type(self).__name__}(Object)'

    @staticmethod
    def perks():
        return f'{__class__.__name__}:\n\tPerks:\n\t\tExtra Leg Room\n\t\tComfortable Seats'


@singleton
class EconomyClass(FlightClass):

    def __repr__(self) -> str:
        return f'{type(self).__name__}(Object)'

    @staticmethod
    def perks():
        return f'{__class__.__name__}:\n\tPerks:\n\t\tNo perks :D'