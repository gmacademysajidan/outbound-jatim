import os
import re

network_provider_html = '''      <!-- Network Provider Section -->
      <div class="pt-8 pb-8 border-b border-outline-variant/30">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-4">
          <div class="flex items-center gap-2">
            <div class="w-7 h-7 rounded-lg bg-primary-container/10 flex items-center justify-center text-primary-container">
              <span class="material-symbols-outlined text-[18px]">hub</span>
            </div>
            <h4 class="font-headline text-xs font-bold uppercase tracking-wider text-primary-container">Jaringan Provider Resmi</h4>
          </div>
          <span class="text-[11px] text-on-surface-variant/80 font-medium">Outbound Jatim Official Network</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-2">
          <a href="https://outbound.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">outbound.web.id</span>
          </a>
          <a href="https://outboundbatumalang.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">outboundbatumalang.web.id</span>
          </a>
          <a href="https://provideroutboundmalang.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">provideroutboundmalang.web.id</span>
          </a>
          <a href="https://outboundmalang.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">outboundmalang.web.id</span>
          </a>
          <a href="https://paketoutboundmalang.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">paketoutboundmalang.web.id</span>
          </a>
          <a href="https://vendoroutboundmalang.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">vendoroutboundmalang.web.id</span>
          </a>
          <a href="https://offroad.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">offroad.web.id</span>
          </a>
          <a href="https://paintball.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">paintball.web.id</span>
          </a>
          <a href="https://cobantalun.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">cobantalun.web.id</span>
          </a>
          <a href="https://rafting.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">rafting.web.id</span>
          </a>
          <a href="https://familygathering.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">familygathering.web.id</span>
          </a>
          <a href="https://outboundpantai.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">outboundpantai.web.id</span>
          </a>
          <a href="https://paintballbatumalang.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">paintballbatumalang.web.id</span>
          </a>
          <a href="https://vendorhampers.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">vendorhampers.web.id</span>
          </a>
          <a href="https://vendorpaintball.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">vendorpaintball.web.id</span>
          </a>
          <a href="https://paketoutbound.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">paketoutbound.web.id</span>
          </a>
          <a href="https://cobanrondo.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">cobanrondo.web.id</span>
          </a>
          <a href="https://malangtraveler.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">malangtraveler.web.id</span>
          </a>
          <a href="https://outboundkediri.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">outboundkediri.web.id</span>
          </a>
          <a href="https://pantaimalangselatan.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">pantaimalangselatan.web.id</span>
          </a>
          <a href="https://jasaoutboundmalang.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">jasaoutboundmalang.web.id</span>
          </a>
          <a href="https://vendoroffroad.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">vendoroffroad.web.id</span>
          </a>
          <a href="https://vendorgathering.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">vendorgathering.web.id</span>
          </a>
          <a href="https://outboundindonesia.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">outboundindonesia.web.id</span>
          </a>
          <a href="https://indonesiaoutbound.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">indonesiaoutbound.web.id</span>
          </a>
          <a href="https://gemilangkatunoutbound.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">gemilangkatunoutbound.web.id</span>
          </a>
          <a href="https://outboundjatim.web.id" target="_blank" rel="noopener noreferrer" class="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-surface-container-low hover:bg-primary-container hover:text-white border border-outline-variant/30 text-[11px] font-medium text-on-surface-variant transition-all duration-200 hover:shadow-sm">
            <span class="material-symbols-outlined text-[12px] opacity-60 group-hover:opacity-100">language</span>
            <span class="truncate">outboundjatim.web.id</span>
          </a>
        </div>
      </div>'''

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
