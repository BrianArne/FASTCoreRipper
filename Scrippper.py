import sys
import re

print("Ripping: %s" % (sys.argv[1]))
f = open(sys.argv[1], "r+")
core = open(sys.argv[2], 'w+')
p = re.compile('<tr><td class="DLN">\d+</td><td>(.*)</td></tr>')
for line in f:
    matches = p.search(line)
    if matches:
        core.write((matches.group(1))+'\n')
f.close()
core.close()
