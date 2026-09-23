import os
import re

base_dir = r'c:\outboundjatim'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Desktop navbar standalone "Destinasi" link
    # Matches <a ...>Destinasi</a> or <a ...>\n Destinasi\n </a> where text inside tag is exactly "Destinasi"
    desktop_pattern = r'<a\s+class="[^"]*"[^\>]*href="(?:\.\.\/)?destinasi(?:\/index\.html|\.html)?"[^\>]*>\s*Destinasi\s*<\/a>'
    content = re.sub(desktop_pattern, '', content, flags=re.IGNORECASE)

    # 2. Mobile drawer standalone "Destinasi Venue" link (outside the dropdown/sub-block)
    # Notice: Dropdown/Sub-block item says "Kategori Destinasi Venue". Standalone item says "Destinasi Venue".
    mobile_pattern = r'<a\s+class="[^"]*font-headline[^"]*"[^\>]*href="(?:\.\.\/)?destinasi(?:\/index\.html|\.html)?"[^\>]*>\s*Destinasi Venue\s*<\/a>'
    content = re.sub(mobile_pattern, '', content, flags=re.IGNORECASE)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated navbar in: {filepath}")

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

print("Removal of standalone Destinasi link from navbar complete!")
