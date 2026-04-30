import os
import glob

html_files = glob.glob("*.html")

desktop_index_old = """        <a href="#about" class="hover:text-zinc-500 transition-colors">Locations</a>
        <a href="meet-our-leaders.html" class="hover:text-zinc-500 transition-colors">Meet Our Leaders</a>
        <a href="our-origin.html" class="hover:text-zinc-500 transition-colors">Our Origin</a>
        <a href="tent-school-of-ministry.html" class="hover:text-zinc-500 transition-colors">TSM</a>
        <a href="campus-rush.html" class="hover:text-zinc-500 transition-colors">Campus Rush</a>
        <a href="#connect" class="hover:text-zinc-500 transition-colors">Connect</a>"""

desktop_index_new = """        <a href="our-origin.html" class="hover:text-zinc-500 transition-colors">Our Origin</a>
        <a href="meet-our-leaders.html" class="hover:text-zinc-500 transition-colors">Meet Our Leaders</a>
        <a href="campus-rush.html" class="hover:text-zinc-500 transition-colors">Campus Rush</a>
        <a href="tent-school-of-ministry.html" class="hover:text-zinc-500 transition-colors">TSM</a>
        <a href="#about" class="hover:text-zinc-500 transition-colors">Locations</a>
        <a href="#connect" class="hover:text-zinc-500 transition-colors">Connect</a>"""

mobile_index_old = """      <a href="#about" class="mobile-link text-lg font-medium text-zinc-900">Locations</a>
      <a href="meet-our-leaders.html" class="mobile-link text-lg font-medium text-zinc-900">Meet Our Leaders</a>
      <a href="our-origin.html" class="mobile-link text-lg font-medium text-zinc-900">Our Origin</a>
      <a href="tent-school-of-ministry.html" class="mobile-link text-lg font-medium text-zinc-900">TSM</a>
      <a href="campus-rush.html" class="mobile-link text-lg font-medium text-zinc-900">Campus Rush</a>
      <a href="#connect" class="mobile-link text-lg font-medium text-zinc-900">Connect</a>"""

mobile_index_new = """      <a href="our-origin.html" class="mobile-link text-lg font-medium text-zinc-900">Our Origin</a>
      <a href="meet-our-leaders.html" class="mobile-link text-lg font-medium text-zinc-900">Meet Our Leaders</a>
      <a href="campus-rush.html" class="mobile-link text-lg font-medium text-zinc-900">Campus Rush</a>
      <a href="tent-school-of-ministry.html" class="mobile-link text-lg font-medium text-zinc-900">TSM</a>
      <a href="#about" class="mobile-link text-lg font-medium text-zinc-900">Locations</a>
      <a href="#connect" class="mobile-link text-lg font-medium text-zinc-900">Connect</a>"""

desktop_other_old = """        <a href="index.html#about" class="hover:text-zinc-500 transition-colors">Locations</a>
        <a href="meet-our-leaders.html" class="hover:text-zinc-500 transition-colors">Meet Our Leaders</a>
        <a href="our-origin.html" class="hover:text-zinc-500 transition-colors">Our Origin</a>
        <a href="tent-school-of-ministry.html" class="hover:text-zinc-500 transition-colors">TSM</a>
        <a href="campus-rush.html" class="hover:text-zinc-500 transition-colors">Campus Rush</a>
        <a href="index.html#connect" class="hover:text-zinc-500 transition-colors">Connect</a>"""

desktop_other_new = """        <a href="our-origin.html" class="hover:text-zinc-500 transition-colors">Our Origin</a>
        <a href="meet-our-leaders.html" class="hover:text-zinc-500 transition-colors">Meet Our Leaders</a>
        <a href="campus-rush.html" class="hover:text-zinc-500 transition-colors">Campus Rush</a>
        <a href="tent-school-of-ministry.html" class="hover:text-zinc-500 transition-colors">TSM</a>
        <a href="index.html#about" class="hover:text-zinc-500 transition-colors">Locations</a>
        <a href="index.html#connect" class="hover:text-zinc-500 transition-colors">Connect</a>"""

mobile_other_old = """      <a href="index.html#about" class="mobile-link text-lg font-medium text-zinc-900">Locations</a>
      <a href="meet-our-leaders.html" class="mobile-link text-lg font-medium text-zinc-900">Meet Our Leaders</a>
      <a href="our-origin.html" class="mobile-link text-lg font-medium text-zinc-900">Our Origin</a>
      <a href="tent-school-of-ministry.html" class="mobile-link text-lg font-medium text-zinc-900">TSM</a>
      <a href="campus-rush.html" class="mobile-link text-lg font-medium text-zinc-900">Campus Rush</a>
      <a href="index.html#connect" class="mobile-link text-lg font-medium text-zinc-900">Connect</a>"""

mobile_other_new = """      <a href="our-origin.html" class="mobile-link text-lg font-medium text-zinc-900">Our Origin</a>
      <a href="meet-our-leaders.html" class="mobile-link text-lg font-medium text-zinc-900">Meet Our Leaders</a>
      <a href="campus-rush.html" class="mobile-link text-lg font-medium text-zinc-900">Campus Rush</a>
      <a href="tent-school-of-ministry.html" class="mobile-link text-lg font-medium text-zinc-900">TSM</a>
      <a href="index.html#about" class="mobile-link text-lg font-medium text-zinc-900">Locations</a>
      <a href="index.html#connect" class="mobile-link text-lg font-medium text-zinc-900">Connect</a>"""

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    if file == 'index.html':
        content = content.replace(desktop_index_old, desktop_index_new)
        content = content.replace(mobile_index_old, mobile_index_new)
    else:
        content = content.replace(desktop_other_old, desktop_other_new)
        content = content.replace(mobile_other_old, mobile_other_new)
        
    with open(file, 'w') as f:
        f.write(content)
    
    print(f"Updated {file}")

