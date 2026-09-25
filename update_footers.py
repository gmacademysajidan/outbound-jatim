import os
import re

network_provider_html = '''      <!-- Network Provider Section -->
      <div class="pt-8 pb-6 border-b border-outline-variant/30">
        <div class="flex items-center gap-2 mb-3">
          <span class="material-symbols-outlined text-[18px] text-secondary">hub</span>
          <h4 class="font-headline text-xs font-bold uppercase tracking-wider text-primary-container">Network Provider</h4>
        </div>
        <div class="flex flex-wrap gap-1.5 sm:gap-2">
          <a href="https://outbound.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">outbound.web.id</a>
          <a href="https://outboundbatumalang.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">outboundbatumalang.web.id</a>
          <a href="https://provideroutboundmalang.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">provideroutboundmalang.web.id</a>
          <a href="https://outboundmalang.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">outboundmalang.web.id</a>
          <a href="https://paketoutboundmalang.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">paketoutboundmalang.web.id</a>
          <a href="https://vendoroutboundmalang.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">vendoroutboundmalang.web.id</a>
          <a href="https://offroad.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">offroad.web.id</a>
          <a href="https://paintball.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">paintball.web.id</a>
          <a href="https://cobantalun.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">cobantalun.web.id</a>
          <a href="https://rafting.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">rafting.web.id</a>
          <a href="https://familygathering.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">familygathering.web.id</a>
          <a href="https://outboundpantai.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">outboundpantai.web.id</a>
          <a href="https://paintballbatumalang.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">paintballbatumalang.web.id</a>
          <a href="https://vendorhampers.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">vendorhampers.web.id</a>
          <a href="https://vendorpaintball.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">vendorpaintball.web.id</a>
          <a href="https://paketoutbound.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">paketoutbound.web.id</a>
          <a href="https://cobanrondo.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">cobanrondo.web.id</a>
          <a href="https://malangtraveler.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">malangtraveler.web.id</a>
          <a href="https://outboundkediri.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">outboundkediri.web.id</a>
          <a href="https://pantaimalangselatan.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">pantaimalangselatan.web.id</a>
          <a href="https://jasaoutboundmalang.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">jasaoutboundmalang.web.id</a>
          <a href="https://vendoroffroad.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">vendoroffroad.web.id</a>
          <a href="https://vendorgathering.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">vendorgathering.web.id</a>
          <a href="https://outboundindonesia.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">outboundindonesia.web.id</a>
          <a href="https://indonesiaoutbound.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">indonesiaoutbound.web.id</a>
          <a href="https://gemilangkatunoutbound.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">gemilangkatunoutbound.web.id</a>
          <a href="https://outboundjatim.web.id" target="_blank" rel="noopener noreferrer" class="text-[11px] font-medium text-on-surface-variant bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 px-2.5 py-1 rounded-md transition-all duration-200">outboundjatim.web.id</a>
        </div>
      </div>
'''

html_files = []
for root, dirs, files in os.walk(r'c:\outboundjatim'):
    if 'stitch_outbound_jatim_website_wireframe' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

updated_count = 0

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'Network Provider' in content:
        print(f"Skipping (already updated): {fpath}")
        continue

    inserted = False
    
    if '<!-- Copyright & Legal -->' in content:
        content = content.replace('<!-- Copyright & Legal -->', network_provider_html + '\n      <!-- Copyright & Legal -->')
        inserted = True
    else:
        match = re.search(r'(<div class="pt-[68]\s+flex flex-col[\s\S]*?<p>©\s*2026 Outbound Jatim)', content)
        if match:
            target_str = match.group(1)
            content = content.replace(target_str, network_provider_html + '\n      ' + target_str)
            inserted = True
        else:
            p_idx = content.find('<p>© 2026 Outbound Jatim')
            if p_idx != -1:
                div_idx = content.rfind('<div', 0, p_idx)
                if div_idx != -1:
                    content = content[:div_idx] + network_provider_html + '\n      ' + content[div_idx:]
                    inserted = True

    if inserted:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1
        print(f"Updated: {fpath}")
    else:
        print(f"WARNING: Could not insert in {fpath}")

print(f"\nDone! Updated {updated_count} files out of {len(html_files)}.")
