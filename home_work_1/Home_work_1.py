import re
import collections

pattern = '.*/[0-9]{8}'
prog = re.compile(pattern)
new_list = []
with open('URLs.txt', 'r') as strig:
    for line in strig:
        line = line.strip()
        if prog.match(line):
            line = line.split('/')
            new_list.append(line[1])
print(collections.Counter(new_list))
