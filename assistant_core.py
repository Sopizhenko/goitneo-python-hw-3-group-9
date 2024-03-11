from collections import UserDict
from datetime import datetime
from birthday_reminder import get_birthdays_per_week

class Field:
	def __init__(self, value):
		self.value = value


	def __str__(self):
		return str(self.value)


class Name(Field):
	def __init__(self, name):
		super().__init__(name)

	def __str__(self):
		return self.value


class Phone(Field):
	def __init__(self, phone):
		if len(phone) != 10 or not phone.isdigit():
			print("Phone number must be 10 digits long.")
			raise ValueError()
		super().__init__(phone)


class Birthday(Field):
	def __init__(self, birthday):
		try:
			birthday = datetime.strptime(birthday, "%d.%m.%Y")
			super().__init__(birthday)
		except ValueError:
			print("Date must be in format DD.MM.YYYY.")
			raise ValueError()
		
	def __str__(self):
		return self.value.strftime("%d.%m.%Y")


class Record:
	def __init__(self, name, birthday = None):
		self.name = Name(name)
		self.phones = []
		if birthday:
			self.birthday = Birthday(birthday)
		else:
			self.birthday = None


	def __str__(self):
		return f"Contact name: {self.name}, phones: {', '.join(map(str, self.phones))}"


	def add_phone(self, phone):
		self.phones.append(Phone(phone))


	def add_birthday(self, birthday):
		self.birthday = Birthday(birthday)


	def remove_phone(self, phone):
		for p in self.phones:
			if p.value == phone:
				self.phones.remove(p)
				break


	def edit_phone(self, phone, new_phone):
		for p in self.phones:
			if p.value == phone:
				p.value = new_phone
				break


	def find_phone(self, phone):
		for p in self.phones:
			if p.value == phone:
				return p


class AddressBook(UserDict):
	def add_record(self, record):
		self.data[record.name.value] = record


	def find(self, name):
		record = self.data.get(name)
		if record:
			return record
		else:
			print(f"No such record with name: {name} in address book.")


	def delete(self, name):
		record_to_delete = self.data.get(name)
		if record_to_delete:
			del self.data[name]
			print(f"Record with name: {name} deleted.")
		else:
			print(f"No such record with name: {name} in address book.")


	def week_birthdays(self):
		contacts = []
		for record in self.data.values():
			if record.birthday:
				contacts.append({"name": record.name.value, "birthday": record.birthday.value})
		get_birthdays_per_week(contacts)