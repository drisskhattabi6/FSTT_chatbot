import csv
import json

def format_article_entry(entry):
    formatted_entry = {
        "text": f"<|system|> FSTT c'est la Faculté des Sciences et Techniques de Tanger <</s>> <|user|> Donne des détails sur l'article '{entry['post_title']}' </s> <|assistant|> {entry['post_content']} </s>"
    }
    return formatted_entry

def format_articles_titles_entry(article_titles):
    formatted_entry = {
        "text": f"<|system|> FSTT c'est la Faculté des Sciences et Techniques de Tanger <</s>> <|user|> Donne des articles dans le site fstt </s> <|assistant|> {', '.join(article_titles)} </s>"
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
article_titles = []
with open("fstt-articles.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        article_titles.append(row['post_title'])
        formatted_entry = format_article_entry(entry=row)
        new_data.append(formatted_entry)

# Adding the single entry with all article titles
formatted_articles_titles_entry = format_articles_titles_entry(article_titles)
new_data.append(formatted_articles_titles_entry)

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