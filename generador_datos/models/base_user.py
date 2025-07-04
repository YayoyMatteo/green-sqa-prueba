from abc import ABC, abstractmethod

class BaseUser(ABC):
    def __init__(self, name, document, country, city, language):
        self.name = name
        self.document = document
        self.country = country
        self.city = city
        self.language = language

    @abstractmethod
    def to_dict(self):
        pass
