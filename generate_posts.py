import csv
import os
from datetime import datetime

# Force the server to create the _posts folder if it is missing
os.makedirs('_posts', exist_ok=True)

# The master folder where you will upload your strain images
BASE_IMAGE_DIR = 'assets/images'

with open('algae_data.csv', mode='r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    reader.fieldnames = [name.strip().lower() for name in reader.fieldnames if name]
    
    for row in reader:
        title = row.get('title', '').strip()
        strain_id = row.get('strain_id', '').strip()
        locality = row.get('locality', '').strip()
        culture_brief = row.get('culture_brief', '').strip()
        tags = row.get('tags', '').strip()

        if not title:
            continue 

        date_str = datetime.now().strftime("%Y-%m-%d")
        
        clean_title = title.lower().replace(" ", "-").replace("/", "-").replace("\\", "-")
        clean_strain = strain_id.lower().replace(" ", "-").replace("/", "-").replace("\\", "-")
        
        # Determine the file name and the target image folder name
        if clean_strain:
            filename = f"_posts/{date_str}-{clean_title}-{clean_strain}.md"
            target_folder_name = clean_strain
        else:
            filename = f"_posts/{date_str}-{clean_title}.md"
            target_folder_name = clean_title # Fallback to title if no strain ID exists
            
        # --- AUTOMATED FOLDER IMAGE GRABBER ---
        image_markdown = ""
        
        # SAFETY LOCK: Ensure we have a valid folder name to look for
        if target_folder_name:
            # Build the exact path: e.g., assets/images/utex-2244
            strain_img_folder = f"{BASE_IMAGE_DIR}/{target_folder_name}"
            
            # Ensure it actually exists and is NOT the base directory
            if strain_img_folder != BASE_IMAGE_DIR and os.path.isdir(strain_img_folder):
                valid_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
                img_files = sorted([img for img in os.listdir(strain_img_folder) if img.lower().endswith(valid_exts)])
                
                if img_files:
                    image_markdown += "### Specimen Images\n\n"
                    
                    for img in img_files[:3]:
                        web_path = f"/{strain_img_folder}/{img}"
                        image_markdown += f"![{title}]({web_path})\n\n"
                        
                    if len(img_files) > 3:
                        image_markdown += "<details>\n"
                        image_markdown += "  <summary><strong>View all images</strong></summary>\n\n"
                        for img in img_files[3:]:
                            web_path = f"/{strain_img_folder}/{img}"
                            image_markdown += f"  <img src='{web_path}' alt='{title}' style='max-width:100%; margin-bottom:15px;'>\n"
                        image_markdown += "</details>\n"
        # --------------------------------------
        
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

{image_markdown}

### Notes
Automated entry generated from master repository spreadsheet.
"""
        with open(filename, 'w', encoding='utf-8') as out_file:
            out_file.write(markdown_content)

print("Algae profile posts successfully generated with targeted image galleries!")
        with open(filename, 'w', encoding='utf-8') as out_file:
            out_file.write(markdown_content)

print("Algae profile posts successfully generated with automated image galleries!")
