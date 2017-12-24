import os
import sys

if len(sys.argv) < 3:
    print("Usage: script.py vdom rules.txt")
    exit()

vdom = sys.argv[1]

with open(sys.argv[2]) as rules_file:
    list01 = rules_file.readlines()

rules = []
disable_log = []

for line in list01:
	rules.append(line.strip())

disable_log.append('config vdom\nedit %s\nconfig firewall policy' %vdom)
for line in rules:
	edit = ('edit %s\nset logtraffic disable\nnext' %line)
	disable_log.append(edit)
disable_log.append('end')


if os.path.exists('disable_%s.txt' %vdom):
	os.remove('disable_log_%s.txt' %vdom)

for line in disable_log:
	with open('disable_log_%s.txt' %vdom, 'a') as cmd:
		cmd.write(line + '\n')


