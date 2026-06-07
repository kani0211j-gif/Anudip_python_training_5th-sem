contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

search_name = "Karan"
vowel_names = []
vowels = "AEIOUaeiou"
found_contact = ""

# print alphabetical names first using sorted keys
print("--- Alphabetical Contacts ---")
for name in sorted(contacts.keys()):
    print(name)

# single loop to search name and check vowels
for name, number in contacts.items():
    # 1. check if name starts with vowel
    if name[0] in vowels:
        vowel_names.append(name)
        
    # 2. search for the required contact
    if name == search_name:
        found_contact = f"Found! Name: {name}, Phone: {number}"
        # break is handled implicitly or via flag to keep code simple
        # but if you specifically need break, keep the search loop separate as below:

print("\nTotal contacts saved:", len(contacts))
print("\nNames starting with vowel:", vowel_names)

# search with break as requested
print(f"\nSearching for '{search_name}':")
for name, number in contacts.items():
    if name == search_name:
        print(f"Found! Name: {name}, Phone: {number}")
        break

