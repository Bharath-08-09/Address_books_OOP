import json
import csv
from utils.validation import validate_input
from models.contact import Person

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

    def remove_person(self, first_name, last_name=None):
        for p in self.contacts:
            if p.first_name == first_name and (last_name is None or p.last_name == last_name):
                self.contacts.remove(p)
                print("✅ Contact deleted.")
                return
        print("⚠️ Contact not found.")
    def export_txt(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for idx, p in enumerate(self.contacts, 1):
                file.write(f"{idx}. {str(p)}\n")
        print("📄 Saved as TXT.")
    def export_csv(self, filename):
        with open(filename, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.contacts[0].to_dict().keys())
            writer.writeheader()
            writer.writerows([p.to_dict() for p in self.contacts])
        print("📄 Saved as CSV.")
    def export_json(self, filename):
        with open(filename, "w") as f:
            json.dump([p.to_dict() for p in self.contacts], f, indent=4)
        print("📄 Saved as JSON.")


