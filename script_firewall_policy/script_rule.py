import os
import sys

def config_firewall_policy():
	commands = ["set logtraffic all","set logtraffic utm",
            	"set logtraffic disable","set status disable",
            	"set status enable"]

	if len(sys.argv) < 4:
		print("Usage: script.py vdom rules.txt command")
	exit()

	vdom = sys.argv[1]
	command = sys.argv[3]

	if command not in commands:
		print("Command not allowed")
	exit()

	with open(sys.argv[2]) as rules_file:
		list01 = rules_file.readlines()

	rules = []
	script = []

	for line in list01:
		rules.append(line.strip())

	script.append('config vdom\nedit %s\nconfig firewall policy' %vdom)
	for line in rules:
		edit = ('edit %s\n%s\nnext' %(line,command))
		script.append(edit)
	script.append('end')


	if os.path.exists('script_%s.conf' %vdom):
		os.remove('script_%s.conf' %vdom)

	for line in script:
		with open('script_%s.conf' %vdom, 'a') as cmd:
			cmd.write(line + '\n')

config_firewall_policy()


