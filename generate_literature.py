import csv
import os
from datetime import datetime

# Ensure _posts exists, but do NOT delete it so we keep the algae files
os.makedirs('_posts', exist_ok=True)

with open('literature.csv', mode='r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    reader.fieldnames = [name.strip().lower() for name in reader.fieldnames if name]
    
    for row in reader:
        title = row.get('title', '').strip()
        tags = row.get('tags', '').strip()
        literature_citations = row.get('literature_citations', '').strip()
        article_description = row.get('article_description', '').strip()

        if not title:
            continue 

        date_str = datetime.now().strftime("%Y-%m-%d")
        clean_title = title.lower().replace(" ", "-").replace("/", "-").replace("\\", "-")
        
        # Add "lit-" to prevent filename collisions
        filename = f"_posts/{date_str}-lit-{clean_title}.md"
            
        markdown_content = f"""---
layout: post
title: "{title}"
tags: [{tags}]
literature_citations: "{literature_citations}"
article_description: "{article_description}"
---

## {title}

**Citation:**
{literature_citations}

**Description:**
{article_description}
"""
        with open(filename, 'w', encoding='utf-8') as out_file:
            out_file.write(markdown_content)

print("Literature entries successfully generated into the _posts folder!")
