#!/usr/bin/python
import sys
import re

def count( coll ):
	ret=0
	for x in coll:
		ret+= coll[x]
	return ret


if len(sys.argv) != 2:
	sys.exit("Not enough arguments")

file_name = sys.argv[1]

lines = [line.strip() for line in open(file_name)]

pattern = re.compile(r'.+?(Accepted (publickey|password)|Failed password)')

filtered = filter(pattern.search, lines)

ip_failed_dict = dict()
ip_accepted_dict = dict()

for x in filtered:
	line_list = x.split()
	if len(line_list) > 15:
		del line_list[8:10]
	if line_list[5] == "Failed":
		if line_list[10] in ip_failed_dict:
			if line_list[8] in ip_failed_dict[line_list[10]]:
				ip_failed_dict[line_list[10]][line_list[8]] = (ip_failed_dict[line_list[10]][line_list[8]]+1)
			else:
				ip_failed_dict[line_list[10]][line_list[8]] = 1	
		else:
			ip_failed_dict[line_list[10]] = dict()
			ip_failed_dict[line_list[10]][line_list[8]] = 1	

	else:
		if line_list[10] in ip_accepted_dict:
			if line_list[8] in ip_accepted_dict[line_list[10]]:
				ip_accepted_dict[line_list[10]][line_list[8]] = (ip_accepted_dict[line_list[10]][line_list[8]]+1)
			else:
				ip_accepted_dict[line_list[10]][line_list[8]] = 1	
		else:
			ip_accepted_dict[line_list[10]] = dict()
			ip_accepted_dict[line_list[10]][line_list[8]] = 1	

for x in ip_accepted_dict:
	if x in ip_failed_dict:
		f = count(ip_failed_dict[x])
		a = count(ip_accepted_dict[x])
		if f > a:
			print "{0} - {1} failed for {2} users - {3} accepted for {4} users".format(x,f,len(ip_failed_dict[x]),a,len(ip_accepted_dict[x]))