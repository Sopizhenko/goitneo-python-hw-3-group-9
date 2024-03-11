from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
	today = datetime.today().date()
	week_birthdays = defaultdict(list)

	for user in users:
		name = user["name"]
		birthday = user["birthday"].date()
		birthday_this_year = birthday.replace(year = today.year)

		if birthday_this_year < today:
			birthday_this_year = birthday_this_year.replace(year = today.year + 1)

		if birthday_this_year.weekday() == 5:
			birthday_this_year += timedelta(days = 2)
		elif birthday_this_year.weekday() == 6:
			birthday_this_year += timedelta(days = 1)
		
		delta_days = (birthday_this_year - today).days

		if delta_days < 7:
			weekday = birthday_this_year.strftime("%A")
			week_birthdays[weekday].append(name)

	for key, value in week_birthdays.items():
		print(f"{key}: {', '.join(value)}")



if __name__ == "__main__":
	users = [
		{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
		{"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
		{"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14)},
		{"name": "Jeff Bezos", "birthday": datetime(1964, 1, 12)},
		{"name": "Elon Musk", "birthday": datetime(1971, 3, 8)},
		{"name": "Warren Buffet", "birthday": datetime(1930, 3, 3)},
		{"name": "Larry Page", "birthday": datetime(1973, 3, 4)},
		{"name": "Sergey Brin", "birthday": datetime(1973, 3, 9)},
		{"name": "Satya Nadella", "birthday": datetime(1967, 8, 19)},
		{"name": "Tim Cook", "birthday": datetime(1960, 11, 1)}
	]

	print(users)
	get_birthdays_per_week(users)