import csv
import json

def format_club_entry(entry):
    formatted_entry = {
        "text": f"<|system|> FSTT c'est la Faculté des Sciences et Techniques de Tanger <</s>> <|user|> Donne des informations sur le club '{entry['club_name']}' </s> <|assistant|> {entry['departement_info']} </s>"
    }
    return formatted_entry

def format_clubs_list(club_names):
    formatted_entry = {
        "text": f"<|system|> FSTT c'est la Faculté des Sciences et Techniques de Tanger <</s>> <|user|> Donne les clubs de la FSTT </s> <|assistant|> {', '.join(club_names)} </s>"
    }
    return formatted_entry

def format_club_count(club_count):
    formatted_entry = {
        "text": f"<|system|> FSTT c'est la Faculté des Sciences et Techniques de Tanger <</s>> <|user|> Donne le nombre des clubs en FSTT </s> <|assistant|> {club_count} </s>"
    }
    return formatted_entry

# Load existing JSONL content
existing_data = []
try:
    with open("fstt_data.jsonl", "r", encoding="utf-8") as infile:
        for line in infile:
            existing_data.append(json.loads(line))
except FileNotFoundError:
    print("The existing JSONL file was not found. A new file will be created.")

# Process new CSV data and create formatted entries
new_data = []
club_names = []
club_count = 0

with open("fstt-clubs-info.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        club_names.append(row['club_name'])
        club_count += 1
        formatted_entry = format_club_entry(entry=row)
        new_data.append(formatted_entry)

# Adding the single entry with all club names
formatted_clubs_list_entry = format_clubs_list(club_names)
new_data.append(formatted_clubs_list_entry)

# Adding the single entry with the number of clubs
formatted_club_count_entry = format_club_count(club_count)
new_data.append(formatted_club_count_entry)

# Combine existing data with new data
combined_data = existing_data + new_data

# Write the combined data back to the JSONL file
with open("fstt_data.jsonl", "w", encoding="utf-8") as outfile:
    for entry in combined_data:
        try:
            json.dump(entry, outfile, ensure_ascii=False)
            outfile.write('\n')
        except Exception as ex:
            print(ex)