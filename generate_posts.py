import csv
import os
import shutil
import urllib.parse
from datetime import datetime

# ==========================================
# 1. CLEAN SLATE: PURGE DUPLICATES
# ==========================================
if os.path.exists('_posts'):
    shutil.rmtree('_posts')

os.makedirs('_posts', exist_ok=True)

BASE_IMAGE_DIR = 'assets/images'

def normalize_name(name):
    return name.lower().replace(" ", "").replace("-", "").replace("_", "").replace(".", "").replace("/", "").replace("\\", "")

# ==========================================
# 2. READ CSV AND GENERATE POSTS
# ==========================================
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
        
        if clean_strain:
            filename = f"_posts/{date_str}-{clean_title}-{clean_strain}.md"
        else:
            filename = f"_posts/{date_str}-{clean_title}.md"
            
        # ==========================================
        # 3. AUTOMATED IMAGE SEARCH LOOP
        # ==========================================
        image_markdown = ""
        
        if strain_id and os.path.isdir(BASE_IMAGE_DIR):
            target_normal = normalize_name(strain_id)
            matched_folder = None
            
            for folder in os.listdir(BASE_IMAGE_DIR):
                folder_path = os.path.join(BASE_IMAGE_DIR, folder)
                if os.path.isdir(folder_path):
                    if normalize_name(folder) == target_normal:
                        matched_folder = folder
                        break
            
            if matched_folder:
                strain_img_folder = f"{BASE_IMAGE_DIR}/{matched_folder}"
                valid_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
                
                # Use .lower() here ONLY to find the files, without renaming them
                img_files = sorted([img for img in os.listdir(strain_img_folder) if img.lower().endswith(valid_exts)])
                
                if img_files:
                    for img in img_files[:3]:
                        # Make spaces safe for web URLs (e.g., "Image 1.JPG" -> "Image%201.JPG")
                        safe_img = urllib.parse.quote(img)
                        web_path = f"{{{{ '/{strain_img_folder}/{safe_img}' | relative_url }}}}"
                        image_markdown += f"![{title}]({web_path})\n\n"
                        
                    if len(img_files) > 3:
                        image_markdown += "<details>\n"
                        image_markdown += "  <summary><strong>View all images</strong></summary>\n\n"
                        for img in img_files[3:]:
                            safe_img = urllib.parse.quote(img)
                            web_path = f"{{{{ '/{strain_img_folder}/{safe_img}' | relative_url }}}}"
                            image_markdown += f"  <img src='{web_path}' alt='{title}' style='max-width:100%; margin-bottom:15px;'>\n"
                        image_markdown += "</details>\n"
        
        if not image_markdown:
            image_markdown = "*No images available for this specimen yet.*\n"

        # ==========================================
        # 4. MARKDOWN LAYOUT TEMPLATE
        # ==========================================
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

### Specimen Photo Gallery
{image_markdown}

### Notes
Automated entry generated from master repository spreadsheet.
"""
        with open(filename, 'w', encoding='utf-8') as out_file:
            out_file.write(markdown_content)

print("All posts processed! Image names were kept exactly as-is to preserve links.")
