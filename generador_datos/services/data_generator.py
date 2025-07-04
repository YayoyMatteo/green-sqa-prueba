import random
from faker import Faker
from models.person import Person
from models.company import Company

fake = Faker()
used_docs = set()
used_fullnames = set()

class DataFactory:
    @staticmethod
    def create_user():
        is_company = random.choice([True, False])
        name = fake.first_name()

        if is_company:
            document = "9" + str(fake.random_number(digits=8, fix_len=True))
            country = fake.country()
            city = fake.city()
            language = "Español" if country == "Colombia" else "Inglés"
            return Company(name, document, country, city, language)

        age = random.randint(11, 79)
        surname = fake.last_name()
        full_name = f"{name} {surname}"
        while full_name in used_fullnames:
            name = fake.first_name()
            surname = fake.last_name()
            full_name = f"{name} {surname}"
        used_fullnames.add(full_name)

        if age < 18:
            document = str(random.randint(11000000, 11999999))
        else:
            document = str(random.randint(10**8, 10**11))

        while document in used_docs:
            document = str(random.randint(10**8, 10**11))
        used_docs.add(document)

        country = fake.country()
        city = fake.city()
        language = "Español" if country == "Colombia" else "Inglés"
        return Person(name, surname, age, document, country, city, language)
