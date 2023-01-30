person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)


# name of the second child
print(person.get("children")[1])
print(person["children"][1])  # easiest way to get the second child

# name of the cat
print(person["pets"]["cat"])

# use a for loop to list all the children
for i in person["children"]:
    print(i)

# print out the pets in this format;
# 'Type of pet: dog', 'Name of pet: Fido'
for i, j in person['pets'].items():
    print(f"Type of pet: {i} name of pet: {j}")
