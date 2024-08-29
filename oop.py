class MagicalContact:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def describe(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone_number}"

class WizardOrWitch(MagicalContact):
    def __init__(self, name, email, phone_number, wand, house):
        super().__init__(name, email, phone_number)
        self.wand = wand
        self.house = house

    def describe(self):
        return f"{super().describe()}, Wand: {self.wand}, House: {self.house}"

class MagicalCreature(MagicalContact):
    def __init__(self, name, email, phone_number, species, is_tame):
        super().__init__(name, email, phone_number)
        self.species = species
        self.is_tame = is_tame

    def describe(self):
        tame_status = "Tame" if self.is_tame else "Not Tame"
        return f"{super().describe()}, Species: {self.species}, Tame: {tame_status}"


class MagicalContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def list_contacts(self):
        for contact in self.contacts:
            print(contact.describe())

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact.describe()
        return "Contact not found."


harry = WizardOrWitch(
    name="Harry Potter",
    email="harry@hogwarts.edu",
    phone_number="1240859685",
    wand="11 inches, Holly, phoenix feather",
    house="Gryffindor")


hedwig = MagicalCreature(
    name="Hedwig",
    email="hedwig@owls.post",
    phone_number="0987654321",
    species="Owl",
    is_tame=True)


contact_book = MagicalContactBook()
contact_book.add_contact(harry)
contact_book.add_contact(hedwig)

contact_book.list_contacts()
print(contact_book.find_contact("Harry Potter"))
class MagicalContact:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def describe(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone_number}"


class WizardOrWitch(MagicalContact):
    def __init__(self, name, email, phone_number, wand, house):
        super().__init__(name, email, phone_number)
        self.wand = wand
        self.house = house

    def describe(self):
        return f"{super().describe()}, Wand: {self.wand}, House: {self.house}"


class MagicalCreature(MagicalContact):
    def __init__(self, name, email, phone_number, species, is_tame):
        super().__init__(name, email, phone_number)
        self.species = species
        self.is_tame = is_tame

    def describe(self):
        tame_status = "Tame" if self.is_tame else "Not Tame"
        return f"{super().describe()}, Species: {self.species}, Tame: {tame_status}"


class MagicalContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def list_contacts(self):
        for contact in self.contacts:
            print(contact.describe())

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact.describe()
        return "Contact not found."
