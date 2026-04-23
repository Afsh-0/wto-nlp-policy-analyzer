from src.extract import extract_text
from src.preprocess import clean_text
from src.nlp_pipeline import extract_entities
from src.insights import generate_insights
from src.visualization import plot_entity_frequency

pdf_path = "data/report.pdf"

raw_text = extract_text(pdf_path)
cleaned_text = clean_text(raw_text)

entities = extract_entities(cleaned_text)

insights = generate_insights(entities)

print("\nPOLICY INSIGHTS:\n")
for i in insights:
    print("-", i)

print("\nKEY ENTITIES:\n")
for k, v in entities.items():
    print(k, ":", list(set(v))[:8])


plot_entity_frequency(entities)

import sys
import os

os.makedirs("output", exist_ok=True)

original_stdout = sys.stdout

with open("output/report.txt", "w", encoding="utf-8") as f:
    sys.stdout = f   # redirect output to file

    print("\nPOLICY INSIGHTS:\n")
    for i in insights:
        print("-", i)

    print("\nKEY ENTITIES:\n")
    for k, v in entities.items():
        print(k, ":", list(set(v))[:8])

sys.stdout = original_stdout  # back to normal

print("Report saved to output/report.txt")
