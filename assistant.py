from assistant_core import AddressBook, Name, Phone, Birthday, Record

def parse_input(user_input):
	cmd, *args = user_input.split()
	cmd = cmd.strip().lower()
	return cmd, *args


def input_error(func):
	def inner(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except ValueError:
			return "Give me name and phone please."
		except KeyError:
			return "Contact not found."
		except IndexError:
			return "The contact list is empty."
		
	return inner


@input_error
def add_contact(args, contacts):
	name, phone = args
	new_record = Record(name)
	new_record.add_phone(phone)
	contacts.add_record(new_record)
	return "Contact added."


@input_error
def change_contact(args, contacts):
	name, phone = args
	contact = contacts.data.get(name)
	if contact:
		contact.edit_phone(contact.phones[0].value, phone)
		return "Contact updated."
	else:
		raise KeyError


@input_error
def get_contact(args, contacts):
	name = args[0]
	contact = contacts.data.get(name)
	if contact:
		return f"The phone number of {contact.name} is {contact.phones[0]}."
	else:
		raise KeyError


@input_error
def get_all_contacts(contacts):
	if contacts:
		return "\n".join([f"{record}" for record in contacts.data.values()])
	else:
		raise IndexError


@input_error
def add_birthday(args, contacts):
	name, birthday = args
	contact = contacts.data.get(name)
	if contact:
		contact.add_birthday(birthday)
		return "Birthday added."
	else:
		raise KeyError


@input_error
def show_birthday(args, contacts):
	name = args[0]
	contact = contacts.data.get(name)
	if contact:
		if contact.birthday:
			return f"The birthday of {contact.name} is {contact.birthday}."
		else:
			return f"{contact.name} has no birthday."
	else:
		raise KeyError


def birthday_week(contacts):
	contacts.week_birthdays()


def help():
	return """Available commands:
	- hello: Show a welcome message.
	- add [name] [phone]: Add a new contact.
	- change [name] [phone]: Update a contact.
	- phone [name]: Get the phone number of a contact.
	- all: Get all contacts.
	- add-birthday [name] [birthday]: Add a birthday to a contact.
	- show-birthday [name]: Get the birthday of a contact.
	- birthdays: Get all contacts with birthdays for next week.
	- help: Show this help message.
	- close: Close the program.
	- exit: Close the program."""


def main():
	contacts = AddressBook()
	print("Welcome to the assistant bot!")
	while True:
		command = input("Enter a command: ")
		command, *args = parse_input(command)

		if command in ["close", "exit"]:
			print("Goodbye!")
			break
		elif command == "add":
			print(add_contact(args, contacts))
		elif command == "change":
			print(change_contact(args, contacts))
		elif command == "phone":
			print(get_contact(args, contacts))
		elif command == "all":
			print(get_all_contacts(contacts))
		elif command == "add-birthday":
			print(add_birthday(args, contacts))
		elif command == "show-birthday":
			print(show_birthday(args, contacts))
		elif command == "birthdays":
			birthday_week(contacts)
		elif command == "help":
			print(help())
		elif command == "hello":
			print("How can I help you?")
		else:
			print("Invalid command.")


if __name__ == "__main__":
	main()