# tests/test_person_book.py

import pytest
from services.address_book import ContactBook
from services.system import BookSystem
from services.search import BookSearcher

@pytest.fixture
def mock_contact_list():
    return [
        {
            "first_name": "Rhea",
            "last_name": "Singh",
            "phone_number": "91 9876543210",
            "address": "Sector 10",
            "city": "Mumbai",
            "state": "Maharashtra",
            "zip": "400001",
            "email": "rhea@example.com"
        },
        {
            "first_name": "Rhea",
            "last_name": "Kumar",
            "phone_number": "91 9123456780",
            "address": "MG Road",
            "city": "Delhi",
            "state": "Delhi",
            "zip": "110001",
            "email": "rhea.k@example.com"
        }
    ]

@pytest.fixture
def single_book():
    return ContactBook("testbook")

def test_create_multiple_books():
    system = BookSystem()
    system.create_book("Home")
    system.create_book("Office")
    assert len(system.books) == 2

def test_add_contact(single_book, mock_contact_list):
    single_book.add_person(**mock_contact_list[0])
    assert len(single_book.contacts) == 1
    assert single_book.contacts[0].first_name == "Rhea"

def test_prevent_duplicate(single_book, mock_contact_list):
    single_book.add_person(**mock_contact_list[0])
    single_book.add_person(**mock_contact_list[0])  # same name
    assert len(single_book.contacts) == 1

def test_add_multiple_contacts(single_book, mock_contact_list):
    for entry in mock_contact_list:
        single_book.add_person(**entry)
    assert len(single_book.contacts) == 2

def test_edit_contact(single_book, mock_contact_list):
    for entry in mock_contact_list:
        single_book.add_person(**entry)
    single_book.update_person("Rhea", field="email", new_value="updated@example.com", last_name_hint="Kumar")
    assert single_book.contacts[1].email == "updated@example.com"

def test_invalid_phone(single_book):
    invalid = {
        "first_name": "Amit",
        "last_name": "Verma",
        "phone_number": "notanumber",
        "address": "5th Cross",
        "city": "Lucknow",
        "state": "UP",
        "zip": "226001",
        "email": "amitv@example.com"
    }
    with pytest.raises(ValueError):
        single_book.add_person(**invalid)

def test_delete_contact(single_book, mock_contact_list):
    for entry in mock_contact_list:
        single_book.add_person(**entry)
    single_book.remove_person("Rhea", last_name="Kumar")
    assert len(single_book.contacts) == 1

def test_city_state_directory(single_book, mock_contact_list):
    for entry in mock_contact_list:
        single_book.add_person(**entry)
    assert "Mumbai" in single_book.city_directory
    assert "Delhi" in single_book.city_directory
    assert "Delhi" in single_book.state_directory

def test_search_city_state():
    system = BookSystem()
    system.create_book("Work")
    book = system.get_book("Work")
    book.add_person(
        first_name="Priya",
        last_name="Iyer",
        phone_number="9876543210",
        address="JP Nagar",
        city="Bangalore",
        state="Karnataka",
        zip="560078",
        email="priya@example.com"
    )
    search = BookSearcher(system.books)
    assert len(search.search_by_city("Bangalore")) == 1
    assert len(search.search_by_state("Karnataka")) == 1

def test_save_txt(tmp_path, single_book, mock_contact_list):
    single_book.add_person(**mock_contact_list[0])
    file = tmp_path / "contacts.txt"
    single_book.export_txt(str(file))
    assert "Rhea" in file.read_text()

def test_save_csv(tmp_path, single_book, mock_contact_list):
    single_book.add_person(**mock_contact_list[0])
    file = tmp_path / "contacts.csv"
    single_book.export_csv(str(file))
    assert "Rhea" in file.read_text()

def test_save_json(tmp_path, single_book, mock_contact_list):
    single_book.add_person(**mock_contact_list[0])
    file = tmp_path / "contacts.json"
    single_book.export_json(str(file))
    assert "Rhea" in file.read_text()