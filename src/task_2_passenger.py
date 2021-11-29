from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, id: str, name: str) -> None:
        super().__init__()
        self._id = id
        self._name = name
    
    @abstractmethod
    def __str__(self) -> str:
        pass
        # return super().__str__()


class Pilot(Person):
    
    def __str__(self) -> str:
        return f'{self._name} ({self._id}) is the pilot.'

    def __repr__(self) -> str:
        return f'{type(self).__name__}(Name={self._name}, id={self._id})'


class Crew(Person):

    def __str__(self) -> str:   
        return f'{self._name} ({self._id}) is the crew.'

    def __repr__(self) -> str:
        return f'{type(self).__name__}(Name={self._name}, id={self._id})'


class Passenger(Person):

    def __str__(self) -> str:   
        return f'{self._name} ({self._id}) is the passenger.'

    def __repr__(self) -> str:
        return f'{type(self).__name__}(Name={self._name}, id={self._id})'