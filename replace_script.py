html_path = 'index.html'
with open(html_path, 'r') as f:
    lines = f.readlines()

with open('/tmp/replacement.html', 'r') as f:
    new_lines = f.readlines()

# Replace lines 256 to 439 inclusive. So indices 255 to 439 (since 1-indexed line 439 is index 438, slice should end at 439)
final_lines = lines[:255] + new_lines + lines[439:]
with open(html_path, 'w') as f:
    f.writelines(final_lines)
