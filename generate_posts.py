import csv
from datetime import datetime

# Open your uploaded spreadsheet with the BOM fix
with open('algae_data.csv', mode='r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    
    # Strip accidental spaces and force lowercase on all headers
    reader.fieldnames = [name.strip().lower() for name in reader.fieldnames if name]
    
    # Print what Python actually sees so we can read it in the logs
    print(f"Detected columns: {reader.fieldnames}")
    
    for row in reader:
        # Grab the data, ignoring any extra spaces in the cells
        title = row.get('title', '').strip()
        strain_id = row.get('strain_id', '').strip()
        locality = row.get('locality', '').strip()
        culture_brief = row.get('culture_brief', '').strip()
        tags = row.get('tags', '').strip()

        if not title:
            continue # Skip empty rows

        date_str = datetime.now().strftime("%Y-%m-%d")
        clean_title = title.lower().replace(" ", "-")
        filename = f"_posts/{date_str}-{clean_title}.md"
        
        markdown_content = f"""---
layout: post
title: "{title}"
tags: [{tags}]
strain_id: "{strain_id}"
locality: "{locality}"
culture_brief: "{culture_brief}"
---

## Specimen Profile for {title}
* **Strain ID:** {strain_id}
* **Collection Locality:** {locality}

### Notes
Automated entry generated from master repository spreadsheet.
"""
        with open(filename, 'w', encoding='utf-8') as out_file:
            out_file.write(markdown_content)

print("Algae profile posts successfully generated!")
