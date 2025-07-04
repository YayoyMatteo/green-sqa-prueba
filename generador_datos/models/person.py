from .base_user import BaseUser

class Person(BaseUser):
    def __init__(self, name, surname, age, document, country, city, language):
        super().__init__(name, document, country, city, language)
        self.surname = surname
        self.age = age

    def to_dict(self):
        return {
            "nombre": self.name,
            "apellido": self.surname,
            "edad": self.age,
            "documento": self.document,
            "pais": self.country,
            "ciudad": self.city,
            "idioma": self.language,
            "tipo": "persona"
        }
