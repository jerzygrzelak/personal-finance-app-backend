import json

# Read the contents of new_currencies.json
with open('new_currencies.json', encoding='utf-8') as file:
    data = json.load(file)

# Add empty values for namePlural and symbol keys to each entry
for currency in data:
    currency["namePlural"] = ""
    currency["symbol"] = ""

# Save the updated data to the same file
with open('new_currencies.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Updated data saved to new_currencies.json.")
