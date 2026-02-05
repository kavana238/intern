# task 1

contact = {
    "John Doe": "785565551",
    "ram":"9856565656",
    "Sita":"9656565656",
    "Gita":"9856565656",
    "Hari":"9856565656",}

contact.get("John Doe")
John_doe = contact.get("John Doe")
print(John_doe)

contact["mohan"] = "9856564566"

print(contact)

contact.get("Sita")
print(contact.get("Sita"))

contact.get("Ramesh", "Contact not found")
print(contact.get("Ramesh", "Contact not found"))

for name, number in contact.items():
    print(f"{name}: {number}")


    #task 2

ids = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(ids) 
print(unique_users)
   
print("ID05" in unique_users)


print("original ids list", len(ids))
print("unique ids list", len(unique_users))

# task 3

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

common_interests = friend_a & friend_b
print("Common Interests:", common_interests)

all_interests = friend_a | friend_b
print("All Interests:", all_interests)

different_interests = friend_a - friend_b
print("Different Interests (Friend A - Friend B):", different_interests)
