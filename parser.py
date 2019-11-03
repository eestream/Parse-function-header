import re
import os

f=open('C:\\Users\\greedy\\Desktop\\sample header.h', 'r')
for line in f:
	pattern = '\s*(\w*)\s+(\w*)\s*\((.*)\);$'
	match = re.search(pattern, line)
	
	if match:
		ret = match.group(1)
		function_name = match.group(2)
		all_parameters = match.group(3)
		print("ret: " + ret)
		print ("function_name: " + function_name)
		print ("all_parameters: " + all_parameters)
		
		args = re.split(',', all_parameters)
		print (args)
		for i in args:
			i = re.sub('^\s+|\s+$', '', i)
			arg = re.split('\s+', i)
			
			if len(arg) == 3: #case1: const <type> <parameter>
				print("Parameter Type: " + arg[1])
				print("Parameter Value: " + arg[2])
			elif len(arg) == 2: #case2: <type> <parameter>
				print("Parameter Type: " + arg[0])
				print("Parameter Value: " + arg[1])
			print()		
			
		print ()
	else:
		#print("Pattern not found")
		print ()



f.close()

os.system("pause")
