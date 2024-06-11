import csv
import json

def format_entry(entry):
    formatted_entry = {
        "text": f"<|system|> FSTT c'est la Faculté des Sciences et Techniques de Tanger <</s>> <|user|> Donne des détails sur le département {entry['departement_name']} </s> <|assistant|> {entry['departement_info']} </s>"
    }
    return formatted_entry

def format_departments_list(department_names):
    formatted_entry = {
        "text": f"<|system|> FSTT c'est la Faculté des Sciences et Techniques de Tanger <</s>> <|user|> Donne les noms de départements </s> <|assistant|> {', '.join(department_names)} </s>"
    }
    return formatted_entry

def format_department_count(department_count):
    formatted_entry = {
        "text": f"<|system|> FSTT c'est la Faculté des Sciences et Techniques de Tanger <</s>> <|user|> Donne le nombre de départements </s> <|assistant|> {department_count} </s>"
    }
    return formatted_entry

formatted_data = []
department_names = []
department_count = 0

with open("fstt-departements-info.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        department_names.append(row['departement_name'])
        department_count += 1
        formatted_entry = format_entry(entry=row)
        formatted_data.append(formatted_entry)

# Adding the single entry with all department names
formatted_departments_list = format_departments_list(department_names)
formatted_data.append(formatted_departments_list)

# Adding the entry with the department count
formatted_department_count = format_department_count(department_count)
formatted_data.append(formatted_department_count)

print(formatted_data)
with open("fstt_data.jsonl", "w", encoding="utf-8") as llama2:
    for entry in formatted_data:
        try:
            json.dump(entry, llama2, ensure_ascii=False)
            llama2.write('\n')
        except Exception as ex:
            print(ex)