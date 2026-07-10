import csv
from datetime import datetime

# Open your uploaded spreadsheet
with open('algae_data.csv', mode='r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        # Generate a standard Jekyll date and clean filename
        date_str = datetime.now().strftime("%Y-%m-%d")
        clean_title = row['title'].lower().replace(" ", "-")
        filename = f"_posts/{date_str}-{clean_title}.md"
        
        # Build the Jekyll Front Matter format dynamically
        markdown_content = f"""---
layout: post
title: "{row['title']}"
tags: [{row['tags']}]
strain_id: "{row['strain_id']}"
locality: "{row['locality']}"
culture_brief: "{row['culture_brief']}"
---

## Specimen Profile for {row['title']}
* **Strain ID:** {row['strain_id']}
* **Collection Locality:** {row['locality']}

### Notes
Automated entry generated from master repository spreadsheet.
"""
        # Save the file into the _posts directory
        with open(filename, 'w', encoding='utf-8') as out_file:
            out_file.write(markdown_content)

print("Algae profile posts successfully generated!")
