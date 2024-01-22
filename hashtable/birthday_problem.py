import random

TRAIALS = 1000000
same_birthdays = 0

for _ in range(TRAIALS):
    birthdays = []
    for i in range(57):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

print(f"{same_birthdays / TRAIALS * 100}%")
