import csv
import json

def format_response(prompt, response):
    formatted_entry = {
        "text": f"<|system|> FSTT c'est la Faculté des Sciences et Techniques de Tanger <</s>> <|user|>  {prompt} </s> <|assistant|> {response} </s>"
    }
    return formatted_entry

def distinct_values(column_values):
    distinct_set = set(column_values)
    distinct_list = sorted(list(distinct_set))  # Ensure the order is consistent
    return ', '.join(distinct_list)

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

with open("fstt-formation-initial.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    formation_types = []
    mst_names = []
    mst_programs = {}
    mst_objectifs = {}
    mst_skills = {}
    mst_coords = {}
    
    for row in reader:
        # Gather formation types and mst names
        formation_types.append(row['formation_type'])
        mst_names.append(row['mst_name'])
        
        # Collect program, objective, skills, and coordinator information
        mst_programs[row['mst_name']] = row['mst_program']
        mst_objectifs[row['mst_name']] = row['mst_objectif']
        mst_skills[row['mst_name']] = row['mst_skills']
        mst_coords[row['mst_name']] = row['mst_Coord']

# Adding the single entry with distinct formation types
distinct_formation_types = distinct_values(formation_types)
distinct_formation_types_response = format_response("Donne les formations qui existent dans FSTT:", distinct_formation_types)
new_data.append(distinct_formation_types_response)

# Adding the single entry for each question
questions_responses = {
    "Donne le programme de mst_name": mst_programs,
    "Donne l'objectif de mst_name": mst_objectifs,
    "Donne les skills de mst_name": mst_skills,
    "Donne le Coordinnateur de mst_name": mst_coords
}

for question, response_dict in questions_responses.items():
    for mst_name, response in response_dict.items():
        formatted_response = format_response(question.replace('mst_name', mst_name), response)
        new_data.append(formatted_response)

# Filter and add entries for license, master, and deust
license_names = [mst_name for mst_name, formation_type in zip(mst_names, formation_types) if formation_type == 'lst']
master_names = [mst_name for mst_name, formation_type in zip(mst_names, formation_types) if formation_type == 'mst']
deust_names = [mst_name for mst_name, formation_type in zip(mst_names, formation_types) if formation_type == 'deust']

license_response = format_response("Donne les licenses dans FSTT:", ', '.join(license_names))
master_response = format_response("Donne les masters dans FSTT:", ', '.join(master_names))
deust_response = format_response("Donne les deust dans FSTT:", ', '.join(deust_names))

new_data.extend([license_response, master_response, deust_response])

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
