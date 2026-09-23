import os

base_dir = r'c:\outboundjatim'

def process_topbar(content):
    # Direct exact replacements for precision & safety
    
    # 1. Outer topbar div class
    old_outer = 'class="bg-primary-container text-on-primary py-2 px-4 sm:px-8 text-xs sm:text-sm font-medium border-b border-primary/40"'
    new_outer = 'class="bg-primary-container text-on-primary py-1 sm:py-2 px-3 sm:px-8 text-[10px] sm:text-sm font-medium border-b border-primary/40"'
    content = content.replace(old_outer, new_outer)

    # 2. Inner flex container class
    old_inner = 'class="flex items-center gap-2 overflow-x-auto text-on-primary/90 text-xs sm:text-sm"'
    new_inner = 'class="flex items-center gap-1.5 sm:gap-2 overflow-x-auto text-on-primary/90 text-[10px] sm:text-sm whitespace-nowrap sm:whitespace-normal"'
    content = content.replace(old_inner, new_inner)

    # 3. Pin drop icon
    old_pin = '<span class="material-symbols-outlined text-[16px] text-secondary-container">pin_drop</span>'
    new_pin = '<span class="material-symbols-outlined text-[13px] sm:text-[16px] text-secondary-container">pin_drop</span>'
    content = content.replace(old_pin, new_pin)

    # 4. Area Layanan label badge
    old_badge = '<span class="font-headline font-bold text-secondary-container tracking-wider uppercase text-[11px]">Area Layanan:</span>'
    new_badge = '<span class="font-headline font-bold text-secondary-container tracking-wider uppercase text-[9px] sm:text-[11px]">Area Layanan:</span>'
    content = content.replace(old_badge, new_badge)

    # 5. Call icon
    old_call = '<span class="material-symbols-outlined text-[16px]">call</span>'
    new_call = '<span class="material-symbols-outlined text-[13px] sm:text-[16px]">call</span>'
    content = content.replace(old_call, new_call)

    # 6. Hotline text font size
    old_hotline = 'class="font-headline font-semibold text-xs sm:text-sm">Hotline 24/7: +62 822-1122-1909</span>'
    new_hotline = 'class="font-headline font-semibold text-[10px] sm:text-sm">Hotline 24/7: +62 822-1122-1909</span>'
    content = content.replace(old_hotline, new_hotline)

    return content

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = process_topbar(content)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated topbar font size in: {filepath}")

print("Topbar mobile font size adjustment completed successfully!")
