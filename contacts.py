# Phone Book

"""
    Take name and phone number from user ad store it in a phone book
"""

# Get fullname from user
while True:
    full_name = input("Enter fullname: ")

    # Split fullname into separate names
    names = full_name.split(' ')

    # Validate name
    stop = True
    for name in names:
        if not name.isalpha():
            stop = False
            break

    if stop:
        break

