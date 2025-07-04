from .base_user import BaseUser

class Company(BaseUser):
    def __init__(self, name, document, country, city, language):
        super().__init__(name, document, country, city, language)

    def to_dict(self):
        return {
            "nombre": self.name,
            "apellido": "",
            "edad": "",
            "documento": self.document,
            "pais": self.country,
            "ciudad": self.city,
            "idioma": self.language,
            "tipo": "empresa"
        }
