from __future__ import absolute_import, division, print_function
from builtins import input
import signal
import os

vdom = input("VDOM name: ")
file = input("File with id rules name: ")
print("List of avaliabled commands:\n"
	  "set logtraffic all\n"
	  "set logtraffic utm\n"
	  "set logtraffic disable\n"
	  "set status disable\n"
	  "set status enable\n"
	  )
command = input("Command to be executabled: ")

commands = ["set logtraffic all","set logtraffic utm",
        	"set logtraffic disable","set status disable",
        	"set status enable"]

signal.signal(signal.SIGPIPE, signal.SIG_DFL) #IOError: Broken pine
signal.signal(signal.SIGINT, signal.SIG_DFL) #KeyboardInterrupt: Ctrl+C

try:
	if command not in commands:
		print("Command not allowed")
		exit()

	with open(file) as rules_file:
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
except Exception as e:
	print(e)

