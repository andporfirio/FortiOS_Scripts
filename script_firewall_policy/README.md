### 1. Necessary modules ###
future.
builtins.
signal.
os.

Try: pip install future.

### Create a file with id policies ###
FGT01 # c v.
FGT01 (vdom) # edit Office.
FGT01 (Office) # config firewall policy.
FGT01 (policy) # edit ?.
policyid    Policy ID. (0-4294967294).
1.
1638.
1497.
9120.
1677.
1680.
1681.
1675.
1590.
1566.
1593.
1665.
1679.

Copy to a file and save at the same directory of the script.py, ex: id_rules.txt. 

### Executing the script ###
$ python script_rule.py.
VDOM name: Office.
File with id rules name: id_rules.txt.
List of commands:.
set logtraffic all.
set logtraffic utm.
set logtraffic disable.
set status disable.
set status enable.

Command to be executabled: set status disable.

### Example of created file ###
$ cat script_Office.conf.
config vdom.
edit Office.
config firewall policy.
edit 3.
set status disable.
next.
edit 4.
set status disable.
next.
edit 5.
set status disable.
next.
end.

### Importing to Fortigate ###.

Global > System > Advanced > Configuration Scripts > Upload and Run a New Script.