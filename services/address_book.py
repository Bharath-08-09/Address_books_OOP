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

    # @validate_input
    def update_person(self, first_name, field=None, new_value=None, last_name_hint=None, **kwargs):
        edit_fields = kwargs.copy()
        if field and new_value:
            edit_fields[field] = new_value

        for person in self.contacts:
            if person.first_name == first_name and (last_name_hint is None or person.last_name == last_name_hint):
                for attr, val in edit_fields.items():
                    setattr(person, attr, val)
                print("✅ Contact updated.")
                return
        print("⚠️ Contact not found.")

    def find_by_first_name(self, first_name):
        return [[p.first_name, p.last_name] for p in self.contacts if p.first_name == first_name]