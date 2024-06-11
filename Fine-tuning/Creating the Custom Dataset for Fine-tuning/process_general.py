import csv
import json

def format_entry(entry):
    formatted_entry = {
        "text": f" FSTT c'est la Faculté des Sciences et Techniques de Tanger <</s>> <|user|>  {entry[1]} </s> <|assistant|> {entry[0]} </s>"
    }
    return formatted_entry

formatted_data = []

file_path = "general_info.csv"

# Open and read the CSV file
with open(file_path, "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) >= 2:  # Ensure there are at least two columns
            formatted_entry = format_entry(entry=row)
            formatted_data.append(formatted_entry)

print(formatted_data)
with open("fstt_data1.jsonl", "a") as jsonl_file:
    for entry in formatted_data:
        try:
            json.dump(entry, jsonl_file, ensure_ascii=False)
            jsonl_file.write('\n')
        except Exception as ex:
            print(ex)