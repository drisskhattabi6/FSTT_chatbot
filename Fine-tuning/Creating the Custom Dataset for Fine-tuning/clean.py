import json

# Function to clean JSON lines
def clean_json_line(line):
    try:
        # Load the JSON object from the line
        json_obj = json.loads(line)
        # Replace � with é in the "text" field
        if "text" in json_obj:
            json_obj["text"] = json_obj["text"].replace('Ãª', 'é')
        # Return the cleaned JSON object as a string
        return json.dumps(json_obj, ensure_ascii=False)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON on line: {line}")
        print(f"Error message: {e}")
        return None

# Read the file contents line by line with 'latin-1' encoding
with open('fstt_data1.jsonl', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Process each line to replace � with é
processed_lines = [clean_json_line(line) for line in lines if clean_json_line(line) is not None]

# Write the processed lines back to the file
with open('fstt_data1.jsonl', 'w', encoding='utf-8') as file:
    for processed_line in processed_lines:
        file.write(processed_line + '\n')