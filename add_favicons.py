import os
import re

base_dir = r'c:\outboundjatim'

# Favicon tags for root HTML files
root_favicon_tag = '''  <!-- Favicon -->
  <link rel="icon" type="image/webp" href="assets/img/Favicon-navbar.webp"/>
  <link rel="apple-touch-icon" href="assets/img/Favicon-navbar.webp"/>
</head>'''

# Favicon tags for subfolder HTML files
subfolder_favicon_tag = '''  <!-- Favicon -->
  <link rel="icon" type="image/webp" href="../assets/img/Favicon-navbar.webp"/>
  <link rel="apple-touch-icon" href="../assets/img/Favicon-navbar.webp"/>
</head>'''

# 1. Update generate_details.py
details_gen_path = os.path.join(base_dir, 'generate_details.py')
if os.path.exists(details_gen_path):
    with open(details_gen_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Favicon-navbar.webp' not in content:
        content = content.replace('</head>', '''  <!-- Favicon -->
  <link rel="icon" type="image/webp" href="../assets/img/Favicon-navbar.webp"/>
  <link rel="apple-touch-icon" href="../assets/img/Favicon-navbar.webp"/>
</head>''', 1)
        with open(details_gen_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated generate_details.py with favicon tags")

# 2. Update generate_blogs.py
blogs_gen_path = os.path.join(base_dir, 'generate_blogs.py')
if os.path.exists(blogs_gen_path):
    with open(blogs_gen_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Favicon-navbar.webp' not in content:
        content = content.replace('</head>', '''  <!-- Favicon -->
  <link rel="icon" type="image/webp" href="../assets/img/Favicon-navbar.webp"/>
  <link rel="apple-touch-icon" href="../assets/img/Favicon-navbar.webp"/>
</head>''', 1)
        with open(blogs_gen_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated generate_blogs.py with favicon tags")

# 3. Add favicons to all existing .html files in root & subfolders
for root, dirs, files in os.walk(base_dir):
    # Skip node_modules or .git if any
    if '.git' in root or 'node_modules' in root:
        continue
    
    is_root = (root == base_dir)
    target_favicon_code = root_favicon_tag if is_root else subfolder_favicon_tag
    
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                html_code = f.read()
            
            if 'Favicon-navbar.webp' not in html_code and '</head>' in html_code:
                html_code = html_code.replace('</head>', target_favicon_code, 1)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(html_code)
                print(f"Added favicon to: {file_path}")

print("Favicon injection process finished successfully!")
