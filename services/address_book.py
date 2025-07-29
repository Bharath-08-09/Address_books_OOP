import json
import csv
from utils.validation import validate_input
from models.person import Person

class ContactBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []
        self.city_directory = {}
        self.state_directory = {}

    @validate_input
    def add_person(self, **kwargs):
        new_person = Person(**kwargs)
        if [new_person.first_name, new_person.last_name] in self.find_by_first_name(new_person.first_name):
            print("Duplicate contact exists.")
            return
        self.contacts.append(new_person)

        self.city_directory.setdefault(new_person.city, []).append(new_person)
        self.state_directory.setdefault(new_person.state, []).append(new_person)

        print("✅ Contact successfully added.")