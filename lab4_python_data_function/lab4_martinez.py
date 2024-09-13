"""
Samuel Martinez
Pyhton Data and Function
"""

print("\n --- Example 1 : Dictionary ---")
car = {
    "brand": "Tesla",
    "model": "S",
    "year": 2023
}

print(f"Best car 2022 = {car['brand']}, model = {car['model']}")

print("\n--- Example 2: Loop through each key in a dictionary ---")
for k in car:
    print(f"{k} has a value of {car[k]}")

print("\n--- Example 3: Number of key-value pairs in a dictionary ---")
print(f"Dictionary has {len(car)} key-value pairs")

print("\n--- Example 4: Remove a key-value pair from a dictionary ---")
car.pop("year", None)
print(f"Dictionary after removing the 'year' key")
for k in car:
    print(f"{k} , {car[k]}")

print("\n--- Example 5: Get value of a key ---")
look_key = "last_visit"
print(f"The value of key {look_key} is {car.get(look_key)}")

print("\n--- Example 6: Store data in dictionary ---")
phrase = "to be or not to be"
phrase = phrase.split()
print(f"phrase after split method {phrase}")

word_count_dict = {}  # Initialize an empty dictionary to store word counts

# For loop to count how many times a word is in the dictionary
for word in phrase:
    if word not in word_count_dict:
        word_count_dict[word] = 1
    else:
        word_count_dict[word] += 1

print(word_count_dict)


print("\n --- Exercise ---")

# Given the following user list, find the number of users that use 'gmail', 'hotmail', and 'yahoo'

user = """
    peter = ppan@gmail.com
    diana = d@hotmail.com
    Kent = ckent@yahoo.com
    Bruce = bwayne@hotmail.com
    tony = tstark@gmail.com
    shrek = shrek@gmail.com
"""

provider_count = {
    'gmail': 0,
    'hotmail': 0,
    'yahoo': 0
}


for line in user.strip().split('\n'):
    parts = line.split('=', 1)
    if len(parts) == 2:
        email = parts[1].strip()
        if '@gmail.com' in email:
            provider_count['gmail'] += 1
        elif '@hotmail.com' in email:
            provider_count['hotmail'] += 1
        elif '@yahoo.com' in email:
            provider_count['yahoo'] += 1


print(f"Number of users with Gmail: {provider_count['gmail']}")
print(f"Number of users with Hotmail: {provider_count['hotmail']}")
print(f"Number of users with Yahoo: {provider_count['yahoo']}")

