# Phone Book

"""
    Take name and phone number from user ad store it in a phone book
"""
import csv
from os import linesep

# # Get fullname from user
# while True:
#     full_name = input("Enter fullname: ")

#     # Split fullname into separate names
#     names = full_name.split(' ')

#     # Validate name
#     stop = True
#     for name in names:
#         if not name.isalpha() or len(name) == 1:
#             stop = False
#             break

#     if stop:
#         break


contacts = {
    "karthik": 123456789,
    "omkar": 987654321
}

contacts = [
    {
        "name": "Omkar",
        "phonenumber": 987654321,
    },
    {
        "name": "Karthik",
        "phonenumber": 123456789
    }
]

# contacts["foo"] = ""


print(contacts)

with open('./contacts.csv', 'a') as file:

    csv_writer = csv.DictWriter(file, fieldnames=["name", "phonenuber"], lineterminator="\n")

    csv_writer.writerow({"name": "foo", "phonenuber": 1223456789})


SELECT title FROM movies WHERE id IN (SELECT movie_id FROM stars WHERE person_id IN (SELECT id FROM people WHERE name = "Nicolas Cage"));

